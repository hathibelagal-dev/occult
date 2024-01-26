from occult_parser import parser
import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <file>")
    sys.exit(2)

with open(sys.argv[1], 'r') as f:
    program = f.read()
    parser.parse(program)
