# -------------------------
# ExpressionLanguageParser.py
#--------------------------

import ply.yacc as yacc
import ply.lex as lex
from ExpressionLanguageLex import tokens 

def p_main(p):
  '''
  main : BEGIN_PROGRAM inner_statement END_PROGRAM
  '''

def p_inner_statement(p):
  '''
  inner_statement : statement
    | function_declaration_statement
  '''

def p_statement(p):
  '''
  statement : LKEY inner_statement* RKEY
      | IF LPAREN expr RPAREN statement elseif_branch? else_single? new_else_single? ENDIF SEMICOLON
      | WHILE LPAREN expr RPAREN while_statement
      | DO statement WHILE LPAREN expr RPAREN SEMICOLON
      | FOR LPAREN for_expr SEMICOLON for_expr SEMICOLON for_expr RPAREN for_statement
      | BREAK expr? SEMICOLON
      | CONTINUE expr? SEMICOLON
      | RETURN expr_without_variable SEMICOLON
      | RETURN variable? SEMICOLON
      | GLOBAL global_var LPAREN COLON global_var RPAREN* SEMICOLON
      | expr SEMICOLON
      | FOREACH LPAREN variable AS foreach_variable (ATTR_ASSOC foreach_variable)? RPAREN foreach_statement
      | FOREACH LPAREN expr_without_variable AS foreach_variable (ATTR_ASSOC foreach_variable)? RPAREN foreach_statement foreach_statement
      | SEMICOLON 
  '''
  
def p_function_declaration_statement(p):
  '''
  function_declaration_statement : FUNCTION AMPERSAND? STRING LPAREN parameter_list RPAREN LKEY inner_statement* RKEY 
  '''
  
def p_foreach_variable(p):
  '''
  foreach_variable : AMPERSAND? variable
  '''
  
def p_for_statement(p):
  '''
  for_statement : statement 
    | DDOT inner_statement* ENDFOR SEMICOLON
  '''

def p_foreach_statement(p):
  '''
  foreach_statement : statement
    | DDOT inner_statement ENDFOREACH SEMICOLON
  '''
  
def p_declare_statement(p):
  '''
  declare_statement : statement
    | DDOT inner_statement ENDDECLARE SEMICOLON
  '''

def p_declare_list(p):
  '''
  declare_list : STRING ASSIGN static_scalar (COLON STRING ASSIGN static_scalar)*
  '''


def p_while_stament(p):
  '''
  while_statement : statement
    | DDOT inner_statement* ENDWHILE SEMICOLON 
  '''

def p_elseif_branch(p):
  '''
  elseif_branch : ELSEIF LPAREN expr RPAREN statement 
  '''

def p_new_elseif_branch(p):
  '''
  new_elseif_branch : ELSEIF LPAREN expr RPAREN DDOT inner_statement* 
  '''

def p_else_single(p):
  '''
  else_single : ELSE statement 
  '''

def p_new_else_single(p):
  '''
  new_else_single : ELSE DDOT inner_statement* 
  '''

def p_parameter_list(p):  
  '''
  parameter_list : parameter (COLON parameter)* 
  '''  

def p_parameter(p):
  ''' 
  parameter : STRING AMPERSAND? VARIABLE (ASSIGN static_scalar)? 
    | ARRAY AMPERSAND? VARIABLE (ASSIGN static_scalar)? 
  '''

def p_function_call_list(p):
  '''
  function_call_parameter_list : function_call_parameter (COLON function_call_parameter)* 
  '''

def p_function_call_parameter(p):
  '''
  function_call_parameter : expr_without_variable
      | variable
      | AMPERSAND VARIABLE
  '''
  
def p_global_var(p):
  '''
  global_var : VARIABLE
    | DOLAR VARIABLE
    | DOLAR LKEY expr RKEY 
  '''

def p_variable_modifiers(p):
  '''
  variable_modifiers : "var" 
    | modifier (modifier)*
  ''' 

def p_for_expr(p):
  '''
  for_expr : expr (COLON expr)* 
  '''

def p_expr_without_variable(p):
    '''
    expr_without_variable : LIST LPAREN assignment_list_element (COLON assignment_list_element)* RPAREN ASSIGN expr
      | variable ASSIGN expr
      | variable ASSIGN AMPERSAND variable
      | CLONE expr
      | VARIABLE INCREMENT
      | INCREMENT VARIABLE
      | VARIABLE DECREMENT
      | DECREMENT VARIABLE
      | LPAREN expr RPAREN
      | expr INTE_DOT expr DDOT expr
      | internal_functions
      | LPAREN INT_TYPE RPAREN expr
      | LPAREN DOUBLE_TYPE RPAREN expr
      | LPAREN FLOAT_TYPE RPAREN expr
      | LPAREN REAL_TYPE RPAREN expr
      | LPAREN STRING_TYPE RPAREN expr
      | LPAREN ARRAY_TYPE RPAREN expr
      | LPAREN OBJECT_TYPE RPAREN expr
      | LPAREN BOOL_TYPE RPAREN expr
      | LPAREN BOOLEAN_TYPE RPAREN expr
      | LPAREN UNSET RPAREN expr
      | EXIT exit_expr?
      | DIE exit_expr?
      | ARROBA expr
      | scalar
      | ARRAY LPAREN array_pair_list? RPAREN
      | CRASE encaps* CRASE
    '''

