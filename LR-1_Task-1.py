import argparse


def calculation(x, operator, y):
    match operator:
        case '+':
            print(x + y)
        case '-':
            print(x - y)
        case '*':
            print(x * y)
        case '/':
            try:
                print(x / y)
            except ZeroDivisionError:
                print('Division by zero error!')
        case _:
            raise Exception('no operator found')


def main():
    parser = argparse.ArgumentParser(exit_on_error=False)  # Initialize the parser
    parser.add_argument('x', type=float)                   # Add parameters positional/optional
    parser.add_argument('operator')
    parser.add_argument('y', type=float)
    try:
        args = parser.parse_args()                        # Parse the arguments
        calculation(args.x, args.operator, args.y)
    except Exception as ex:
        print('Something went wrong. Check values or operator:', ex)


main()  # Run code
