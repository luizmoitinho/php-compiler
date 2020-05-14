import ply.yacc as yacc
import ply.lex as lex
import SemanticVisitor as sv
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
  else:
    p[0] = sa.Main_MainInner_Empty()
    
def p_main_INNER(p):
  '''
  main_INNER : inner_statement main_INNER
    | inner_statement
  '''
  if len(p) == 3:
    p[0] = sa.MainInner_InnerStatement_MainInner(p[1], p[2])
  else:
    p[0] = sa.MainInner_InnerStatement(p[1])

def p_inner_statement(p):
  '''
  inner_statement : function_declaration_statement
    | statement
  ''' 
  if isinstance(p[1], sa.FuncDecStatement):
    p[0] = sa.InnerStatement_FuncDecStatement(p[1])
  elif isinstance(p[1], sa.Statement):
    p[0] = sa.InnerStatement_Statement(p[1])
    
def p_inner_statement_MUL(p):
  '''
  inner_statement_MUL : inner_statement inner_statement_MUL
    | inner_statement
  '''
  if len(p) == 3:
    p[0] = sa.InnerStatementMul_Mul(p[1], p[2])
  else:
    p[0] = sa.InnerStatementMul_Single(p[1])
  
def p_expr(p):
  '''
  expr : MINUS expr1 expr2
    | expr1 expr2
    | expr3 
    | MINUS expr1
    | expr1
  '''
  if isinstance(p[1], sa.Expr1) and len(p) == 3:
    p[0] = sa.Expr_Expr1_Expr2(p[1], p[2])
  elif isinstance(p[1], sa.Expr1) and len(p) == 2:
    p[0] = sa.Expr_Expr1(p[1])
  elif isinstance(p[1], sa.Expr3) and len(p) == 2:
    p[0] = sa.Expr_Expr3(p[1])
  elif p[1] == '-' and len(p) == 3:
    p[0] = sa.Expr_Minus_Expr1(p[2])
  else: 
    p[0] = sa.Expr_Minus_Expr1_Expr2(p[2], p[3])
    
def p_expr2(p): 
  '''
  expr2 : INTE_DOT expr DDOT expr 
    | comparission_operator expr 
    | arithmetic_operator expr
  '''
  if isinstance(p[1], sa.ArithmeticOperator):
    p[0] = sa.Expr2_ArithmeticOp(p[1], p[2])
  elif isinstance(p[1], sa.ComparissionOperator):
    p[0] = sa.Expr2_ComparissionOp(p[1], p[2])
  else:
    p[0] = sa.Expr2_TernaryExpr(p[2], p[4])
  
def p_expr3(p):
  '''
  expr3 : variable assign_operator expr
    | variable assign_operator AMPERSAND expr
    | LPAREN type_cast_operator RPAREN expr
  '''
  if isinstance(p[2], sa.TypeCastOp):
    p[0] = sa.Expr3_TypeCast(p[2], p[4])
  elif isinstance(p[1], sa.Variable) and len(p) == 4:
    p[0] = sa.Expr3_Var_Assign_Expr(p[1], p[2], p[3])
  else:
    p[0] = sa.Expr3_Var_Assign_Amp_Expr(p[1], p[2], p[4])

def p_expr1(p): 
  ''' 
  expr1 : INCREMENT variable
    | variable INCREMENT
    | DECREMENT variable
    | variable DECREMENT
    | variable
    | LPAREN expr RPAREN
    | ARRAY_TYPE array_declaration
    | function_call
    | scalar
    | TRUE
    | FALSE
  '''
  if isinstance(p[1], sa.Variable) and len(p) == 2:
    p[0] = sa.Expr1_Variable(p[1])
  elif p[1] == 'true':
    p[0] = sa.Expr1_True()
  elif p[1] == 'false':
    p[0] = sa.Expr1_False()
  elif isinstance(p[1], sa.Scalar):
    p[0] = sa.Expr1_Scalar(p[1])
  elif isinstance(p[1], sa.FunctionCall):
    p[0] = sa.Expr1_FunctionCall(p[1])
  elif (p[1] == 'array' and isinstance(p[2], sa.ArrayDeclaration)):
    p[0] = sa.Expr1_ArrayDeclaration(p[2])
  elif isinstance(p[2], sa.Expr):
    p[0] = sa.Expr1_ExprPar(p[2])
  elif p[2] == '++':
    p[0] = sa.Expr1_Variable_Increment(p[1])
  elif p[2] == '--':
    p[0] = sa.Expr1_Variable_Decrement(p[1])
  elif p[1] == '++':
    p[0] = sa.Expr1_Increment_Variable(p[2])
  elif p[1] == '--':
    p[0] = sa.Expr1_Decrement_Variable(p[2])
  
