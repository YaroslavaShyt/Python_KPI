import argparse
import operator


ops = {'+': operator.add,
       '-': operator.sub,
       '*': operator.mul,
       '/': operator.truediv}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('x')
    parser.add_argument('op')
    parser.add_argument('y')
    args = parser.parse_args()
    try:
        print(ops[args.op](float(args.x), float(args.y)))
    except ZeroDivisionError:
        print('Error: do not divide by 0.')
    except KeyError:
        print('Error: you chose wrong operator.')
    except ValueError:
        print('Error: incorrect operand.')


main()
