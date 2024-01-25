import ply.yacc as y

from occult_lex import tokens

precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','UMINUS'),
)

variables = {}

def p_statement_equals(p):
    '''
    statement : NAME EQUALS expression END
    '''
    variables[p[1]] = p[3]
    print(variables)

def p_statement_expr(p):
    'statement : expression END'
    p[0] = p[1]

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[2]

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
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    print("Syntax error")
    print(p)

parser = y.yacc()
