import os.path

from nomad.client import normalize_all, parse


def test_schema_package():
    test_file = os.path.join('tests', 'data', 'test.archive.yaml')
    entry_archive = parse(test_file)[0]
    normalize_all(entry_archive)

    data = entry_archive.data
    assert data.pi_name == 'Dr. Jane Doe'
    assert 'Humboldt-Universität zu Berlin' in data.institutions
    assert data.research_group == 'Computational Materials Science Group'
    assert 'Area C - Computation' in data.fairmat_areas
    assert data.RDM_contact_email == 'john.smith@hu-berlin.de'
    assert data.research_focus.research_type == '2- Computational'
    assert data.NOMAD_usage.using_nomad == 'Yes'
    assert '4- Plugin development' in data.NOMAD_usage.training_topics
    assert data.research_data_management.research_data[0].data_type == '1- DFT calculations'
