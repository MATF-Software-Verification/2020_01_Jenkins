from typing import Tuple, Optional

from src.custom_exceptions import UnsupportedOperationException
from src.operations import Operations


def parser(raw_input: Optional[str] = None) -> Tuple[float, float, Operations]:
    if not raw_input:
        tokenized_input = input().split(' ')
    else:
        tokenized_input = raw_input.split(' ')

    x = float(tokenized_input[0])
    raw_operation = tokenized_input[1]
    y = float(tokenized_input[2])

    if raw_operation == '+':
        operation = Operations.ADD
    elif raw_operation == '-':
        operation = Operations.SUB
    elif raw_operation == '*':
        operation = Operations.MUL
    elif raw_operation == '/':
        operation = Operations.DIV
    else:
        raise UnsupportedOperationException(f'Unknown operation "{raw_operation}"')

    return x, y, operation
