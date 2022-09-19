import argparse
import ast
import math
import operator


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("function")
    parser.add_argument("args", nargs='*')
    p = parser.parse_args()
    try:
        if p.function in dir(math):
            func = getattr(math, p.function)
        else:
            func = getattr(operator, p.function)
    except AttributeError:
        raise AttributeError(f"The function {p.function} is not defined.")
    try:
        args = [ast.literal_eval(arg) for arg in p.args]
    except SyntaxError:
        raise SyntaxError(f"The arguments to {p.function}"
                          f"were not properly formatted.")
    print(func(*args))


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print("Something wrong:", ex)
