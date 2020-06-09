import ply.yacc as yacc
import ply.lex as lex
import SemanticVisitor as sv
from Lex import *
import SintaxeAbstrata as sa
import Visitor as vis

# DIREITA PARA ESQUERDA => ASSOC. DIREITA
# ESQUERDA PARA DIREITA => ASSOC. ESQUERDA

precedence = (
  ('right', 'ADD_ASSIGN', 'SUB_ASSIGN', 'MOD_ASSIGN', 'TIMES_ASSIGN', 'DIVIDE_ASSIGN', 'ASSIGN'),
  ('left','INTE_DOT', 'DDOT'),
  ('left', 'AND', 'OR'),
  ('left', 'EQUALS','NOT_EQUAL', 'LESS_THAN', 'LESS_EQUAL', 'GREAT_THAN', 'GREAT_EQUAL'),
  ('left', 'PLUS', 'MINUS'),
  ('left', 'TIMES', 'DIVIDE','PERCENT'),
  ('right', 'EXC_DOT'),
  ('left', 'POS_INCREMENT','POS_DECREMENT'),
  ('right', 'PRE_INCREMENT', 'PRE_DECREMENT', 'RPAREN'),
  ('right', 'UMINUS'),
)

def p_main(p):
  '''
  main : BEGIN_PROGRAM main_program END_PROGRAM 
  | BEGIN_PROGRAM END_PROGRAM 
  '''
  if len(p) == 4:
    p[0] = sa.Main_MainProgram(p[2])
  else:
    p[0] = sa.Main_Empty()
    