def p_exit_statement(p):
  '''
  exit_statement : EXIT exit_expr
    | EXIT
  '''  
  if len(p) == 3:
    p[0] = sa.Exit_ExitExpr(p[2])
  else: 
    p[0] = sa.Exit_Empty()
  
def p_die_statement(p):
  '''
  die_statement : DIE exit_expr
    | DIE
  '''
  if len(p) == 3:
    p[0] = sa.Die_ExitExpr(p[2])
  else:
    p[0] = sa.Die_Empty()

def p_exit_expr(p):
  '''
  exit_expr : LPAREN expr RPAREN
    | LPAREN RPAREN
  '''
  if len(p) == 4:
    p[0] = sa.ExitExpr_Expr(p[2])
  else:
    p[0] = sa.ExitExpr_Empty()

def p_array_declaration(p):
  '''
  array_declaration : LPAREN array_pair_list RPAREN
    | LPAREN RPAREN
  '''
  if isinstance(p[2], sa.ArrayPairList):
    p[0] = sa.ArrayDec_WithPairList(p[2])
  else:
    p[0] = sa.ArrayDec_NoPairList()


def p_statement(p):
  '''
  statement : expr SEMICOLON
    | if_statement 
    | while_statement
    | do_statement
    | for_statement
    | foreach_statement
    | break_statement
    | continue_statement 
    | return_statement
    | exit_statement SEMICOLON
    | die_statement SEMICOLON
    | global_statement SEMICOLON
  '''
  if isinstance(p[1], sa.Expr): 
    p[0] = sa.Statement_Expr(p[1], p[2])
  elif isinstance(p[1], sa.Exit):
    p[0] = sa.Statement_Exit(p[1])
  elif isinstance(p[1], sa.Die):
    p[0] = sa.Statement_Die(p[1])
  elif isinstance(p[1], sa.Break):
    p[0] = sa.Statement_Break(p[1])
  elif isinstance(p[1], sa.Continue):
    p[0] = sa.Statement_Continue(p[1])
  elif isinstance(p[1], sa.Return):
    p[0] = sa.Statement_Return(p[1])
  elif isinstance(p[1], sa.IfStatement):
    p[0] = sa.Statement_If(p[1])
  elif isinstance(p[1], sa.WhileStatement):
    p[0] = sa.Statement_While(p[1])
  elif isinstance(p[1], sa.DoWhileStatement):
    p[0] = sa.Statement_Do_While(p[1])
  elif isinstance(p[1], sa.ForeachStatement):
    p[0] = sa.Statement_Foreach(p[1])
  elif isinstance(p[1], sa.GlobalStatement):
    p[0] = sa.Statement_Global(p[1])
  elif isinstance(p[1], sa.ForStatement):
    p[0] = sa.Statement_For(p[1])
  
def p_global_statement(p):
  '''
  global_statement : GLOBAL global_var statement_COLON_GLOBAL 
    | GLOBAL global_var 
  '''
  if len(p) == 3:
    p[0] = sa.GlobalStatement_Single(p[2])
  else:
    p[0] = sa.GlobalStatement_Mul(p[2], p[3])
    
  
def p_if_statement(p):
  '''
  if_statement : statement_if if_statement_complement
    | statement_if 
  '''
  if len(p)==3:
    p[0] = sa.IfStatement_Complement(p[1],p[2])
  else:
    p[0] = sa.IfStatement_Single(p[1])

def p_statement_if(p):
  ''' 
  statement_if : IF expr_parentheses statement_BLOCK_OPT 
  '''
  if len(p) ==4:
    p[0] = sa.StatementIf_ExprParen(p[2],p[3])

