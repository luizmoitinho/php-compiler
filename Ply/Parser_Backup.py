
def p_inner_statement(p):
  '''
  inner_statement : statement
    | function_declaration_statement
  '''
  
def p_statement(p):
  '''
  statement : LKEY INNER_STATEMENT_MUL RKEY
      | IF LPAREN expr RPAREN statement statement_ELSEIF statement_ELSE_SINGLE statement_NEW_ELSE_SINGLE ENDIF SEMICOLON
      | WHILE LPAREN expr RPAREN while_statement
      | DO statement WHILE LPAREN expr RPAREN SEMICOLON
      | FOR LPAREN for_expr SEMICOLON for_expr SEMICOLON for_expr RPAREN for_statement
      | BREAK EXPR_OPT SEMICOLON
      | CONTINUE EXPR_OPT SEMICOLON
      | RETURN expr_without_variable SEMICOLON
      | RETURN VARIABLE_OPT SEMICOLON
      | GLOBAL global_var statement_COLON_GLOBAL SEMICOLON
      | expr SEMICOLON
      | FOREACH LPAREN variable AS foreach_variable statement_ATTR_FOREACH RPAREN foreach_statement
      | FOREACH LPAREN expr_without_variable AS foreach_variable statement_ATTR_FOREACH RPAREN foreach_statement foreach_statement
      | SEMICOLON 
  '''

def p_statement_ATTR_FOREACH(p):
  '''
  statement_ATTR_FOREACH : ATTR_ASSOC foreach_variable 
    |
  '''
  
def p_statement_COLON_GLOBAL(p):
  '''
  statement_COLON_GLOBAL : COLON global_var statement_COLON_GLOBAL
    | 
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
  
def p_statement_NEW_ELSE_SINGLE(p):
  '''
  statement_NEW_ELSE_SINGLE : new_else_single
    | 
  '''
  
def p_VARIABLE_OPT(p):
  '''
  VARIABLE_OPT : variable
    |
  '''
  
def p_EXPR_OPT(p):
  '''
  EXPR_OPT : expr
    | 
  '''
  
def p_INNER_STATEMENT_OPT(p):
  '''
  INNER_STATEMENT_OPT : inner_statement 
    |  
  '''

def p_INNER_STATEMENT_MUL(p):
  '''
  INNER_STATEMENT_MUL : inner_statement INNER_STATEMENT_MUL
    |
  '''
  
def p_function_declaration_statement(p):
  '''
  function_declaration_statement : FUNCTION AMPERSAND_OPT STRING LPAREN parameter_list RPAREN LKEY INNER_STATEMENT_OPT RKEY 
  '''
  
  
def p_foreach_variable(p):
  '''
  foreach_variable : AMPERSAND_OPT variable
  '''
  
def p_for_statement(p):
  '''
  for_statement : statement 
    | DDOT INNER_STATEMENT_MUL ENDFOR SEMICOLON
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
  declare_list : STRING ASSIGN static_scalar declare_list_COLON_STRING_ASSIGN_STATIC
  '''

def p_declare_list_COLON_STRING_ASSIGN_STATIC(p):
  '''
  declare_list_COLON_STRING_ASSIGN_STATIC : COLON STRING ASSIGN static_scalar declare_list_COLON_STRING_ASSIGN_STATIC
    |
  '''

def p_while_statement(p):
  '''
  while_statement : statement
    | DDOT INNER_STATEMENT_MUL ENDWHILE SEMICOLON 
  '''

def p_elseif_branch(p):
  '''
  elseif_branch : ELSEIF LPAREN expr RPAREN statement 
  '''

def p_new_elseif_branch(p):
  '''
  new_elseif_branch : ELSEIF LPAREN expr RPAREN DDOT INNER_STATEMENT_MUL
  '''

def p_else_single(p):
  '''
  else_single : ELSE statement 
  '''

def p_new_else_single(p):
  '''
  new_else_single : ELSE DDOT INNER_STATEMENT_MUL
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
  parameter : STRING AMPERSAND_OPT VARIABLE parameter_ASSIGN_STATIC
    | ARRAY_TYPE AMPERSAND_OPT VARIABLE parameter_ASSIGN_STATIC
  '''
  
def p_parameter_ASSIGN_STATIC(p):
  '''
  parameter_ASSIGN_STATIC : ASSIGN static_scalar
    |
  '''

#essa função será reutilizada, então fiz genérica
def p_AMPERSAND_OPT(p):
  '''
  AMPERSAND_OPT : AMPERSAND 
    | 
  '''

def p_function_call_list(p):
  '''
  function_call_parameter_list : function_call_parameter function_call_list_COLON_FUNCTION
  '''
  
def p_function_call_list_COLON_FUNCTION(p):
  '''
  function_call_list_COLON_FUNCTION : COLON function_call_parameter function_call_list_COLON_FUNCTION
    | 
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
  variable_modifiers : VAR 
    | modifier variable_modifiers_MODIFIER
  ''' 
  
def p_variable_modifiers_MODIFIER(p):
  '''
  variable_modifiers_MODIFIER : modifier variable_modifiers_MODIFIER
    | 
  '''

def p_for_expr(p):
  '''
  for_expr : expr for_expr_COLON_EXPR 
  '''
  
def p_for_expr_COLON_EXPR(p):
  '''
  for_expr : COLON expr for_expr_COLON_EXPR
    | 
  '''

def p_expr_without_variable(p):
  '''
  expr_without_variable : LIST LPAREN assignment_list_element expr_without_variable_COLON_ASSIGNMENT RPAREN ASSIGN expr
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
    | EXIT expr_without_variable_EXIT
    | DIE expr_without_variable_EXIT
    | ARROBA expr
    | scalar
    | ARRAY LPAREN expr_without_variable_ARRAY RPAREN
    | CRASE expr_without_variable_ENCAPS CRASE
  '''

def p_expr_without_variable_COLON_ASSIGNMENT(p):
  '''
  expr_without_variable_COLON_ASSIGNMENT : COLON assignment_list_element expr_without_variable_COLON_ASSIGNMENT
    | 
  '''
  
def p_expr_without_variable_EXIT(p):
  '''
  expr_without_variable_EXIT : exit_expr
    | 
  '''
  
def p_expr_without_variable_ARRAY(p):
  '''
  expr_without_variable_ARRAY : array_pair_list
    | 
  '''
  
def p_expr_without_variable_ENCAPS(p):
  '''
  expr_without_variable_ENCAPS : encaps expr_without_variable_ENCAPS
    |
  '''

def p_function_call(p):
  '''
  function_call : STRING LPAREN function_call_parameter_list RPAREN 
    | variable_without_objects LPAREN function_call_parameter_list RPAREN 
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


