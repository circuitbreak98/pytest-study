import pytest
from calculator import add, divide

@pytest.fixture
def sample_numbers():
    return (10,2)

def test_add_with_fixture(sample_numbers):
    a, b = sample_numbers
    assert add(a,b) == 12

@pytest.mark.parametrize("a,b,expected", [
    (6,3,2),
    (10,2,5),
    (9,3,3),
    ])
def test_divide_parametrize(a,b,expected):
    assert divide(a,b) == expected