def p_if_statement_complement(p):
  '''
  if_statement_complement : statement_elseif
    | statement_else
  '''
  p[0] = sa.IfStatement_Else(p[1])

def p_statement_else(p):
  '''
  statement_else : ELSE statement_BLOCK_OPT
  '''
  if len(p)==3:
    p[0] = sa.StatementElse_Else(p[2])


def p_statement_elseif(p):
  '''
  statement_elseif : ELSEIF expr_parentheses statement_BLOCK_OPT
  '''

def p_while_statement(p):
  '''
  while_statement : WHILE expr_parentheses statement_BLOCK_OPT
  '''
  if len(p)==4:
    p[0] = sa.WhileStatementSingle(p[2], p[3])
  
def p_do_statement(p):
  '''
  do_statement : DO statement_BLOCK_OPT WHILE expr_parentheses SEMICOLON
  '''
  p[0] = sa.DoWhileStatementSingle(p[2], p[4])

def p_break_statement(p):
  '''
  break_statement : BREAK expr SEMICOLON
    | BREAK SEMICOLON
  '''
  if len(p) == 4:
    p[0] = sa.Break_Expr(p[2])
  else:
    p[0] = sa.Break_Empty()

def p_continue_statement(p):
  '''
  continue_statement : CONTINUE expr SEMICOLON
    | CONTINUE SEMICOLON
  '''
  if len(p) == 4:
    p[0] = sa.Continue_Expr(p[2])
  else:
    p[0] = sa.Continue_Empty()
  
def p_return_statement(p):
  '''
  return_statement : RETURN expr SEMICOLON 
    | RETURN SEMICOLON 
  '''
  if len(p) == 4:
    p[0] = sa.Return_Expr(p[2])
  else:
    p[0] = sa.Return_Empty()
  
def p_for_statement(p):
  '''
  for_statement : FOR LPAREN for_parameters RPAREN statement_BLOCK_OPT
  '''
  p[0] = sa.ForStatement_For(p[3], p[5])
  
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
  if len(p) == 3:
    p[0] = sa.ForParameters_Empty()
  elif len(p) == 4 and isinstance(p[1], sa.ForExprOpt):
    p[0] = sa.ForParameters_Left(p[1])
  elif len(p) == 5 and isinstance(p[1], sa.ForExprOpt) and isinstance(p[3], sa.ForExprOpt):
    p[0] = sa.ForParameters_Left_Mid(p[1], p[3])
  elif len(p) == 5 and isinstance(p[1], sa.ForExprOpt) and isinstance(p[4], sa.ForExprOpt):
    p[0] = sa.ForParameters_Left_Right(p[1], p[4])
  elif len(p) == 4 and isinstance(p[2], sa.ForExprOpt):
    p[0] = sa.ForParameters_Mid(p[2])
  elif len(p) == 5 and isinstance(p[2], sa.ForExprOpt) and isinstance(p[4], sa.ForExprOpt):
    p[0] = sa.ForParameters_Mid_Right(p[2], p[4])
  elif len(p) == 4 and isinstance(p[3], sa.ForExprOpt):
    p[0] = sa.ForParameters_Right(p[3])
  else:
    p[0] = sa.ForParameters_Full(p[1], p[3], p[5])
  
  
def p_global_var(p):
  '''
  global_var : VARIABLE
    | DOLAR VARIABLE
    | DOLAR LKEY expr RKEY 
  '''
  if len(p) == 2:
    p[0] = sa.GlobalVar_Var(p[1])
  elif len(p) == 3:
    p[0] = sa.GlobalVar_DolarVar(p[2])
  else: 
    p[0] = sa.GlobalVar_DolarExpr(p[3])

def p_statement_COLON_GLOBAL(p):
  '''
  statement_COLON_GLOBAL : COLON global_var statement_COLON_GLOBAL
    | COLON global_var
  '''
  if len(p) == 3:
    p[0] = sa.GlobalVarMul_Single(p[2])
  else:
    p[0] = sa.GloballVarMul_Mul(p[2], p[3])

