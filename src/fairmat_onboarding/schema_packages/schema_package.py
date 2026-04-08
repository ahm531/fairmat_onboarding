from collections.abc import Iterable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger

from nomad.config import config
from nomad.datamodel.data import (
    ArchiveSection,
    Schema,
    UseCaseElnCategory,
)
from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum
from nomad.metainfo import Datetime, MEnum, Quantity, SchemaPackage, Section, SubSection

configuration = config.get_plugin_entry_point(
    'fairmat_onboarding.schema_packages:schema_onboarding_entry_point'
)

m_package = SchemaPackage()

# Review group ID for FAIRmat PI Onboarding questionnaires
REVIEWER_GROUP_ID = 'fairmat-pi-onboarding-reviewers' # TODO replace with actual group ID once created


def _unique_clean(values: Iterable[str] | None) -> list[str]:
    out: list[str] = []
    for v in values or []:
        if v is None:
            continue
        cleaned = v.strip() if isinstance(v, str) else v
        if not cleaned:
            continue
        if cleaned not in out:
            out.append(cleaned)
    return out


class ResearchTopicTerm(ArchiveSection):
    m_def = Section(a_eln={'hide': ['value']})
    value = Quantity(type=str)


class MaterialSystemTerm(ArchiveSection):
    m_def = Section(a_eln={'hide': ['value']})
    value = Quantity(type=str)


class ResearchMethodTerm(ArchiveSection):
    m_def = Section(a_eln={'hide': ['value']})
    value = Quantity(type=str)


