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
    | statement
  '''

def p_statement(p):
  '''
  statement : expr SEMICOLON
    | IF LPAREN expr RPAREN statement
    | SEMICOLON
  '''

  
def p_statement_ELSEIF(p):
  '''
  statement_ELSEIF : elseif_branch
    | 
  '''

def p_statement_ELSE_SINGLE(p):
  '''
  statement_ELSE_SINGLE : else_single
    | 
  '''

def p_elseif_branch(p):
  '''
  elseif_branch : ELSEIF LPAREN expr RPAREN statement 
  '''

def p_statement_NEW_ELSE_SINGLE(p):
  '''
  statement_NEW_ELSE_SINGLE : new_else_single
    | 
  '''

def p_new_else_single(p):
  '''
  new_else_single : ELSE DDOT INNER_STATEMENT_MUL
  '''

def p_else_single(p):
  '''
  else_single : ELSE statement 
  '''

def p_new_elseif_branch(p):
  '''
  new_elseif_branch : ELSEIF LPAREN expr RPAREN DDOT INNER_STATEMENT_MUL
  '''
  
def p_AMPERSAND_OPT(p):
  '''
  AMPERSAND_OPT : AMPERSAND
    | 
  '''

def p_INNER_STATEMENT_MUL(p):
  '''
  INNER_STATEMENT_MUL : inner_statement INNER_STATEMENT_MUL
    |
  '''
  

#  | variable_without_objects LPAREN function_call_parameter_list RPAREN 
def p_function_call(p):
  '''
  function_call : ID LPAREN function_call_parameter_list RPAREN SEMICOLON
    | base_variable
  '''


def p_function_call_parameter_list(p):
  '''
  function_call_parameter_list : function_call_parameter function_call_list_COLON_FUNCTION
  | 
  '''

def p_function_call_list_COLON_FUNCTION(p):
  '''
  function_call_list_COLON_FUNCTION : COLON function_call_parameter function_call_list_COLON_FUNCTION
    | 
  '''

def p_expr_without_variable_COLON_ASSIGNMENT(p):
  '''
  expr_without_variable_COLON_ASSIGNMENT : COLON assignment_list_element expr_without_variable_COLON_ASSIGNMENT
    | 
  '''

def p_function_call_parameter(p):
  '''
  function_call_parameter : VARIABLE
    | AMPERSAND VARIABLE
  '''

def p_assignment_list_element(p):
  '''
  assignment_list_element : variable
    | LIST LPAREN assignment_list_element assignment_list_element_COLON_ASSIGNMENT  RPAREN
  '''

def p_assignment_list_element_COLON_ASSIGNMENT(p):
  '''
  assignment_list_element_COLON_ASSIGNMENT : COLON assignment_list_element assignment_list_element_COLON_ASSIGNMENT
    | 
  '''

#    | scalar
#    | ARRAY LPAREN expr_without_variable_ARRAY RPAREN
def p_expr_without_variable(p):
  '''
  expr_without_variable : LIST LPAREN assignment_list_element RPAREN ASSIGN expr
    | LPAREN expr RPAREN
    | expr INTE_DOT expr DDOT expr
    | LPAREN INT_TYPE RPAREN expr
    | LPAREN DOUBLE_TYPE RPAREN expr
    | LPAREN FLOAT_TYPE RPAREN expr
    | LPAREN REAL_TYPE RPAREN expr
    | LPAREN STRING_TYPE RPAREN expr
    | LPAREN ARRAY_TYPE RPAREN expr
    | LPAREN BOOLEAN_TYPE RPAREN expr
    | LPAREN UNSET RPAREN expr
    | EXIT expr_without_variable_EXIT
    | DIE expr_without_variable_EXIT
    | ARROBA expr
    | CRASE expr_without_variable_ENCAPS CRASE
  '''

def p_arithmetic_operator(p):
  '''
  arithmetic_operator : PLUS
    | MINUS
    | TIMES
    | DIVIDE
    | PERCENT
  '''

def p_assign_operator(p):
  '''
  assign_operator : ADD_ASSIGN
    | SUB_ASSIGN
    | MOD_ASSIGN
    | PLUS_ASSIGN
    | DIVIDE_ASSIGN
    | ASSIGN
  '''

def p_comparission_operator(p): 
  '''
  comparission_operator : EQUALS
    | GREAT_THAN
    | LESS_THAN
    | LESS_EQUAL
    | GREAT_EQUAL
    | NOT_EQUAL
  '''

def p_expr(p): 
  ''' 
  expr : VARIABLE
    | INCREMENT variable
    | variable INCREMENT
    | DECREMENT variable
    | variable DECREMENT
    | expr comparission_operator expr
    | variable assign_operator expr
    | expr arithmetic_operator expr
    | NUMBER_REAL
    | NUMBER_INTEGER
  '''  


def p_expr_without_variable_ENCAPS(p):
  '''
  expr_without_variable_ENCAPS : encaps expr_without_variable_ENCAPS
    |
  '''
  
def p_encaps(p):
  '''
  encaps : encaps_var
    | ID
    | LPAREN
    | RPAREN
    | LKEY
    | RKEY
  '''

def p_encaps_var(p):
  '''
  encaps_var : VARIABLE encaps_var_1
    | DOLAR LBRACKET expr RBRACKET
    | DOLAR  LKEY ID LBRACKET expr RBRACKET RKEY
    | LKEY variable RKEY
  '''

def p_encaps_var_1(p):
  '''
  encaps_var_1 : LBRACKET encaps_var_offset RBRACKET
    | 
  '''

def p_encaps_var_offset(p):
  '''
  encaps_var_offset : STRING 
    | VARIABLE
  '''


def p_expr_without_variable_EXIT(p):
  '''
  expr_without_variable_EXIT : exit_expr
    | 
  '''

def p_exit_expr(p):
  '''
  exit_expr : LPAREN exit_expr_EXPR RPAREN   
  '''
  
def p_exit_expr_EXPR(p):
  '''
  exit_expr_EXPR : expr
    | 
  '''

def p_variable(p):
  '''
  variable : base_variable
    | function_call
  '''
  
def p_base_variable(p):
  '''
  base_variable : reference_variable
    | simple_indirect_reference reference_variable
  '''
  
def p_reference_variable(p):
  '''
  reference_variable : compound_variable reference_variable_SELECTOR
  '''

def p_reference_variable_SELECTOR(p):
  '''
  reference_variable_SELECTOR : selector reference_variable_SELECTOR
    | 
  '''
  
def p_compound_variable(p):
  '''
  compound_variable : VARIABLE 
    | DOLAR LKEY expr RKEY 
  '''

def p_simple_indirect_reference(p):
  '''
  simple_indirect_reference : simple_indirect_reference_DOLAR
  '''

def p_simple_indirect_reference_DOLAR(p):
  '''
  simple_indirect_reference_DOLAR : DOLAR simple_indirect_reference_DOLAR
    | 
  '''

def p_selector(p):
  '''
  selector : LBRACKET selector_EXPR RBRACKET 
  '''
    
def p_selector_EXPR(p):
  '''
  selector_EXPR : expr
    |
  '''
  
def p_variable_name(p):
  '''
  variable_name : VARIABLE
  '''
    
# Essa regra não deve existir, pois não é permitido vazio entre as chaves de uma função. Não pela regra.
def p_inner_statement_OPT(p):
  '''
  inner_statement_OPT : inner_statement 
    |  
  '''

def p_function_declaration_statement(p):
  '''
  function_declaration_statement : FUNCTION AMPERSAND_OPT ID LPAREN parameter_list RPAREN LKEY inner_statement_OPT RKEY
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
#VERIFICAR SYNTAX
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
arquivo = '''<?php 
  function add($valor1, $valor2) {
    if($valor1 <= $valor++)
      $valor = $valor2 - 10;
  }
  
  function add($valor1, $valor2) {
    if($valor1 <= $valor2 - $valor)
      $valor = $valor2 + $valor - $valor;
  }
?>'''
lex.input(arquivo)

parser = yacc.yacc()
result = parser.parse(debug=True)
#v = Visitor()
#result.accept(v)
