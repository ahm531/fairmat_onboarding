import os.path

from nomad.client import normalize_all, parse

from fairmat_onboarding.schema_packages.schema_package import REVIEWER_GROUP_ID


def test_schema_package():
    test_file = os.path.join('tests', 'data', 'test.archive.yaml')
    entry_archive = parse(test_file)[0]
    normalize_all(entry_archive)

    data = entry_archive.data
    assert data.pi_name == 'Dr. Jane Doe'
    assert any('Humboldt' in i for i in (data.institutions or []))
    assert data.research_group == 'Computational Materials Science Group'
    assert 'Area C - Computation' in data.fairmat_areas
    assert data.RDM_contact_email == 'john.smith@hu-berlin.de'
    assert data.research_focus.research_type == '2- Computational'
    assert data.NOMAD_usage.using_nomad == 'Yes'
    assert '4- Plugin development' in data.NOMAD_usage.training_topics
    assert data.research_data_management.research_data[0].data_type == '1- DFT calculations'


def test_reviewer_group_added():
    """Test that the reviewer group is automatically added during normalization."""
    test_file = os.path.join('tests', 'data', 'test.archive.yaml')
    entry_archive = parse(test_file)[0]

    # Verify reviewer_groups is empty before normalization
    assert entry_archive.metadata.reviewer_groups == []

    normalize_all(entry_archive)

    # Verify reviewer_groups contains the expected group ID after normalization
    assert REVIEWER_GROUP_ID in entry_archive.metadata.reviewer_groups
    assert len(entry_archive.metadata.reviewer_groups) == 1


def test_reviewer_group_not_duplicated():
    """Test that the reviewer group is not duplicated if already present."""
    test_file = os.path.join('tests', 'data', 'test.archive.yaml')
    entry_archive = parse(test_file)[0]

    # Pre-add the reviewer group
    entry_archive.metadata.reviewer_groups = [REVIEWER_GROUP_ID]

    normalize_all(entry_archive)

    # Verify it wasn't duplicated
    assert entry_archive.metadata.reviewer_groups.count(REVIEWER_GROUP_ID) == 1
    assert len(entry_archive.metadata.reviewer_groups) == 1
