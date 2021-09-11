from math import isclose

import pytest

from src.operations import add, multiply


@pytest.mark.parametrize('x, y, z', [
    (0.251, 5.2545, 1.3188795),
    (1.28, 999852445, 1279811129.6000001),
    (235.9, 10e-4, 0.2359),
    (5, 6, 1),
    (1558472381, 999852445, 12),
    (1e6, 24e-6, 42)
])
def test_distributive_property(x, y, z):
    assert isclose(multiply(x, add(y, z)), add(multiply(x, y), multiply(x, z)))

