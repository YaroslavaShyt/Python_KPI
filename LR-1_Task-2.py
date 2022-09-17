import argparse
import ast
import math
import operator


def main():
    # parse arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("function")
    parser.add_argument("args", nargs='*')
    opt = parser.parse_args()

    # try to get the function from the operator module
    try:
        if opt.function in dir(math):
            func = getattr(math, opt.function)
        else:
            func = getattr(operator, opt.function)
    except AttributeError:
        raise AttributeError(f"The function {opt.function} is not defined.")

    # try to safely eval the arguments
    try:
        args = [ast.literal_eval(arg) for arg in opt.args]
    except SyntaxError:
        raise SyntaxError(f"The arguments to {opt.function}"
                          f"were not properly formatted.")

    # run the function and pass in the args, print the output to stdout
    print(func(*args))


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print("Something wrong:", ex)
