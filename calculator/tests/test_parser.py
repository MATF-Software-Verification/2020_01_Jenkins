import pytest

from src.custom_exceptions import UnsupportedOperationException
from src.custom_parser import parser
from src.operations import Operations


@pytest.mark.parametrize('raw_input, x, y', [
    ('4 + 2', 4, 2),
    ('4.3 + 1.2', 4.3, 1.2),
    ('0.0003 + 88888', 0.0003, 88888)
])
def test_parser_add(raw_input, x, y):
    parsed_x, parsed_y, operator = parser(raw_input)
    assert parsed_x == x
    assert parsed_y == y
    assert operator == Operations.ADD


@pytest.mark.parametrize('raw_input, x, y', [
    ('4 - 2', 4, 2),
    ('4.3 - 1.2', 4.3, 1.2),
    ('0.0003 - 88888', 0.0003, 88888),
    ('0 - 585', 0, 585)
])
def test_parser_sub(raw_input, x, y):
    parsed_x, parsed_y, operator = parser(raw_input)
    assert parsed_x == x
    assert parsed_y == y
    assert operator == Operations.SUB


@pytest.mark.parametrize('raw_input, x, y', [
    ('1.01 * 2', 1.01, 2),
    ('42 * 42', 42, 42),
    ('0.0003 * 88888', 0.0003, 88888),
    ('0 * 1', 0, 1)
])
def test_parser_mul(raw_input, x, y):
    parsed_x, parsed_y, operator = parser(raw_input)
    assert parsed_x == x
    assert parsed_y == y
    assert operator == Operations.MUL


@pytest.mark.parametrize('raw_input, x, y', [
    ('22.34 / 2', 22.34, 2),
    ('4.3 / 4.1', 4.3, 4.1),
    ('123 / 123', 123, 123),
    ('0 / 0', 0, 0)
])
def test_parser_div(raw_input, x, y):
    parsed_x, parsed_y, operator = parser(raw_input)
    assert parsed_x == x
    assert parsed_y == y
    assert operator == Operations.DIV

@pytest.mark.parametrize('raw_input', [
    '1 // 3',
    '2 ** 4',
    '4 . 2'
    '5 ^ 1'
])
def test_parser_raises_exception(raw_input):
    with pytest.raises(UnsupportedOperationException):
        parser(raw_input)
