def p_main_INNER(p):
  '''
  main_INNER : inner_statement main_INNER
    | 
  '''

def p_statement_MUL(p):
  '''
  statement_MUL : statement statement_MUL
    | 
  '''

def p_inner_statement_MUL(p):
  '''
  inner_statement_MUL : inner_statement inner_statement_MUL
    |
  '''
  
def p_for_expr_COLON_EXPR(p):
  '''
  for_expr_COLON_EXPR : COLON expr for_expr_COLON_EXPR
    | 
  '''
  
def p_statement_BLOCK_OPT(p):
  '''
  statement_BLOCK_OPT : statement 
    | LKEY statement_MUL RKEY 
  ''' 
  
def p_AMPERSAND_OPT(p):
  '''
  AMPERSAND_OPT : AMPERSAND
    | 
  '''
  
def p_statement_attr_variable_OPT(p):
  '''
  statement_attr_variable_OPT : ATTR_ASSOC ampersand_variable 
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
  
def p_assignment_list_element_COLON_ASSIGNMENT(p):
  '''
  assignment_list_element_COLON_ASSIGNMENT : COLON assignment_list_element assignment_list_element_COLON_ASSIGNMENT
    | 
  '''
  
def p_expr_OPT(p):
  '''
  expr_OPT : expr 
    | 
  '''
  
def p_expr_without_variable_ENCAPS(p):
  '''
  expr_without_variable_ENCAPS : encaps expr_without_variable_ENCAPS
    |
  '''
  
def p_parameter_list_COLON_PARAMETER(p):
  '''
  parameter_list_COLON_PARAMETER : COLON parameter parameter_list_COLON_PARAMETER
    | 
  '''
  
def p_parameter_ASSIGN_STATIC_OPT(p):
  '''
  parameter_ASSIGN_STATIC_OPT : ASSIGN static_scalar
    |
  '''
  
def p_reference_variable_SELECTOR(p):
  '''
  reference_variable_SELECTOR : selector reference_variable_SELECTOR
    | 
  '''
  
def p_simple_indirect_reference_DOLAR(p):
  '''
  simple_indirect_reference_DOLAR : DOLAR simple_indirect_reference_DOLAR
    | 
  '''
  
def p_selector_EXPR(p):
  '''
  selector_EXPR : expr
    |
  '''
  
def p_static_scalar_OPT(p): 
  '''
  static_scalar_OPT : static_array_pair_list
    | 
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
  
def p_static_array_pair_ATTR_STATIC(p):
  '''
  static_array_pair_ATTR_STATIC : ATTR_ASSOC static_scalar
    | 
  '''
  
def p_array_pair_list_ARR_PAIR(p):
  '''
  array_pair_list_ARR_PAIR : COLON array_pair array_pair_list_ARR_PAIR
    | 
  '''
  
def p_array_pair_ATTR_EXPR_OPT(p):
  '''
  array_pair_ATTR_EXPR_OPT : ATTR_ASSOC expr 
    |
  '''
  
def p_array_pair_EXPR_ATTR_OPT(p):
  '''
  array_pair_EXPR_ATTR_OPT : expr ATTR_ASSOC
    |
  '''
