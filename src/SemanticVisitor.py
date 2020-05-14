from AbstractVisitor import AbstractVisitor
import SymbolTable as st
from Visitor import Visitor

import SintaxeAbstrata as sa

class SemanticVisitor(AbstractVisitor):
  
  def __init__(self):
    self.printer = Visitor()
    st.beginScope('global')
    
  def visitMain_MainInner(self, main):
    main.mainInner.accept(self)
    
  def visitMain_MainInner_Empty(self):
    st.endScope()
    return []
    
  def visitMainInner_InnerStatement(self, mainInner):
    mainInner.innerStatement.accept(self)
    
  def visitInnerStatement_FuncDecStatement(self, innerStatement):
    innerStatement.funcDecStatement.accept(self)
    
  def visitFuncDecStatement_Function(self, funcDecStatement):
    funcId = funcDecStatement.fds_id.accept(self)
    params = funcDecStatement.fds_parameter.accept(self)
    st.addFunction(funcId, params)
    st.beginScope(funcId)
    for i in range(0, len(params)):
      st.addVar(params[i])
    #funcDecStatement.fds_statements.accept(self)
    
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
    
  def visitFds_statements_noStatements(self):
    return []