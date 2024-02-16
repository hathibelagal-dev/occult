from occult_parser import parser
from occult_gen import items
import argparse
import sys

ap = argparse.ArgumentParser(
    prog = "Occult",
    description = "A very occult/sacred-looking language",
    epilog = "Dominus vobiscum"
)

ap.add_argument('input_program')
ap.add_argument('-t', '--translate_to', choices = [
    'ast',
    'json',
    'js',
    'python',
    'perl',
    'ruby',
    'bash'
], default = 'ast')
ap.add_argument('-o', '--output_filename', default = 'occ.out')

args = ap.parse_args()

if not args.input_program:
    sys.exit(2)

with open(sys.argv[1], 'r') as f:
    program = f.read()
    ast = parser.parse(program)
    items(ast, args.translate_to, args.output_filename)
