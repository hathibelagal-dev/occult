import ply.yacc as y
import sys
from occult_lex import tokens

precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
)

def p_program(p):
    '''
    program : statement_list
    '''
    p[0] = ('OCCULT_PROGRAM', p[1])

def p_statement_list(p):
    '''
    statement_list : statement
                   | statement_list statement
    '''
    n = len(p)
    if n == 2 and p[1]:
        p[0] = [p[1]]
    elif n == 3:
        p[0] = p[1] + [p[2]]

def p_array(p):
    '''
    expression : LSQUARE sequence RSQUARE
    '''
    p[0] = ('OCCULT_ARRAY', p[2])

def p_sequence_single(p):
    '''
    sequence : expression
    '''
    p[0] = ('OCCULT_ONE-VALUE-ARRAY', p[1])

def p_sequence_multiple(p):
    '''
    sequence : expression COMMA sequence
    '''
    p[0] = ('OCCULT_MULTI-VALUE-ARRAY', p[1], p[3])

def p_statement_equals(p):
    '''
    statement : NAME EQUALS expression END
    '''
    p[0] = ('OCCULT_VARIABLE-ASSIGNMENT', p[1], p[3])

def p_statement_exit(p):
    '''
    statement : EXIT
    '''
    p[0] = ('OCCULT_EXIT', None)

def p_statement_out(p):
    '''
    statement : PRINT expression END
    '''
    p[0] = ('OCCULT_STATEMENT-OUT', p[2])

def p_statement_expr(p):
    'statement : expression END'
    p[0] = ('OCCULT_STATEMENT-EXPRESSION', p[1]) 

def p_expression_concatenate(p):
    'expression : expression CONCATENATE expression'
    p[0] = ('OCCULT_STATEMENT-CONCAT', p[1], p[3])

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = ('OCCULT_EXPRESSION-PLUS', p[1], p[3])

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = ('OCCULT_EXPRESSION-MINUS', p[1], p[3])
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = ('OCCULT_EXPRESSION-TERM', p[1])

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = ('OCCULT_EXPRESSION-TIMES', p[1], p[3])

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = ('OCCULT_EXPRESSION-DIVIDE', p[1], p[3])

def p_term_factor(p):
    'term : factor'
    p[0] = ('OCCULT_TERM-FACTOR', p[1])

def p_factor_int(p):
    'factor : INT'
    p[0] = ('OCCULT_FACTOR-INT', p[1])

def p_factor_float(p):
    'factor : FLOAT'
    p[0] = ('OCCULT_FACTOR-FLOAT', p[1])

def p_factor_variable(p):
    'factor : NAME'
    p[0] = ('OCCULT_FACTOR-VARIABLE', p[1])

def p_factor_array_variable(p):
    'factor : NAME LSQUARE INT RSQUARE'
    p[0] = ('OCCULT_FACTOR-ARRAY-VARIABLE', p[1], p[3])

def p_factor_string(p):
    'factor : STRING'
    p[0] = ('OCCULT_FACTOR-STRING', p[1])

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = ('OCCULT_FACTOR-EXPR', p[2])    

def p_error(p):
    if p:
        print("Error syntaxis 💀")
        sys.exit(3)

parser = y.yacc()
