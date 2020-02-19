# -------------------------
# ExpressionLanguageParser.py
#----------------------

import ply.yacc as yacc
import ply.lex as lex

from ExpressionLanguageLex import tokens
import SintaxeAbstrata as sa

def p_exp_soma(p):
  '''exp : exp SOMA exp1 
    | exp1'''
  if(len(p) == 4):
    p[0] = sa.SomaExp(p[1], p[3])
  else:
    p[0] = p[1]
  
def p_exp1_vezes(p):
  '''exp1 : exp1 VEZES exp2 
    | exp2'''
  if(len(p) == 4):
    p[0] = sa.MulExp(p[1], p[3])
  else:
    p[0] = p[1]
    
def p_exp2_expo(p):
  '''exp2 : exp2 POT exp3
    | exp3'''
  if(len(p) == 4):
    p[0] = sa.PotExp(p[1], p[3])
  else:
    p[0] = p[1]
  
def p_exp3(p):
  '''exp3 : assign
    | NUMBER
    | ID
    | call'''
  if(isinstance(p[1], sa.Call)):
    p[0] = sa.CallExp(p[1])
  elif(isinstance(p[1], sa.Assign)):
    p[0] = sa.AssignExp(p[1])
  else:
    p[0] = p[1]
  
  
def p_call(p):
  '''call :  ID LPAREN params RPAREN
  | ID LPAREN RPAREN
  '''
  if(len(p) == 5):
    p[0] = sa.ParamsCall(p[1], p[3])
  else:
    p[0] =  sa.SingleParam(p[1])
   
    
def p_params(p):
  '''params : ID COMMA params
    | ID'''
  if(len(p) == 4):
    p[0] = sa.CompoundParams(p[3])
  else:
    p[0] =  sa.SingleParam(p[1])
    
def p_assign(p):
  '''assign : ID IGUAL exp'''
  
    
parser = yacc.yacc()
result = parser.parse(debug=True)
# v = Visitor()
# result.accept(v)