def p_function_call(p):
  '''
  function_call : STRING LPAREN function_call_parameter_list RPAREN 
    | variable_without_objects LPAREN function_call_parameter_list RPAREN 
  '''
  
def p_exit_expr(p):
  '''
  exit_expr : LPAREN expr? RPAREN   
  '''

def p_static_scalar(p):
  '''
  static_scalar : common_scalar
    | STRING
    | PLUS static_scalar
    | MINUS static_scalar
    | ARRAY LPAREN static_array_pair_list? RPAREN 
  '''

#FINALIZAR REGRA ----------------------------------------------
def p_common_scalar(p): 
  '''
  common_scalar : NUMBER_REAL
    | NUMBER_INTEGER
    | 
  '''

def p_scalar(p):
  '''
  scalar : STRING
      | STRING_VARNAME
      | common_scalar
      | ASPAS encaps* ASPAS
      | APOSTROFE encaps* APOSTROFE;
  '''
    
def p_assignment_list_element(p):
  '''
  assignment_list_element : variable
    | LIST LPAREN assignment_list_element (COLON assignment_list_element)* RPAREN
  '''
    
def static_array_pair_list(p):
  '''
  static_array_pair_list : static_array_pair (COLON static_array_pair)* COLON? 
  '''

def static_array_pair(p):
  ''' 
  static_array_pair : static_scalar (ATTR_ASSOC static_scalar)? 
  '''

def p_expr(p): 
  ''' 
  expr : VARIABLE 
    | expr_without_variable
  '''  

#Ver essa regra, talvez esteja errada.
def p_variable(p):
  '''
    variable : base_variable_with_function_calls ( method_parameters (method_parameters) * )? 
  '''

def p_method_parameters(p):
  '''
  method_parameters : LPAREN function_call_parameter_list RPAREN 
  '''


def p_base_variable_with_function_calls(p):
  '''
    base_variable_with_function_calls : base_variable 
      | function_call 
  '''

def p_base_variable(p):
  '''
    base_variable : reference_variable
    | simple_indirect_reference reference_variable
  '''

def p_reference_variable(p):
  '''
    reference_variable : compound_variable (selector)* 
  '''

def p_compound_variable(p):
  '''
  compound_variable : VARIABLE 
    | DOLAR LKEY expr RKEY 
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
    
def p_simple_indirect_reference(p):
  '''
  simple_indirect_reference : simple_indirect_reference_DOLAR
  '''
  
#Tentando resolver o problemas das ERs
def p_simple_indirect_reference_DOLAR(p):
  '''
  simple_indirect_reference : DOLAR simple_indirect_reference_DOLAR
    | 
  '''
  
def p_array_pair_list(p):
  '''
  array_pair_list : array_pair array_pair_list_ARR_PAIR array_pair_list_COLON
  '''

#Tentando resolver o problemas das ERs
def p_array_pair_list_ARR_PAIR(p):
  '''
  array_pair_list_ARR_PAIR : COLON array_pair array_pair_list_ARR_PAIR
    | 
  '''
  
#Tentando resolver o problemas das ERs
def p_array_pair_list_COLON(p):
  '''
  p_array_pair_list_COLON : COLON
    | 
  '''

def p_array_pair(p):
  ''' 
  array_pair : AMPERSAND VARIABLE
    | expr ATTR_ASSOC AMPERSAND VARIABLE
    | expr ATTR_ASSOC expr 
  '''

def p_encaps(p):
  '''
  encaps : encaps_var
    | STRING
    | LPAREN
    | RPAREN
    | LKEY
    | RKEY
  '''

def p_encaps_var(p):
  '''
  encaps_var : VARIABLE encaps_var_1
    | DOLAR LBRACKET expr RBRACKET
    | DOLAR  LKEY STRING_VARNAME LBRACKET expr RBRACKET RKEY
    | CURLY_OPEN variable  
  '''

#Tentando resolver o problema das ERs
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
  
parser = yacc.yacc()
result = parser.parse(debug=True)
#v = Visitor()
#result.accept(v)