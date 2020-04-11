import ply.yacc as yacc
import ply.lex as lex
import Visitor as vis
from ExpressionLanguageLex import *
import SintaxeAbstrata as sa

precedence = (
     ('left', 'PLUS', 'MINUS'),
     ('left', 'TIMES', 'DIVIDE'),
 )

def p_main(p):
  '''
  main : BEGIN_PROGRAM main_INNER END_PROGRAM 
  | BEGIN_PROGRAM END_PROGRAM
  '''
  if len(p) == 4:
    p[0] = sa.Main_MainInner(p[2])
    print(p[2])

def p_inner_statement(p):
  '''
  inner_statement : function_declaration_statement
    | statement
  '''
  if isinstance(p[1], sa.Statement):
    p[0] = sa.InnerStatement_Statement(p[1])

def p_statement(p):
  '''
  statement : expr SEMICOLON
    | if_statement
    | while_statement
    | do_statement
    | for_statement
    | break_statement
    | continue_statement
    | return_statement
    | GLOBAL global_var statement_COLON_GLOBAL SEMICOLON
    | GLOBAL global_var SEMICOLON
  '''
  if isinstance(p[1], sa.Expr):
    p[0] = sa.Statement_Expr(p[1], p[2])
    
def p_if_statement(p):
  '''
  if_statement : statement_if if_statement_complement
    | statement_if
  '''
  
def p_if_statement_complement(p):
  '''
  if_statement_complement : statement_elseif
    | statement_elseif statement_else
    | statement_else
  '''
    
def p_while_statement(p):
  '''
  while_statement : WHILE expr_parentheses statement_BLOCK_OPT
  '''

def p_do_statement(p):
  '''
  do_statement : DO statement_BLOCK_OPT WHILE expr_parentheses SEMICOLON
  '''

def p_break_statement(p):
  '''
  break_statement : BREAK expr SEMICOLON
    | BREAK SEMICOLON
  '''

def p_continue_statement(p):
  '''
  continue_statement : CONTINUE expr SEMICOLON
    | CONTINUE SEMICOLON
  '''
  
def p_return_statement(p):
  '''
  return_statement : RETURN expr SEMICOLON 
    | RETURN SEMICOLON
  '''
  
def p_for_statement(p):
  '''
  for_statement : FOR LPAREN for_parameters RPAREN statement_BLOCK_OPT
  '''
  
def p_for_parameters(p):
  '''
  for_parameters : SEMICOLON SEMICOLON 
  | for_expr_OPT SEMICOLON SEMICOLON
  | for_expr_OPT SEMICOLON for_expr_OPT SEMICOLON 
  | for_expr_OPT SEMICOLON SEMICOLON for_expr_OPT
  | SEMICOLON for_expr_OPT SEMICOLON
  | SEMICOLON for_expr_OPT SEMICOLON for_expr_OPT
  | SEMICOLON SEMICOLON for_expr_OPT
  | for_expr_OPT SEMICOLON for_expr_OPT SEMICOLON for_expr_OPT
  '''
  
def p_global_var(p):
  '''
  global_var : VARIABLE
    | DOLAR VARIABLE
    | DOLAR LKEY expr RKEY 
  '''

def p_statement_COLON_GLOBAL(p):
  '''
  statement_COLON_GLOBAL : COLON global_var statement_COLON_GLOBAL
    | COLON global_var
  '''
  
def p_ampersand_variable(p):
  '''
  ampersand_variable : AMPERSAND VARIABLE
    | VARIABLE
  '''
  
def p_expr_parentheses(p):
  '''
  expr_parentheses : LPAREN expr RPAREN
  '''

def p_statement_if(p):
  '''
  statement_if : IF expr_parentheses statement_BLOCK_OPT
  '''

def p_statement_elseif(p):
  '''
  statement_elseif : ELSEIF expr_parentheses statement_BLOCK_OPT
  '''

def p_statement_else(p):
  '''
  statement_else : ELSE statement_BLOCK_OPT
  '''

def p_statement_foreach(p):
  '''
  statement_foreach : FOREACH LPAREN expr AS ampersand_variable RPAREN statement_BLOCK_OPT
  | FOREACH LPAREN expr AS ampersand_variable ATTR_ASSOC ampersand_variable RPAREN statement_BLOCK_OPT
  '''

def p_for_expr_OPT(p):
  '''
  for_expr_OPT : expr for_expr_COLON_EXPR
   | expr
  '''
  