def p_ampersand_variable(p):
  '''
  ampersand_variable : AMPERSAND VARIABLE
    | VARIABLE
  '''
  if len(p) == 3:
    p[0] = sa.AmpersandVariable_WithAmp(p[2])
  else:
    p[0] = sa.AmpersandVariable_NoAmp(p[1])
  
def p_expr_parentheses(p):
  '''
  expr_parentheses : LPAREN expr RPAREN
  '''
  if len(p)==4:
    p[0] = sa.ExprParentheses_Expr(p[2])


def p_foreach_statement(p):
  '''
  foreach_statement : FOREACH LPAREN expr AS ampersand_variable RPAREN statement_BLOCK_OPT
  | FOREACH LPAREN expr AS ampersand_variable ATTR_ASSOC ampersand_variable RPAREN statement_BLOCK_OPT
  '''
  if len(p) == 8:
    p[0] = sa.ForeachStatement_NoAssoc(p[3], p[5], p[7])
  else: 
    p[0] = sa.ForeachStatement_WithAssoc(p[3], p[5], p[7], p[9])

def p_for_expr_OPT(p):
  '''
  for_expr_OPT : expr for_expr_COLON_EXPR
  | expr
  '''
  if len(p) == 3:
    p[0] = sa.ForExprOpt_Mul(p[1], p[2])
  else:
    p[0] = sa.ForExprOpt_Single(p[1])
    
def p_for_expr_COLON_EXPR(p):
  '''
  for_expr_COLON_EXPR : COLON expr for_expr_COLON_EXPR
    | COLON expr
  '''
  if len(p) == 3:
    p[0] = sa.ForExprColonExpr_Single(p[2])
  else:
    p[0] = sa.ForExprColonExpr_Mul(p[2], p[3])

def p_function_call(p):
  '''
  function_call : ID LPAREN function_call_parameter_list RPAREN
    | ID LPAREN RPAREN
  '''
  if len(p) == 4:
    p[0] = sa.FunctionCall_NoParameter(p[1])
  else:
    p[0] = sa.FunctionCall_WithParameter(p[1], p[3])

def p_function_call_parameter_list(p):
  '''
  function_call_parameter_list : function_call_parameter fc_parameter_list_COLON_PARAMETER
    |  function_call_parameter
  '''
  if len(p) == 2:
    p[0] = sa.FCParameterList_Single(p[1])
  else:
    p[0] = sa.FCParameterList_Mul(p[1], p[2])

def p_fc_parameter_list_COLON_PARAMETER(p):
  '''
  fc_parameter_list_COLON_PARAMETER : COLON function_call_parameter fc_parameter_list_COLON_PARAMETER
    | COLON function_call_parameter
  '''
  if len(p) == 4:
    p[0] = sa.FCParameterListColonParameter_Mul(p[2], p[3])
  else:
    p[0] = sa.FCParameterListColonParameter_Single(p[2])

def p_function_call_parameter(p):
  '''
  function_call_parameter : expr
    | AMPERSAND VARIABLE
  '''
  if len(p) == 2:
    p[0] = sa.FunctionCallParameter_Expr(p[1])
  else:
    p[0] = sa.FunctionCallParameter_AmpersandVariable(p[2])
  
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
  p[0] = sa.TypeCastOp_Token(p[1])
  
def p_assign_operator(p):
  '''
  assign_operator : ADD_ASSIGN
    | SUB_ASSIGN
    | MOD_ASSIGN
    | PLUS_ASSIGN
    | DIVIDE_ASSIGN
    | ASSIGN
  '''
  p[0] = sa.AssignOperator_Token(p[1]) 

