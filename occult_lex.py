import ply.lex as l
import sys
from argparse import ArgumentParser

tokens = (
    'NAME',
    'INT',
    'FLOAT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQUALS',
    'LPAREN',
    'RPAREN',
)

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_ignore = " \t\n"

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(x):
    print("Lexing error: %s" % x.value[0])
    sys.exit(0)

occult_lex = l.lex()

program = None
with open(sys.argv[1], 'r') as f:
    program = f.read()

occult_lex.input(program)

while True:
    token = occult_lex.token()
    if not token:
        break
    print(token)