def p_main_program(p):
  '''
  main_program : inner_statement main_program
    | inner_statement
  '''
  if len(p) == 3:
    p[0] = sa.MainProgram_InnerStatement_Recursive(p[1], p[2])
  else:
    p[0] = sa.MainProgram_InnerStatement(p[1])

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
  expr : expr PLUS expr
    | expr MINUS expr 
    | MINUS expr %prec UMINUS
    | expr DIVIDE expr
    | expr PERCENT expr
    | expr TIMES expr   
    | expr EQUALS expr
    | expr NOT_EQUAL expr
    | expr GREAT_THAN expr 
    | expr GREAT_EQUAL expr
    | expr LESS_THAN expr
    | expr LESS_EQUAL expr
    | expr AND expr
    | expr OR expr
    | EXC_DOT expr
    | PRE_INCREMENT variable
    | variable POS_INCREMENT
    | PRE_DECREMENT variable
    | variable POS_DECREMENT
    | variable
    | LPAREN expr RPAREN
    | ARRAY_TYPE array_declaration
    | LPAREN typecast_operator RPAREN expr 
    | function_call
    | expr INTE_DOT expr DDOT expr
    | variable ADD_ASSIGN expr
    | variable SUB_ASSIGN expr
    | variable MOD_ASSIGN expr
    | variable TIMES_ASSIGN expr
    | variable DIVIDE_ASSIGN expr
    | variable ASSIGN expr
    | NUMBER_INTEGER
    | NUMBER_REAL
    | CONSTANT_ENCAPSED_STRING
    | TRUE
    | FALSE
  '''
  if isinstance(p[1], sa.Expr) and p[2] == '+' and isinstance(p[3], sa.Expr):
    p[0] = sa.Expr_Plus(p[1],p[3])
  elif isinstance(p[1], sa.Expr) and p[2] == '-' and isinstance(p[3], sa.Expr):
    p[0] = sa.Expr_Minus(p[1],p[3])
  elif p[1]== '-'  and isinstance(p[2], sa.Expr):
    p[0] = sa.Expr_Uminus(p[2])
  elif isinstance(p[1], sa.Expr) and p[2] == '*' and isinstance(p[3], sa.Expr):
    p[0] = sa.Expr_Times(p[1],p[3])
  elif isinstance(p[1], sa.Expr) and p[2] == '/' and isinstance(p[3], sa.Expr):
    p[0] = sa.Expr_Divide(p[1],p[3])
  elif isinstance(p[1], sa.Expr) and p[2] == '%' and isinstance(p[3], sa.Expr):
    p[0] = sa.Expr_Mod(p[1],p[3])
  elif isinstance(p[1], sa.Expr) and p[2] == '==' and isinstance(p[3], sa.Expr):
    p[0] = sa.Expr_Equals(p[1],p[3])
  elif isinstance(p[1], sa.Expr) and p[2] == '!=' and isinstance(p[3], sa.Expr):
    p[0] = sa.Expr_NotEquals(p[1],p[3])
  elif isinstance(p[1], sa.Expr) and p[2] == '>' and isinstance(p[3], sa.Expr):
    p[0] = sa.Expr_GreatThan(p[1],p[3])
  elif isinstance(p[1], sa.Expr) and p[2] == '>=' and isinstance(p[3], sa.Expr):
    p[0] = sa.Expr_GreatEqual(p[1],p[3])
  elif isinstance(p[1], sa.Expr) and p[2] == '<' and isinstance(p[3], sa.Expr):
    p[0] = sa.Expr_LessThan(p[1],p[3])
  elif isinstance(p[1], sa.Expr) and p[2] == '<=' and isinstance(p[3], sa.Expr):
    p[0] = sa.Expr_LessEqual(p[1],p[3])
  elif isinstance(p[1], sa.Expr) and p[2] == '&&' and isinstance(p[3], sa.Expr):
    p[0] = sa.Expr_AndLogical(p[1],p[3])
  elif isinstance(p[1], sa.Expr) and p[2] == '||' and isinstance(p[3], sa.Expr):
    p[0] = sa.Expr_OrLogical(p[1],p[3])
  elif p[1] == '!':
    p[0] = sa.Expr_NotLogical(p[2])
  elif len(p)==3 and p[1] =='++' and isinstance(p[2], sa.Variable):
    p[0] = sa.Expr_PreIncrement(p[2])
  elif len(p)==3 and isinstance(p[1], sa.Variable) and p[2] =='++':
    p[0] = sa.Expr_PosIncrement(p[1])
  elif len(p)==3 and p[1] =='--' and isinstance(p[2], sa.Variable):
    p[0] = sa.Expr_PreDecrement(p[2])
  elif len(p)==3 and isinstance(p[2], sa.Variable) and p[1] =='--':
    p[0] = sa.Expr_PosDecrement(p[1])
  elif p[1]=='(' and isinstance(p[2], sa.Expr) and p[3]==')':
    p[0] = sa.Expr_ParenExpr(p[2])
  elif len(p) == 3 and isinstance(p[2], sa.ArrayDeclaration):
    p[0] = sa.Expr_ArrayDeclaration(p[2])
  elif isinstance(p[1], sa.FunctionCall):
    p[0] = sa.Expr_FunctionCall(p[1])
  elif len(p) == 6 and isinstance(p[1], sa.Expr) and isinstance(p[3], sa.Expr) and  isinstance(p[5], sa.Expr):
    p[0] = sa.Expr_TernaryOp(p[1],p[3],p[5])  
  elif len(p) == 4 and isinstance(p[1], sa.Variable) and p[2] == '=' and isinstance(p[3], sa.Expr): 
    p[0] = sa.Expr_AssignExpr(p[1],p[3])
  elif len(p) == 4 and isinstance(p[1], sa.Variable) and p[2] == '+=' and isinstance(p[3], sa.Expr): 
    p[0] = sa.Expr_AddAssignExpr(p[1],p[3])
  elif len(p) == 4 and isinstance(p[1], sa.Variable) and p[2] == '-=' and isinstance(p[3], sa.Expr): 
    p[0] = sa.Expr_SubAssignExpr(p[1],p[3])
  elif len(p) == 4 and isinstance(p[1], sa.Variable) and p[2] == '%=' and isinstance(p[3], sa.Expr): 
    p[0] = sa.Expr_ModAssignExpr(p[1],p[3])
  elif len(p) == 4 and isinstance(p[1], sa.Variable) and p[2] =='/='and isinstance(p[3], sa.Expr):
    p[0] = sa.Expr_DivideAssignExpr(p[1],p[3])
  elif len(p) == 4 and isinstance(p[1], sa.Variable) and p[2] =='*=' and isinstance(p[3], sa.Expr): 
    p[0] = sa.Expr_TimesAssignExpr(p[1],p[3])
  elif p[1] == '(' and isinstance(p[2], sa.TypeCastOp) and p[3] ==')':
    p[0] = sa.Expr_TypeCastOp(p[2],p[4])
  elif isinstance(p[1], sa.Variable):
    p[0] = sa.Expr_Variable(p[1])
  elif p[1] == 'true' or p[1] == 'false':
    p[0] = sa.Expr_Boolean(p[1])
  elif isinstance(p[1], int):
    p[0] = sa.Expr_NumberInt(p[1])
  elif isinstance(p[1], float): 
    p[0] = sa.Expr_NumberFloat(p[1])
  elif isinstance(p[1], str): 
    p[0] = sa.Expr_EncapsedString(p[1]) 
    
def p_typecast_operator(p):
  '''
  typecast_operator : INT_TYPE
    | FLOAT_TYPE
    | ARRAY_TYPE
    | STRING_TYPE
    | BOOL_TYPE
  '''
  p[0] = sa.TypeCastOp_Token(p[1])
  
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
    | while_statement
    | if_statement
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
  #elif isinstance(p[1], sa.IfStatement):
  #  p[0] = sa.Statement_If(p[1])
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

def p_if_statement(p):
  '''
  if_statement : IF expr_parentheses statement_block_optional
  '''
def p_if_statement1(p):
  '''
  
  '''
def p_if_statement1(p):
  '''
  '''
def p_global_statement(p):
  '''
  global_statement : GLOBAL global_var statement_COLON_GLOBAL 
    | GLOBAL global_var 
  '''
  if len(p) == 3:
    p[0] = sa.GlobalStatement_Single(p[2])
  else:
    p[0] = sa.GlobalStatement_Mul(p[2], p[3])


def p_while_statement(p):
  '''
  while_statement : WHILE expr_parentheses statement_block_optional
  '''
  if len(p)==4:
    p[0] = sa.WhileStatementSingle(p[2], p[3])
  
def p_do_statement(p):
  '''
  do_statement : DO statement_block_optional WHILE expr_parentheses SEMICOLON
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
  for_statement : FOR LPAREN for_parameters RPAREN statement_block_optional
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
    p[0] = sa.GlobalVarMul_Mul(p[2], p[3])

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
  foreach_statement : FOREACH LPAREN expr AS ampersand_variable RPAREN statement_block_optional
  | FOREACH LPAREN expr AS ampersand_variable ATTR_ASSOC ampersand_variable RPAREN statement_block_optional
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

