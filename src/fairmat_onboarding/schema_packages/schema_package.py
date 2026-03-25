from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger

from nomad.config import config
from nomad.datamodel.data import ArchiveSection, Schema, UseCaseElnCategory
from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum
from nomad.metainfo import MEnum, Quantity, SchemaPackage, Section, SubSection

configuration = config.get_plugin_entry_point(
    'fairmat_onboarding.schema_packages:schema_onboarding_entry_point'
)

m_package = SchemaPackage()


class ResearchFocus(ArchiveSection):
    m_def = Section(label='Research Focus')

    focus_description = Quantity(
        type=str,
        label='Brief description of the research focus of your group',
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
    )

    main_topics = Quantity(
        type=str,
        shape=['*'],
        label='Main research topics',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    research_type = Quantity(
        type=MEnum('Experimental', 'Computational', 'Both'),
        label='What best describes your research approach?',
        a_eln=ELNAnnotation(component=ELNComponentEnum.RadioEnumEditQuantity),
    )

    key_materials_methods = Quantity(
        type=str,
        label='Key materials systems / methods studied',
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
    )

    fairmat_connection = Quantity(
        type=str,
        label='How does your research connect to FAIRmat\'s scientific scope?',
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
    )


class ResearchDataManagement(ArchiveSection):
    m_def = Section(label='Research Data Management')

    # --- Section 3: Research Data Landscape ---

    data_types = Quantity(
        type=MEnum(
            'DFT calculations',
            'Molecular dynamics simulations',
            'Spectroscopy data',
            'Microscopy data',
            'Device measurements',
            'Other',
        ),
        shape=['*'],
        label='What types of data does your group primarily generate?',
        a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
    )

    data_volume_per_year = Quantity(
        type=str,
        label='Approximate data volume generated per year',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    typical_data_formats = Quantity(
        type=str,
        shape=['*'],
        label='Typical data formats',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    workflow_stages = Quantity(
        type=str,
        label='Typical workflow stages where data is generated',
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
    )

    # --- Section 4: Current RDM Practices ---

    data_storage = Quantity(
        type=MEnum(
            'Local servers',
            'HPC storage',
            'Cloud',
            'External repositories',
            'Other',
        ),
        shape=['*'],
        label='How is research data currently stored?',
        a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
    )

    metadata_documentation = Quantity(
        type=MEnum(
            'Lab notebooks',
            'Electronic lab notebooks',
            'Scripts / workflow managers',
            'Spreadsheets',
            'Databases',
            'Other',
        ),
        shape=['*'],
        label='How is experimental or computational metadata documented?',
        a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
    )

    existing_standards = Quantity(
        type=str,
        label='Are there existing standards or metadata schemas used in your group?',
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
    )

    rdm_responsible = Quantity(
        type=str,
        label='Who in the group is responsible for data management or infrastructure?',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    # --- Section 5: NOMAD and FAIRmat Usage ---

    using_nomad = Quantity(
        type=MEnum('Yes', 'No', 'Planning to'),
        label='Are you currently using NOMAD?',
        a_eln=ELNAnnotation(component=ELNComponentEnum.RadioEnumEditQuantity),
    )

    nomad_services = Quantity(
        type=MEnum(
            'Central NOMAD',
            'NOMAD Oasis',
            'NOMAD Apps',
            'NOMAD plugins',
            'NOMAD CAMELS',
            'Other',
        ),
        shape=['*'],
        label='Which NOMAD services are currently used?',
        a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
    )

    training_topics = Quantity(
        type=MEnum(
            'Getting started with NOMAD',
            'Data management planning',
            'Metadata and data standards',
            'Plugin development',
            'ELN usage',
            'Hosting and administration of NOMAD Oasis',
        ),
        shape=['*'],
        label='Which training topics are relevant for your group\'s current or upcoming needs?',
        a_eln=ELNAnnotation(component=ELNComponentEnum.EnumEditQuantity),
    )

    nomad_challenges = Quantity(
        type=str,
        label='What are the main challenges preventing deeper use of NOMAD today?',
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
    )

    nomad_workflows = Quantity(
        type=str,
        label='What workflows would you like to integrate with NOMAD?',
        a_eln=ELNAnnotation(component=ELNComponentEnum.RichTextEditQuantity),
    )


class PIOnboardingQuestionnaire(Schema):
    m_def = Section(
        label='FAIRmat PI Onboarding',
        categories=[UseCaseElnCategory],
    )

    pi_name = Quantity(
        type=str,
        label='PI Full Name',
        description='Full name of the Principal Investigator.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    institutions = Quantity(
        type=str,
        shape=['*'],
        label='Institution(s)',
        description='Institution(s) the PI is affiliated with.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    research_group = Quantity(
        type=str,
        label='Research Group / Department',
        description='Name of the research group or department.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    research_group_webpage = Quantity(
        type=str,
        label='Webpage of the Research Group / Department',
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
        label='Main Contact Person for Data Management in your group (if different)',
        description='Name of the main contact person for data management, if different from the PI.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    RDM_contact_email = Quantity(
        type=str,
        label='Email of Contact Person',
        description='Email address of the main contact person for data management.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    related_projects = Quantity(
        type=str,
        shape=['*'],
        label='Are you involved in related projects or initiatives, e.g., CRCs, RTGs, EXC, FOR, etc.?',
        description='Examples: CRCs, RTGs, EXC, EU Projects, International Collaborations, Other NFDI Consortia?. Please provide the name of each project/initiative.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity),
    )

    research_focus = SubSection(section_def=ResearchFocus)
    research_data_management = SubSection(section_def=ResearchDataManagement)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)


m_package.__init_metainfo__()