def p_function_call(p):
  '''
  function_call : ID LPAREN function_call_parameter_list RPAREN
    | base_variable
  '''

def p_function_call_parameter_list(p):
  '''
  function_call_parameter_list : function_call_parameter function_call_list_COLON_FUNCTION
  | 
  '''

def p_function_call_parameter(p):
  '''
  function_call_parameter : variable
    | AMPERSAND VARIABLE
  '''

def p_assignment_list_element(p):
  '''
  assignment_list_element : variable
    | LIST LPAREN assignment_list_element assignment_list_element_COLON_ASSIGNMENT  RPAREN
  '''
  
  
def p_unary_operator(p):
  '''
  unary_operator : EXC_DOT
    | PLUS
    | MINUS
  '''
  
def p_type_cast_operator(p):
  '''
    type_cast_operator : INT_TYPE
      | DOUBLE_TYPE
      | FLOAT_TYPE
      | REAL_TYPE
      | STRING_TYPE
      | ARRAY_TYPE
      | BOOLEAN_TYPE
      | BOOL_TYPE
      | UNSET
  '''

# Removida no momento
def p_arithmetic_expr(p):
  '''
  arithmetic_expr : arithmetic_expr PLUS arithmetic_expr               
    | arithmetic_expr MINUS arithmetic_expr               
    | arithmetic_expr TIMES arithmetic_expr               
    | arithmetic_expr DIVIDE arithmetic_expr              
    | LPAREN arithmetic_expr RPAREN                   
    | NUMBER_INTEGER 
    | NUMBER_REAL                                    
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
  
def p_arithmetic_operator(p):
  '''
  arithmetic_operator : PLUS
    | DIVIDE
    | PERCENT
    | TIMES
    | MINUS
  '''

def p_comparission_operator(p): 
  '''
  comparission_operator : EQUALS
    | GREAT_THAN
    | LESS_THAN
    | LESS_EQUAL
    | GREAT_EQUAL
    | NOT_EQUAL
    | LEFT_LOGICAL
    | RIGHT_LOGICAL
  '''

def p_expr(p): 
  ''' 
  expr : INCREMENT variable
    | variable INCREMENT
    | DECREMENT variable
    | variable DECREMENT
    | variable LBRACKET expr RBRACKET
    | LPAREN expr RPAREN
    | unary_operator expr
    | expr INTE_DOT expr DDOT expr
    | expr comparission_operator expr
    | variable assign_operator expr
    | variable assign_operator AMPERSAND expr
    | expr arithmetic_operator expr
    | LPAREN type_cast_operator RPAREN expr
    | EXIT expr_EXIT
    | DIE expr_EXIT
    | ARRAY_TYPE LPAREN array_pair_list RPAREN
    | ARRAY_TYPE LPAREN RPAREN
    | variable
    | function_call
    | NUMBER_REAL
    | NUMBER_INTEGER
    | CONSTANT_ENCAPSED_STRING
    | TRUE
    | FALSE
  '''
  if p[1] == 'true':
    p[0] = sa.Expr_True(p[1])
  
#Não identificado para que serve
def p_encaps(p):
  '''
  encaps : encaps_var
    | VARIABLE
    | LPAREN
    | RPAREN
    | LKEY
    | RKEY
  '''

def p_encaps_var(p):
  '''
  encaps_var : VARIABLE encaps_var_OPT
    | DOLAR LBRACKET expr RBRACKET
    | DOLAR  LKEY ID LBRACKET expr RBRACKET RKEY
    | LKEY variable RKEY
  '''

def p_encaps_var_OPT(p):
  '''
  encaps_var_OPT : LBRACKET encaps_var_offset RBRACKET
    | 
  '''

def p_encaps_var_offset(p):
  '''
  encaps_var_offset : STRING 
    | VARIABLE
  '''

def p_expr_EXIT(p):
  '''
  expr_EXIT : exit_expr
    | 
  '''

def p_exit_expr(p):
  '''
  exit_expr : LPAREN expr RPAREN
    | LPAREN RPAREN
  '''

# Removido chamada a function_call
def p_variable(p):
  '''
  variable : base_variable
  '''
  
def p_base_variable(p):
  '''
  base_variable : reference_variable
    | simple_indirect_reference_DOLAR reference_variable
  '''
  
def p_reference_variable(p):
  '''
  reference_variable : compound_variable reference_variable_SELECTOR
    | compound_variable
  '''
  
def p_compound_variable(p):
  '''
  compound_variable : VARIABLE 
    | DOLAR LKEY expr RKEY 
  '''

#Utilizado para indexação
def p_selector(p):
  '''
  selector : LBRACKET expr RBRACKET 
    | LBRACKET RBRACKET
  '''

def p_function_declaration_statement(p):
  '''
  function_declaration_statement : FUNCTION ID LPAREN RPAREN LKEY RKEY
    | FUNCTION AMPERSAND ID LPAREN RPAREN LKEY RKEY
    | FUNCTION AMPERSAND ID LPAREN parameter_list RPAREN LKEY RKEY
    | FUNCTION AMPERSAND ID LPAREN RPAREN LKEY inner_statement_MUL RKEY
    | FUNCTION AMPERSAND ID LPAREN parameter_list RPAREN LKEY inner_statement_MUL RKEY
    | FUNCTION ID LPAREN parameter_list RPAREN LKEY RKEY
    | FUNCTION ID LPAREN RPAREN LKEY inner_statement_MUL RKEY
    | FUNCTION ID LPAREN parameter_list RPAREN LKEY inner_statement_MUL RKEY
  '''

def p_parameter_list(p):  
  '''
  parameter_list : parameter parameter_list_COLON_PARAMETER 
    | parameter
  '''  

def p_parameter(p):
  ''' 
  parameter : VARIABLE
    | VARIABLE ASSIGN static_scalar
    | parameter_type VARIABLE
    | parameter_type AMPERSAND VARIABLE
    | AMPERSAND VARIABLE
    | AMPERSAND VARIABLE ASSIGN static_scalar
    | parameter_type AMPERSAND VARIABLE ASSIGN static_scalar
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
  