class ResearchFocus(ArchiveSection):
    m_def = Section(
        label='Research Focus',
        a_eln={
            'hide': [
                'research_topic_terms',
                'material_system_terms',
                'research_method_terms',
            ]
        },
    )

    research_type = Quantity(
    type=MEnum('1- Experimental', '2- Computational', '3- Both'),
    label='what best describes your research approach?',
    description='Select the option that best reflects your group’s primary research activities. '
        'Choose "Both" if your work combines experimental and computational methods.',
    a_eln=ELNAnnotation(component=ELNComponentEnum.RadioEnumEditQuantity),
    )

    research_topics = Quantity(
    type=str,
    shape=['*'],
    label='main research topics',
    description='List the main scientific topics or themes of your research '
        '(e.g., catalysis, quantum materials, energy storage, photovoltaics). '
        'Add one topic per line.',
    a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    material_systems = Quantity(
    type=str,
    shape=['*'],
    label='main material systems studied',
    description='List the material systems your group works on. This can include broad categories '
    '(e.g., polymers, 2D materials) or specific materials (e.g., MoS2, Si, GaAs). '
    'Add one material system per line.',
    a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    research_methods = Quantity(
    type=str,
    shape=['*'],
    label='main methods and techniques used',
    description='List the main experimental, computational, or analytical techniques used in your research '
    '(e.g., DFT, molecular dynamics, XRD, spectroscopy, microscopy). '
    'Add one technique per line.',
    a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    focus_description = Quantity(
        type=str,
        label='brief description of the research focus of your group',
        description='Describe your group’s research, including the main scientific problems or challenges '
        'you aim to address, and the general approach you take.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
    )

    fairmat_connection = Quantity(
        type=str,
        label='how does your research connect to FAIRmat\'s scientific scope?',
        description='Describe how your research aligns with FAIRmat, for example in terms of '
        'materials domains, data types, methods, or potential use of NOMAD.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
    )

    research_topic_terms = SubSection(section_def=ResearchTopicTerm, repeats=True)
    material_system_terms = SubSection(section_def=MaterialSystemTerm, repeats=True)
    research_method_terms = SubSection(section_def=ResearchMethodTerm, repeats=True)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
        self.research_topic_terms = [
            ResearchTopicTerm(value=v) for v in _unique_clean(self.research_topics)
        ]
        self.material_system_terms = [
            MaterialSystemTerm(value=v) for v in _unique_clean(self.material_systems)
        ]
        self.research_method_terms = [
            ResearchMethodTerm(value=v) for v in _unique_clean(self.research_methods)
        ]


class FileFormatTerm(ArchiveSection):
    m_def = Section(a_eln={'hide': ['value']})
    value = Quantity(type=str)


class ResearchData(ArchiveSection):
    m_def = Section(
        label='Research Data',
        a_eln={'hide': ['file_format_terms']},
    )

    name = Quantity(
    type=str,
    label='name of data entry',
    description='Provide a short descriptive name for this data entry to distinguish it from others '
    '(e.g., "DFT simulations of catalysts", "XRD characterization", "Device I–V measurements").',
    a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
)

    data_type = Quantity(
    type=MEnum(
        '1- DFT calculations',
        '2- Molecular dynamics simulations',
        '3- Spectroscopy data',
        '4- Microscopy data',
        '5- Device measurements',
        'Other',
    ),
    label='data type',
    description="Select the type of data that best describes this entry. If your data doesn't fit into any of the predefined categories, select 'Other' and provide a brief description in the next field.",
    a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
    )

    data_type_other = Quantity(
    type=str,
    label='other data type (please specify)',
    description='If you selected "Other", please specify the data type.',
    a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    volume = Quantity(
        type=str,
        label='approximate data volume per year',
        description='Provide an estimate of the data volume generated per year for this type of data (e.g., "100 GB/year", "1 TB/year").',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    software_instruments = Quantity(
        type=str,
        shape=['*'],
        label='software or instruments used',
        description='List the software or instruments used to generate, process, or analyze this data. '
        'This may include simulation codes, analysis software, specific ELN, or experimental instruments. '
        'For instruments, please include vendor and model if known (e.g., "Bruker D8 Advance"). '
        'Add one item per entry.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    file_format = Quantity(
        type=str,
        shape=['*'],
        label='file formats',
        description='List the file formats used for this data type (e.g., CSV, HDF5, TIFF, TXT, XYZ). '
        'Use common format names or file extensions. Add one format per entry.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    file_format_terms = SubSection(section_def=FileFormatTerm, repeats=True)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
        self.file_format_terms = [
            FileFormatTerm(value=v) for v in _unique_clean(self.file_format)
        ]


class TrainingTopicTerm(ArchiveSection):
    m_def = Section(a_eln={'hide': ['value']})
    value = Quantity(type=str)


class NomadServiceTerm(ArchiveSection):
    m_def = Section(a_eln={'hide': ['value']})
    value = Quantity(type=str)


class NomadUsage(ArchiveSection):
    m_def = Section(
        label='NOMAD Usage',
        a_eln={'hide': ['training_topic_terms', 'nomad_service_terms']},
    )

    using_nomad = Quantity(
        type=MEnum('Yes', 'No', 'Planning to'),
        label='are you currently using NOMAD?',
        a_eln=ELNAnnotation(component=ELNComponentEnum.RadioEnumEditQuantity),
    )

    nomad_services = Quantity(
        type=MEnum(
            '1- Central NOMAD',
            '2- NOMAD Oasis',
            '3- NOMAD CAMELS',
            '4- NORTH',
            '5- AI toolkit',
        ),
        shape=['*'],
        label='NOMAD services currently used by your group',
        a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
    )

    nomad_plugins_developed = Quantity(
        type=MEnum(
            '1- APIs',
            '2- Apps',
            '3- Example uploads',
            '4- Normalizers',
            '5- NORTH tools',
            '6- Parsers',
            '7- Schema packages',
            '8- Actions',
        ),
        shape=['*'],
        label='NOMAD plugins developed in your group',
        description='If your group has developed a NOMAD plugin, select the component types you have implemented. '
        'Leave this field empty if not applicable.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
    )

    nomad_plugin_details = Quantity(
        type=str,
        label='NOMAD plugin details (optional)',
        description=(
            'If applicable, briefly describe the NOMAD plugin your group has developed '
            '(e.g., purpose, functionality). You may also include a link to the repository '
            'or documentation (e.g., GitHub URL).'
        ),
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
    )

    training_topics = Quantity(
        type=MEnum(
            '1- Getting started with NOMAD',
            '2- Data management planning',
            '3- Metadata and data standards',
            '4- Plugin development',
            '5- ELN usage',
            '6- Hosting and administration of NOMAD Oasis',
            '7- Other',
        ),
        shape=['*'],
        label='which training topics are relevant for your group\'s current or upcoming needs?',
        description='Select the training topics that are relevant to your group\'s current or upcoming needs. '
        'Choose "Other" if not listed.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
    )

    training_topics_other = Quantity(
        type=str,
        label='other training topic (please specify)',
        description='If you selected "Other", please specify the training topic.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    nomad_challenges = Quantity(
        type=str,
        label='What are the main challenges preventing deeper use of NOMAD today?',
        description='Describe the main challenges that currently limit or prevent broader use of NOMAD in your group. '
        'This may include technical, organizational, training, or workflow-related challenges.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
    )

    nomad_workflows = Quantity(
        type=str,
        label='what workflows would you like to integrate with NOMAD?',
        description='Describe the research workflows, processes, or data handling steps that you would like to integrate '
        'with NOMAD.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
    )

    training_topic_terms = SubSection(section_def=TrainingTopicTerm, repeats=True)
    nomad_service_terms = SubSection(section_def=NomadServiceTerm, repeats=True)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
        self.training_topic_terms = [
            TrainingTopicTerm(value=v) for v in _unique_clean(self.training_topics)
        ]
        self.nomad_service_terms = [
            NomadServiceTerm(value=v) for v in _unique_clean(self.nomad_services)
        ]


class ResearchDataManagement(ArchiveSection):
    m_def = Section(label='Research Data Management')

    data_storage = Quantity(
    type=MEnum(
        '1- Local servers',
        '2- HPC storage',
        '3- Cloud',
        '4- External repositories',
        '5- Other',
    ),
    shape=['*'],
    label='how is research data currently stored?',
    description='Select all options that apply to your group’s current data storage practices. '
    'For "Other", please specify the storage solution in the next field.',
    a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
    )

    data_storage_other = Quantity(
    type=str,
    label='other storage solution (please specify)',
    description='If you selected "Other", please specify the storage solution used '
    '(e.g., custom infrastructure, partner systems).',
    a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    metadata_documentation = Quantity(
    type=MEnum(
        '1- Lab notebooks',
        '2- Electronic lab notebooks',
        '3- Scripts / workflow managers',
        '4- Spreadsheets',
        '5- Catalogues',
        '6- Other',
    ),
    shape=['*'],
    label='how is metadata documented?',
    description='Select all options that apply to how your group documents metadata and experimental/computational details. ',
    a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
    )

    metadata_documentation_other = Quantity(
    type=str,
    label='other metadata documentation method (please specify)',
    description='If you selected "Other", please specify how metadata is documented '
    '(e.g., custom databases, LIMS, internal tools).',
    a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
)

    existing_standards = Quantity(
        type=str,
        label='are there existing standards or schemas used in your group?',
        description='List any standards, ontologies, or metadata schemas used in your group '
        '(e.g., NeXus, CIF, JSON schemas, domain-specific standards). '
        'Provide names and brief details if relevant.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
    )

    research_data = SubSection(section_def=ResearchData, repeats=True)


class OnboardingAdministration(ArchiveSection):
    m_def = Section(label='Onboarding administration (for onboarding team use)')

    interview_status = Quantity(
        type=MEnum('1- In planning', '2- Scheduled', '3- Completed'),
        label='interview status',
        a_eln=ELNAnnotation(component=ELNComponentEnum.RadioEnumEditQuantity),
    )

    interview_date = Quantity(
        type=Datetime,
        label='interview date',
        a_eln=ELNAnnotation(component=ELNComponentEnum.DateTimeEditQuantity),
    )

    interviewers = Quantity(
        type=str,
        label='interviewers',
        description='Name(s) of the interviewer(s) who conducted or will conduct the interview.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    remarks = Quantity(
        type=str,
        label='remarks',
        description='Internal notes for the onboarding team.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
    )

    letter_of_commitment = Quantity(
        type=str,
        label='Letter of Commitment (LoC)',
        description='Upload the signed Letter of Commitment.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.FileEditQuantity),
    )


class InstitutionTerm(ArchiveSection):
    m_def = Section(a_eln={'hide': ['value']})
    value = Quantity(type=str)


class FairmatAreaTerm(ArchiveSection):
    m_def = Section(a_eln={'hide': ['value']})
    value = Quantity(type=str)


class RelatedProjectTerm(ArchiveSection):
    m_def = Section(a_eln={'hide': ['value']})
    value = Quantity(type=str)


class PIOnboardingQuestionnaire(Schema):
    m_def = Section(
        label='FAIRmat PI Onboarding',
        categories=[UseCaseElnCategory],
        a_eln={
            'hide': [
                'institution_terms',
                'fairmat_area_terms',
                'related_project_terms',
            ]
        },
    )

    pi_name = Quantity(
        type=str,
        label='full name',
        description='Full name (first name and last name) of the PI.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    institutions = Quantity(
        type=str,
        shape=['*'],
        label='institution(s)',
        description='Institution(s) the PI is affiliated with.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    research_group = Quantity(
        type=str,
        label='research group name or department',
        description='Name of the research group or department.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    research_group_webpage = Quantity(
        type=str,
        label='webpage',
        default='https://www.example.com',
        description='URL of the research group or department webpage.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.URLEditQuantity),
    )

    fairmat_areas = Quantity(
        type=MEnum(
            'Area A - Synthesis',
            'Area B - Experiment',
            'Area C - Computation',
            'Area D - Data modeling and interoperability',
            'Area E - Digital infrastructure',
            'Area F - Enabling data-driven science',
            'Area G - Outreach',
            'Area H - Management',
        ),
        shape=['*'],
        label='FAIRmat Area(s)',
        description='FAIRmat area(s) the PI is associated with.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
    )

    RDM_contact_person = Quantity(
        type=str,
        label='main contact person for data management / NOMAD administration',
        description='Name of the person responsible for research data management'
        'in your group. This may be a data steward, lab manager, or another group member who can serve as the main contact for feedback and support related to data management and NOMAD usage.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    RDM_contact_role = Quantity(
        type=str,
        label='role of contact person',
        description='Role or position of the contact person within the group '
        '(e.g., data steward, postdoc, PhD student, lab manager).',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )
    RDM_contact_email = Quantity(
        type=str,
        label='email of contact person',
        description='Email address of the contact person responsible for research data management '
        'or NOMAD administration.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    related_projects = Quantity(
        type=str,
        shape=['*'],
        label='Are you involved in related projects or initiatives, e.g., CRCs, RTGs, EXC, FOR, etc.?',
        description='Examples: CRCs, RTGs, EXC, EU Projects, International Collaborations, Other NFDI Consortia?. Please provide the name of each project/initiative.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    expectations_from_fairmat = Quantity(
    type=str,
    label='what do you expect to gain from FAIRmat?',
    description=(
        'Please describe your expectations from FAIRmat. This may include support with '
        'research data management, tools for data handling and analysis, training needs, '
        'collaboration opportunities, or integration with your existing workflows.'
    ),
    a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
)

    research_focus = SubSection(section_def=ResearchFocus)
    research_data_management = SubSection(section_def=ResearchDataManagement)
    NOMAD_usage = SubSection(section_def=NomadUsage)
    onboarding_administration = SubSection(section_def=OnboardingAdministration)
    institution_terms = SubSection(section_def=InstitutionTerm, repeats=True)
    fairmat_area_terms = SubSection(section_def=FairmatAreaTerm, repeats=True)
    related_project_terms = SubSection(section_def=RelatedProjectTerm, repeats=True)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
        self.institution_terms = [
            InstitutionTerm(value=v) for v in _unique_clean(self.institutions)
        ]
        self.fairmat_area_terms = [
            FairmatAreaTerm(value=v) for v in _unique_clean(self.fairmat_areas)
        ]
        self.related_project_terms = [
            RelatedProjectTerm(value=v) for v in _unique_clean(self.related_projects)
        ]

        # Add the reviewer group if not already present
        if REVIEWER_GROUP_ID not in archive.metadata.reviewer_groups:
            archive.metadata.reviewer_groups.append(REVIEWER_GROUP_ID)


m_package.__init_metainfo__()