def p_static_scalar(p):
  '''
  static_scalar : common_scalar
    | STRING
    | PLUS static_scalar
    | MINUS static_scalar
    | ARRAY LPAREN static_scalar_OPT RPAREN 
  '''
  
def p_static_scalar_OPT(p): 
  '''
  static_scalar_OPT : static_array_pair_list
    | 
  '''

def p_common_scalar(p): 
  '''
  common_scalar : NUMBER_REAL
    | NUMBER_INTEGER
    | S
  '''

def p_scalar(p):
  '''
  scalar : STRING
    | STRING_VARNAME
    | common_scalar
    | ASPAS scalar_ENCAPS ASPAS
    | APOSTROFE scalar_ENCAPS APOSTROFE
  '''
  
def p_scalar_ENCAPS(p):
  '''
  scalar_ENCAPS : encaps scalar_ENCAPS
    | 
  '''
    
def p_assignment_list_element(p):
  '''
  assignment_list_element : variable
    | LIST LPAREN assignment_list_element assignment_list_element_COLLON_ASSIGNMENT  RPAREN
  '''

def p_assignment_list_element_COLON_ASSIGNMENT(p):
  '''
  assignment_list_element_COLON_ASSIGNMENT : COLON assignment_list_element assignment_list_element_COLON_ASSIGNMENT
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

def static_array_pair_list_COLON(p): 
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

def p_expr(p): 
  ''' 
  expr : VARIABLE 
    | expr_without_variable
  '''  

#Ver essa regra, talvez esteja errada. UPDATE: removido do final ->  (method_parameters (method_parameters)*)? 
def p_variable(p):
  '''
    variable : base_variable_with_function_calls 
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
