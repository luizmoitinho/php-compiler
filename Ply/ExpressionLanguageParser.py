import ply.yacc as yacc
import ply.lex as lex
from ExpressionLanguageLex import *

def p_main(p):
  '''
  main : BEGIN_PROGRAM main_INNER END_PROGRAM 
  '''
  
def p_main_INNER(p):
  '''
  main_INNER : inner_statement main_INNER
    | 
  '''

def p_inner_statement(p):
  '''
  inner_statement : function_declaration_statement 
    | 
  '''

def p_AMPERSAND_OPT(p):
  '''
  AMPERSAND_OPT : AMPERSAND
    | 
  '''



def p_function_declaration_statement(p):
  '''
  function_declaration_statement : FUNCTION AMPERSAND_OPT ID LPAREN parameter_list RPAREN LKEY inner_statement  RKEY
  '''
# Essa regra não deve existir, pois não é permitido vazio entre as chaves de uma função. Não pela regra.
def p_INNER_STATEMENT_OPT(p):
  '''
  INNER_STATEMENT_OPT : inner_statement 
    |  
  '''

def p_parameter_list(p):  
  '''
  parameter_list : parameter parameter_list_COLON_PARAMETER 
  '''  

def p_parameter_list_COLON_PARAMETER(p):
  '''
  parameter_list_COLON_PARAMETER : COLON parameter parameter_list_COLON_PARAMETER
    | 
  '''

def p_parameter(p):
  ''' 
  parameter : parameter_type AMPERSAND_OPT VARIABLE parameter_ASSIGN_STATIC_OPT
  '''

def p_parameter_type(p):
  '''
  parameter_type : INT_TYPE
    | BOOLEAN_TYPE
    | STRING_TYPE
    | FLOAT_TYPE
    | ARRAY_TYPE 
    | BOOL_TYPE
    | REAL_TYPE
    | DOUBLE_TYPE
    | 
  '''

def p_parameter_ASSIGN_STATIC_OPT(p):
  '''
  parameter_ASSIGN_STATIC_OPT : ASSIGN static_scalar
    |
  '''

def p_static_scalar(p):
  '''
  static_scalar : common_scalar
    | PLUS static_scalar
    | MINUS static_scalar
    
  '''

def p_common_scalar(p): 
  '''
  common_scalar : NUMBER_REAL
    | NUMBER_INTEGER
    | CONSTANT_ENCAPSED_STRING
  '''

def p_static_scalar_OPT(p): 
  '''
  static_scalar_OPT : static_array_pair_list
    | 
  '''

def p_static_array_pair_list(p):
  '''
  static_array_pair_list : static_array_pair static_array_pair_list_COLON_STATIC static_array_pair_list_COLON 
  '''
  
def p_static_array_pair_list_COLON_STATIC(p):
  '''
  static_array_pair_list_COLON_STATIC : COLON static_array_pair static_array_pair_list_COLON_STATIC
    | 
  '''

def p_static_array_pair_list_COLON(p): 
  '''
  static_array_pair_list_COLON : COLON
    | 
  '''

def p_static_array_pair(p):
  ''' 
  static_array_pair : static_scalar static_array_pair_ATTR_STATIC
  '''
  
def p_static_array_pair_ATTR_STATIC(p):
  '''
  static_array_pair_ATTR_STATIC : ATTR_ASSOC static_scalar
    | 
  '''


def p_error(p):
    print(p)
    print("Syntax error in input!")
  
lex.lex()
arquivo = '''<?php function ola1(&$param1 = "Luiz") {

} ?>'''
lex.input(arquivo)

parser = yacc.yacc()
result = parser.parse(debug=True)
#v = Visitor()
#result.accept(v)