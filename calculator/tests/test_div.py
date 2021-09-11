import pytest

from src.operations import divide


@pytest.mark.parametrize('x, y, expected', [
    (2098089, 4019119, 0.5220270910117366),
    (1558472381, 999852445, 1.5587023753289917),
    (1000000000000, 1202004389984, 0.8319437169554024)
])
def test_divide_big_integers(x, y, expected):
    assert divide(x, y) == expected


@pytest.mark.parametrize('x, y, expected', [
    (0.251, 5.2545, 0.047768579312969836),
    (1.28, -999852445, -1.2801888982728847e-09),
    (235.9, 10e-4, 235900.0)
])
def test_divide_floats(x, y, expected):
    assert divide(x, y) == expected
