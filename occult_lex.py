import ply.lex as l
import sys

tokens = (
    'STRING',
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
    'LSQUARE',
    'RSQUARE',
    'END',
    'PRINT',
    'CONCATENATE',
    'COMMA',
    'LABEL',
    'COLON',
    'GOTO',
)

t_COMMA       = r','
t_PLUS        = r'\+'
t_MINUS       = r'-'
t_TIMES       = r'\*'
t_DIVIDE      = r'/'
t_EQUALS      = r'='
t_LPAREN      = r'\('
t_RPAREN      = r'\)'
t_LSQUARE     = r'\['
t_RSQUARE     = r'\]'
t_LABEL       = r'(signum|titulus|σημείο|σημάδι)'
t_COLON       = r':'
t_GOTO        = r'(adire|πόρευε)'
t_END         = r'(terminus|finis|τέλος)'
t_ignore      = " \t\n"
t_NAME        = r'🕯️\|[a-zA-Z_][a-zA-Z0-9_]*'
t_PRINT       = r'(imprime|manifesta|exara|γρᾰ́φε)'
t_CONCATENATE = r'(concatena|συνδεῖ)'

def t_STRING(t):
    r'\".*?\"'
    t.value = str(t.value)[1:-1]
    return t

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

lexer = l.lex()
