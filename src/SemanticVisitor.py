from AbstractVisitor import AbstractVisitor
import SymbolTable as st
from Visitor import Visitor

import SintaxeAbstrata as sa

def coercion(type1, type2):
  if (type1 in st.Number and type2 in st.Number):
      if (type1 == st.FLOAT or type2 == st.FLOAT):
          return st.FLOAT
      else:
          return st.INT
  else:
      return None


class SemanticVisitor(AbstractVisitor):
  
  def __init__(self):
    self.printer = Visitor()
    st.beginScope('global')
    
  def visitMain_MainInner(self, main):
    main.mainInner.accept(self)
    
  def visitMain_MainInner_Empty(self, main):
    st.endScope()
    
  def visitMainInner_InnerStatement(self, mainInner):
    mainInner.innerStatement.accept(self)
    
  def visitInnerStatement_FuncDecStatement(self, innerStatement):
    innerStatement.funcDecStatement.accept(self)
    
  def visitInnerStatement_Statement(self, innerStatement):
    innerStatement.statement.accept(self)
    
  def visitFuncDecStatement_Function(self, funcDecStatement):
    funcId = funcDecStatement.fds_id.accept(self)
    params = funcDecStatement.fds_parameter.accept(self)
    st.addFunction(funcId, params)
    st.beginScope(funcId)
    for i in range(0, len(params)):
      st.addVar(params[i])
    funcDecStatement.fds_statements.accept(self)
    st.endScope()
    
  def visitFds_id_withAmpersand(self, fds_id):
    return '&' + fds_id.id
    
  def visitFds_id_noAmpersand(self, fds_id):
    return fds_id.id
  
  def visitFds_parameter_noParameter(self):
    return {}
  
  def visitFds_parameter_withParameter(self, fds_parameter):
    return fds_parameter.parameter_list.accept(self)
    
  def visitParameterList_Parameter_Mul(self, parameterList):
    return parameterList.parameter.accept(self) + parameterList.parameter_list_colon_parameter.accept(self)
    
  def visitParameterList_Parameter_Single(self, parameterList):
    return parameterList.parameter.accept(self)
    
  def visitParameterListColonParameter_Mul(self, parameterListColonParameter):
    return parameterListColonParameter.parameter.accept(self) + parameterListColonParameter.parameterListColonParameter.accept(self)
  
  def visitParameterListColonParameter_Single(self, parameterListColonParameter):
    return parameterListColonParameter.parameter.accept(self)
    
  def visitParameter_Var(self, parameter):
    return [parameter.variable]
  
  def visitFds_statements_withStatements(self, fds_statements):
    fds_statements.inner_statement_MUL.accept(self)
    
  def visitFds_statements_noStatements(self):
    return []
  
  def visitInnerStatementMul_Mul(self, innerStatementMul):
    innerStatementMul.innerStatement.accept(self)
    innerStatementMul.innerStatementMul.accept(self)
    
  def visitInnerStatementMul_Single(self, innerStatementMul):
    innerStatementMul.innerStatement.accept(self)
    
  def visitStatement_Expr(self, statement):
    statement.expr.accept(self)
    
  def visitExpr_Expr1(self, expr):
    expr.expr1.accept(self)
    
  def visitExpr1_Variable(self, expr1):
    expr1.variable.accept(self)
    
  def visitVariable_Reference_Variable(self, variable):
    variable.reference_variable.accept(self)
    
  def visitReferenceVariable_Compound(self, referenceVariable):
    referenceVariable.compoundvariable.accept(self)
    
  #A variável será definida caso não esteja na tabela de símbolos
  def visitCompoundVariableSingle(self, singleVariable):
    if(st.getBindable(singleVariable.variable) == None):
      st.addVar(singleVariable.variable)
