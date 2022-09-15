import argparse
import re
parser = argparse.ArgumentParser(exit_on_error=False)     # Initialize the parser
parser.add_argument('formula')
args = parser.parse_args()
print(args.formula)
