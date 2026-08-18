import pytest

@pytest.fixture
def setup():
    print("Setting up the test environment...")
    yield
    print("Tearing down the test environment...")

@pytest.mark.group1
def test_marker_groups(setup):
    assert 1 + 1 == 2


@pytest.mark.group2
def test_marker_groups_2(setup):
    assert 2 + 2 == 4   

@pytest.mark.group1
def test_marker_groups_3(setup):
    assert 3 + 3 == 6


@pytest.mark.great
def test_greater(setup):
   num = 100
   assert num > 100

@pytest.mark.great
def test_greater_equal(setup):
   num = 100
   assert num >= 100

@pytest.mark.others
def test_less(setup):
   num = 100
   assert num < 200


