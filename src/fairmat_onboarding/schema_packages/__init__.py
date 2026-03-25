from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class FAIRmatOnboardingPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from fairmat_onboarding.schema_packages.schema_package import m_package

        return m_package


schema_onboarding_entry_point = FAIRmatOnboardingPackageEntryPoint(
    name='FAIRmat_onboarding_questionaire',
    description='This NOMAD schema plugin provides a structured questionnaire designed '
    'to collect key information from newly onboarded FAIRmat Principal Investigators (PIs).',
)