def p_variable(p):
  '''
  variable : VARIABLE variable_array_selector
    | VARIABLE
  '''
  if len(p) == 2:
    p[0] = sa.Variable_Single(p[1])
  else:
    p[0] = sa.Variable_Array(p[1], p[2])

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
  parameter_list : parameter parameter_list_colon_parameter 
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
    | STRING_TYPE
    | FLOAT_TYPE
    | ARRAY_TYPE
    | BOOL_TYPE
  '''
  p[0] = sa.ParameterType_Type(p[1])

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
  
def p_statement_block_optional(p):
  '''
  statement_block_optional : statement 
    | LKEY statement_MUL RKEY 
    | LKEY RKEY
  '''
  if len(p) == 2:
    p[0] = sa.StatementBlockOpt_Statement(p[1])
  elif len(p) == 4:
    p[0] = sa.StatementBlockOpt_StatementMul(p[2])
  elif len(p) == 3:
    p[0] = sa.StatementBlockOpt_Empty()

def p_parameter_list_colon_parameter(p):
  '''
  parameter_list_colon_parameter : COLON parameter parameter_list_colon_parameter
    | COLON parameter
  '''
  if len(p) == 4:
    p[0] = sa.ParameterListColonParameter_Mul(p[2], p[3])
  else:
    p[0] = sa.ParameterListColonParameter_Single(p[2])
  
def p_variable_array_selector(p):
  '''
    variable_array_selector : selector variable_array_selector
    | selector
  '''
  if len(p) == 3:
    p[0] = sa.ReferenceVariableSelectorMul(p[1], p[2])
  else :
    p[0] = sa.ReferenceVariableSelectorSingle(p[1])

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
    $valor = 1.5;
    
    $v = $valor + $valor - $valor / $valor * $valor;

?>
'''

lex.input(arquivo)
parser = yacc.yacc()
result = parser.parse(debug=False)
v = sv.SemanticVisitor()
#v = vis.Visitor()
#for r in result:
result.accept(v)