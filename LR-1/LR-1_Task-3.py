import argparse


def valid_formula(formula):
    val = '0123456789+-'
    sign = ['++', '+-', '-+', '--']
    incorrect_val = not all(sym in val for sym in formula)
    incorrect_op = any(s in formula for s in sign)
    if incorrect_val or incorrect_op:
        return False
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('formula')
    args = parser.parse_args()
    if valid_formula(args.formula):
        try:
            print(valid_formula(args.formula), eval(args.formula))
        except SyntaxError:
            print(valid_formula(args.formula), None)
    else:
        print(valid_formula(args.formula), None)


main()

