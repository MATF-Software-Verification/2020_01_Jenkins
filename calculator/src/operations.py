from enum import Enum
from src.custom_exceptions import UnsupportedOperationException


class Operations(Enum):
    ADD = '+'
    SUB = '-'
    MUL = '*'
    DIV = '/'

    def __str__(self):
        return self.value


def add(x: float, y: float) -> float:
    return x + y


def subtract(x: float, y: float) -> float:
    return x + y


def multiply(x: float, y: float) -> float:
    return x * y


def divide(x: float, y: float) -> float:
    return x / y


def calculate(x: float, y: float, operation: Operations) -> float:
    if operation == Operations.ADD:
        return add(x, y)
    elif operation == Operations.SUB:
        return subtract(x, y)
    elif operation == Operations.MUL:
        return multiply(x, y)
    elif operation == Operations.DIV:
        return divide(x, y)
    else:
        raise UnsupportedOperationException(f'Unknown operator "{operation}"')
