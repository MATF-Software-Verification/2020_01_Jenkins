import pytest

from src.operations import subtract


@pytest.mark.parametrize('x, y, expected', [
    (2098089, 4019119, -1921030),
    (1558472381, 999852445, 558619936),
    (1000000000000, 1202004389984, -202004389984)
])
def test_subtract_big_integers(x, y, expected):
    assert subtract(x, y) == expected


@pytest.mark.parametrize('x, y, expected', [
    (0.251, 5.2545, -5.0035),
    (1.28, 999852445, -999852443.72),
    (235.9, 10e-4, 235.899)
])
def test_subtract_floats(x, y, expected):
    assert subtract(x, y) == expected
