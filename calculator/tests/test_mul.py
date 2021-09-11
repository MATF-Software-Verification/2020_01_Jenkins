import pytest

from src.operations import multiply


@pytest.mark.parametrize('x, y, expected', [
    (2098089, 4019119, 8432469363591),
    (1558472381, 999852445, 1558242420607821545),
    (1000000000000, 1202004389984, 1202004389984000000000000)
])
def test_multiply_big_integers(x, y, expected):
    assert multiply(x, y) == expected


@pytest.mark.parametrize('x, y, expected', [
    (0.251, 5.2545, 1.3188795),
    (1.28, 999852445, 1279811129.6000001),
    (235.9, 10e-4, 0.2359)
])
def test_multiply_floats(x, y, expected):
    assert multiply(x, y) == expected


@pytest.mark.parametrize('x, y, z', [
    (5, 6, 1),
    (1558472381, 999852445, 12),
    (1e6, 24e-6, 42),
])
def test_multiply_associative_property(x, y, z):
    assert multiply(multiply(x, y), z) == multiply(x, multiply(y, z))


@pytest.mark.parametrize('x, y', [
    (5, -6),
    (1558472381, 999852445),
    (1e6, 24e-6),
])
def test_multiply_commutative_property(x, y):
    assert multiply(x, y) == multiply(y, x)
