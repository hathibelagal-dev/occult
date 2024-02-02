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
    'GOTO', 'GOTO_E', 'GOTO_LE', 'GOTO_GE', 'GOTO_GT', 'GOTO_LT',
    'COMPARE',
    'AND'
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
t_GOTO_E      = r'(adire=|πόρευε=)'
t_GOTO_LE      = r'(adire<=|πόρευε<=)'
t_GOTO_GE      = r'(adire>=|πόρευε>=)'
t_GOTO_GT      = r'(adire>|πόρευε>)'
t_GOTO_LT      = r'(adire<|πόρευε<)'
t_GOTO        = r'(adire|πόρευε)'
t_END         = r'(terminus|finis|τέλος)'
t_ignore      = " \t\n"
t_NAME        = r'🕯️\|[a-zA-Z_][a-zA-Z0-9_]*'
t_PRINT       = r'(imprime|manifesta|exara|γρᾰ́φε)'
t_CONCATENATE = r'(concatena|συνδεῖ)'
t_COMPARE     = r'(compara|comparā|σύγκρισου)'
t_AND         = r'(et|καί)'
t_EXIT        = r'(exī|exi|ἐξέρχου)'

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
