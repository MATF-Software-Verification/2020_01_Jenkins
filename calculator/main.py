""" Toy calculator project which only purpose is being tested on Jenkins. """
from src import parser, calculate


def main():
    x, y, operation = parser()
    result = calculate(x, y, operation)

    print(result)


if __name__ == '__main__':
    main()

