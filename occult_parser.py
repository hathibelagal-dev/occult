import ply.yacc as y
import sys
from occult_lex import tokens

class _ParsingData:
    def __init__(self):
        self.line_number = None
        self.positions = {}
        self.current_line_number = 0

    def get_next_line(self, current):
        if not self.line_number:
            self.current_line_number = current
            return current + 1
        else:
            x = self.line_number
            self.line_number = None
            return x

ParsingData = _ParsingData()

precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
)

variables = {}

def p_block(p):
    '''
    block : block statement
            | statement
    '''

def p_array(p):
    '''
    expression : LSQUARE sequence RSQUARE
    '''
    p[0] = p[2]

def p_sequence_single(p):
    '''
    sequence : expression
    '''
    p[0] = [p[1]]

def p_sequence_multiple(p):
    '''
    sequence : expression COMMA sequence
    '''
    p[0] = [p[1]] + p[3]

def p_statement_label(p):
    'statement : LABEL NAME COLON'
    ParsingData.positions[p[2]] = ParsingData.current_line_number + 2

def p_statement_goto(p):
    'statement : GOTO NAME'
    if p[2] in ParsingData.positions:
        ParsingData.line_number = ParsingData.positions[p[2]]
    else:
        print("Indēterminātum: " + p[2])
        sys.exit(1)

def p_statement_equals(p):
    '''
    statement : NAME EQUALS expression END
    '''
    variables[p[1]] = p[3]

def p_statement_out(p):
    '''
    statement : PRINT expression END
    '''
    print(p[2])

def p_statement_expr(p):
    'statement : expression END'
    p[0] = p[1]

def p_expression_concatenate(p):
    'expression : expression CONCATENATE expression'
    p[0] = str(p[1]) + str(p[3])

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_int(p):
    'factor : INT'
    p[0] = p[1]

def p_factor_float(p):
    'factor : FLOAT'
    p[0] = p[1]

def p_factor_variable(p):
    'factor : NAME'
    if p[1] in variables:
        p[0] = variables[p[1]]
    else:
        print("Indēterminātum: " + p[1])
        sys.exit(1)

def p_factor_array_variable(p):
    'factor : NAME LSQUARE INT RSQUARE'
    if p[1] in variables and type(variables[p[1]]) is list and len(variables[p[1]]) > p[3]:
        p[0] = variables[p[1]][p[3]]
    else:
        print(f"Indēterminātum: {p[1]}[{p[3]}]")
        sys.exit(1)

def p_factor_string(p):
    'factor : STRING'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    if p:
        print("Error syntaxis 💀")
        sys.exit(3)

parser = y.yacc()
