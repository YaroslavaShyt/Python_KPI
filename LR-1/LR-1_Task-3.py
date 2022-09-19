import argparse


def check_values(formula):
    val = '0123456789+-'
    if not all(sym in val for sym in formula):
        return False
    return True


def check_signs(formula):
    sign = ['++', '+-', '-+', '--']
    if not all(s in sign for s in formula):
        return False
    return True


def main():
    flag = True
    parser = argparse.ArgumentParser(exit_on_error=False)  # Initialize the parser
    parser.add_argument('formula')
    try:
        args = parser.parse_args()   # Parse the arguments
        if check_values(args.formula) and check_signs(args.formula):
            print('Result = (', flag, ',', eval(args.formula), ')')
        else:
            print('Result = (', False, ', None)')
    except Exception as ex:
        print('Something went wrong:', ex)


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print("Something wrong:", ex)
