import pytest

from src.operations import add


@pytest.mark.parametrize('x, y, expected', [
    (2098089, 4019119, 6117208),
    (1558472381, 999852445, 2558324826),
    (1000000000000, 1202004389984, 2202004389984)
])
def test_add_big_integers(x, y, expected):
    assert add(x, y) == expected


@pytest.mark.parametrize('x, y, expected', [
    (0.251, 5.2545, 5.5055000000000005),
    (1.28, 999852445, 999852446.28),
    (235.9, 10e-4, 235.901)
])
def test_add_floats(x, y, expected):
    assert add(x, y) == expected


@pytest.mark.parametrize('x, y, z', [
    (5, 6, 1),
    (1558472381, 999852445, 12),
    (1e6, 24e-6, 42),
])
def test_add_associative_property(x, y, z):
    assert add(add(x, y), z) == add(x, add(y, z))


@pytest.mark.parametrize('x, y', [
    (5, -6),
    (1558472381, 999852445),
    (1e6, 24e-6),
])
def test_add_commutative_property(x, y):
    assert add(x, y) == add(y, x)