def p_array_pair_list(p):
  '''
  array_pair_list : array_pair array_pair_list_ARR_PAIR 
    | array_pair
  '''

def p_array_pair(p):
  ''' 
  array_pair : expr
    | expr ATTR_ASSOC expr
    | expr ATTR_ASSOC AMPERSAND variable
    | AMPERSAND variable
  '''

# Expressões regulares transformadas em regras.
# ======================================================================

def p_main_INNER(p):
  '''
  main_INNER : inner_statement main_INNER
    | inner_statement
  '''
  if len(p) == 3:
    p[0] = sa.MainInner_InnerStatement(p[1], p[2])

def p_inner_statement_MUL(p):
  '''
  inner_statement_MUL : inner_statement inner_statement_MUL
    | inner_statement
  '''
  
def p_statement_MUL(p):
  '''
  statement_MUL : statement statement_MUL
    | statement
  '''
  
def p_for_expr_COLON_EXPR(p):
  '''
  for_expr_COLON_EXPR : COLON expr for_expr_COLON_EXPR
    | COLON expr
  '''
  
def p_statement_BLOCK_OPT(p):
  '''
  statement_BLOCK_OPT : statement 
    | LKEY statement_MUL RKEY 
    | LKEY RKEY
  ''' 

def p_function_call_list_COLON_FUNCTION(p):
  '''
  function_call_list_COLON_FUNCTION : COLON function_call_parameter function_call_list_COLON_FUNCTION
    | 
  '''
  
def p_assignment_list_element_COLON_ASSIGNMENT(p):
  '''
  assignment_list_element_COLON_ASSIGNMENT : COLON assignment_list_element assignment_list_element_COLON_ASSIGNMENT
    | 
  '''
  
def p_parameter_list_COLON_PARAMETER(p):
  '''
  parameter_list_COLON_PARAMETER : COLON parameter parameter_list_COLON_PARAMETER
    | COLON parameter
  '''
  
def p_reference_variable_SELECTOR(p):
  '''
  reference_variable_SELECTOR : selector reference_variable_SELECTOR
    | selector
  '''
  
def p_simple_indirect_reference_DOLAR(p):
  '''
  simple_indirect_reference_DOLAR : DOLAR simple_indirect_reference_DOLAR
    | DOLAR
  '''

def p_array_pair_list_ARR_PAIR(p):
  '''
  array_pair_list_ARR_PAIR : COLON array_pair array_pair_list_ARR_PAIR
    | COLON array_pair
  '''

def p_error(p):
    print(p)
    print("Syntax error in input!")
 

lex.lex()
arquivo = '''
<?php
  while ($valor[0][1] < 150){
    $valor;
  }
?>'''

lex.input(arquivo)
parser = yacc.yacc()
result = parser.parse(debug=True)
#v = vis.Visitor()
#result.accept(v)