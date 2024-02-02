from occult_parser import parser, ParsingData
import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <file>")
    sys.exit(2)

with open(sys.argv[1], 'r') as f:
    program = f.read()
    lines = program.split("\n")
    i = 0
    while True:
        line = lines[i]
        parser.parse(line)
        i = ParsingData.get_next_line(i)
        if i >= len(lines):
            break