def p_arithmetic_operator(p):
  '''
  arithmetic_operator : PLUS
    | DIVIDE
    | PERCENT
    | TIMES
    | MINUS
  '''
  p[0] = sa.ArithmeticOperator_Token(p[1])

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
    | AND
    | OR
  '''
  p[0] = sa.ComparissionOperator_Token(p[1])

def p_scalar(p):
  '''
  scalar : NUMBER_REAL
    | NUMBER_INTEGER
    | CONSTANT_ENCAPSED_STRING
  '''
  p[0] = sa.Scalar_Token(p[1])
  
def p_variable(p):
  '''
  variable : reference_variable
    | simple_indirect_reference_DOLAR reference_variable
  '''
  if len(p) == 2:
    p[0] = sa.Variable_Reference_Variable(p[1])
  else :
    p[0] = sa.Variable_Simple_Indirect(p[1], p[2])
  
def p_reference_variable(p):
  '''
  reference_variable : compound_variable reference_variable_SELECTOR
  | compound_variable
  ''' 
  if len(p) == 3:
    p[0] = sa.ReferenceVariable_Compound_Reference(p[1], p[2])
  else :
    p[0] = sa.ReferenceVariable_Compound(p[1])
  
def p_compound_variable(p):
  '''
  compound_variable : VARIABLE 
    | DOLAR LKEY expr RKEY 
  '''
  if len(p) == 5:
    p[0] = sa.CompoundVariableMul(p[3])
  else:
    p[0] = sa.CompoundVariableSingle(p[1])

def p_selector(p):
  '''
  selector : LBRACKET expr RBRACKET 
    | LBRACKET RBRACKET
  '''
  if len(p) == 4:
    p[0] = sa.SelectorWithExpr(p[2])
  else :
    p[0] = sa.SelectorWithoutExpr()

def p_function_declaration_statement(p):
  '''
  function_declaration_statement : FUNCTION fds_id fds_parameter fds_statements
  '''
  p[0] = sa.funcDecStatement_Function(p[2], p[3], p[4])
  
def p_fds_statements(p):
  '''
  fds_statements : LKEY inner_statement_MUL RKEY
    | LKEY RKEY
  '''
  if len(p) == 4:
    p[0] = sa.Fds_statements_withStatements(p[2])
  else: 
    p[0] = sa.Fds_statements_noStatements()
  
def p_fds_id(p):
  '''
  fds_id : AMPERSAND ID
    | ID
  '''
  if len(p) == 3:
    p[0] = sa.Fds_id_withAmpersand(p[2])
  else:
    p[0] = sa.Fds_id_noAmpersand(p[1])
  
def p_fds_parameter(p):
  '''
  fds_parameter : LPAREN parameter_list RPAREN
    | LPAREN RPAREN
  '''
  if len(p) == 4:
    p[0] = sa.Fds_parameter_withParameter(p[2])
  else:
    p[0] = sa.Fds_parameter_noParameter()

def p_parameter_list(p):  
  '''
  parameter_list : parameter parameter_list_COLON_PARAMETER 
    | parameter
  '''  
  if len(p) == 3:
    p[0] = sa.ParameterList_Parameter_Mul(p[1], p[2])
  else:
    p[0] = sa.ParameterList_Parameter_Single(p[1])

def p_parameter(p):
  ''' 
  parameter : VARIABLE 
    | parameter_prefix VARIABLE
    | VARIABLE ASSIGN static_scalar
    | parameter_prefix VARIABLE ASSIGN static_scalar
  '''
  if len(p) == 5:
    p[0] = sa.Parameter_Full(p[1], p[2], p[4])
  elif len(p) == 4:
    p[0] = sa.Parameter_Var_Sufix(p[1], p[3])
  elif len(p) == 3:
    p[0] = sa.Parameter_Prefix_Var(p[1], p[2])
  else: 
    p[0] = sa.Parameter_Var(p[1])
  
def p_parameter_prefix(p):
  '''
  parameter_prefix : parameter_type AMPERSAND
    | AMPERSAND
    | parameter_type
  '''
  if len(p) == 3:
    p[0] = sa.ParameterPrefix_PType_Amp(p[1])
  elif isinstance(p[1], sa.ParameterType):
    p[0] = sa.ParameterPrefix_PType(p[1])
  else:
    p[0] = sa.ParameterPrefix_Ampersand()

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
  p[0] = sa.ParameterType_Type(p[1])

#VERIFICAR SYNTAX
def p_static_scalar(p):
  '''
  static_scalar : common_scalar 
    | PLUS static_scalar
    | MINUS static_scalar
  '''
  if len(p) == 2:
    p[0] = sa.StaticScalar_CommonScalar(p[1])
  elif p[1] == '+':
    p[0] = sa.StaticScalar_Plus_Static(p[2]) 
  else:
    p[0] = sa.StaticScalar_Minus_Static(p[2])

def p_common_scalar(p): 
  '''
  common_scalar : NUMBER_REAL
    | NUMBER_INTEGER
    | CONSTANT_ENCAPSED_STRING
  '''
  p[0] = sa.CommonScalar_Token(p[1])
  
def p_array_pair_list(p):
  '''
  array_pair_list : array_pair array_pair_list_ARR_PAIR 
    | array_pair
  '''
  if len(p)==3:
    p[0] = sa.ArrayPairList_ArrayPair_Mul(p[1],p[2])
  else:
    p[0] = sa.ArrayPairList_ArrayPair_Single(p[1])
 
def p_array_pair(p):
  ''' 
  array_pair : expr
    | AMPERSAND variable
    | expr ATTR_ASSOC expr
    | expr ATTR_ASSOC AMPERSAND variable
  '''
  if len(p) == 2:
    p[0] = sa.ArrayPair_Expr(p[1])
  elif len(p) == 3:
    p[0] = sa.ArrayPair_Variable(p[2])
  elif len(p) == 4:
    p[0] = sa.ArrayPair_Attr_Expr(p[1],p[3])
  elif len(p) == 5:
    p[0] =  sa.ArrayPair_Attr_AmpersandVariable(p[1],p[4])
    

# Expressões regulares transformadas em regras.
# ======================================================================
def p_statement_MUL(p):
  '''
  statement_MUL : statement statement_MUL
    | statement
  '''
  if len(p) == 3:
    p[0] = sa.statementMulMul(p[1], p[2])
  else:
    p[0] = sa.statementMulSingle(p[1])
  
def p_statement_BLOCK_OPT(p):
  '''
  statement_BLOCK_OPT : statement 
    | LKEY statement_MUL RKEY 
    | LKEY RKEY
  '''
  if len(p) == 2:
    p[0] = sa.StatementBlockOpt_Statement(p[1])
  elif len(p) == 4:
    p[0] = sa.StatementBlockOpt_StatementMul(p[2])
  elif len(p) == 3:
    p[0] = sa.StatementBlockOpt_Empty()

def p_parameter_list_COLON_PARAMETER(p):
  '''
  parameter_list_COLON_PARAMETER : COLON parameter parameter_list_COLON_PARAMETER
    | COLON parameter
  '''
  if len(p) == 4:
    p[0] = sa.ParameterListColonParameter_Mul(p[2], p[3])
  else:
    p[0] = sa.ParameterListColonParameter_Single(p[2])
  
def p_reference_variable_SELECTOR(p):
  '''
  reference_variable_SELECTOR : selector reference_variable_SELECTOR
    | selector
  '''
  if len(p) == 3:
    p[0] = sa.ReferenceVariableSelectorMul(p[1], p[2])
  else :
    p[0] = sa.ReferenceVariableSelectorSingle(p[1])

def p_simple_indirect_reference_DOLAR(p):
  '''
  simple_indirect_reference_DOLAR : DOLAR simple_indirect_reference_DOLAR
    | DOLAR
  '''
  if len(p) == 3:
    p[0] = sa.SimpleIndirectReference_Mul(p[2])
  else:
    p[0] = sa.SimpleIndirectReference_Single()
  

def p_array_pair_list_ARR_PAIR(p):
  '''
  array_pair_list_ARR_PAIR : COLON array_pair array_pair_list_ARR_PAIR
    | COLON array_pair
  '''
  if len(p)==4:
    p[0] = sa.ArrayPairList_Mul(p[2],p[3])
  elif len(p)==3:
    p[0] = sa.ArrayPairList_Single(p[2])


def p_error(p):
    print(p)
    print("Syntax error in input!")
 

lex.lex()
arquivo = '''
<?php
function add($valor, $valor1){}
?>
'''

lex.input(arquivo)
parser = yacc.yacc()
result = parser.parse(debug=False)

visitor = sv.SemanticVisitor()
#v = vis.Visitor()
#for r in result:
result.accept(visitor)