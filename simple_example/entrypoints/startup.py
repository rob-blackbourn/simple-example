"""The entrypoint for calculate"""

import sys

from simple_example import calculate


def main():
    calculate(sys.argv[1:])


if __name__ == '__main__':
    main()
