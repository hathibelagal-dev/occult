from occult_parser import parser
from occult_gen import items
import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <file>")
    sys.exit(2)

with open(sys.argv[1], 'r') as f:
    program = f.read()
    ast = parser.parse(program)
    items(ast)
