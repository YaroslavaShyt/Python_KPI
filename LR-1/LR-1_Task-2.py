import argparse
import math
import operator


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('function')
    parser.add_argument('x')
    parser.add_argument('y')
    args = parser.parse_args()
    try:
        if args.function in dir(math):
            func = getattr(math, args.function)
        else:
            func = getattr(operator, args.function)
        print(func(float(args.x), float(args.y)))
    except AttributeError:
        print('Error: incorrect operator.')
    except ZeroDivisionError:
        print('Error: do not divide by 0.')
    except ValueError:
        print('Error: incorrect operand.')


main()
