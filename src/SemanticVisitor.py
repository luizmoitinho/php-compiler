from AbstractVisitor import AbstractVisitor
import SymbolTable as st
from Visitor import Visitor

import SintaxeAbstrata as sa

def isValidNumber(number):
    try:
        if(number in st.Number and int(number) or float(number) ):
            return True
    except ValueError:
        return False

def coercion(type1, type2):
    if (type1 in st.Number and type2 in st.Number):
        if (type1 == st.FLOAT or type2 == st.FLOAT):
            return st.FLOAT
        return st.INT
    return None

class SemanticVisitor(AbstractVisitor):
  
  def __init__(self):
    self.printer = Visitor()
    st.beginScope('global')
    
  def visitMain_MainInner(self, main):
    main.mainInner.accept(self)
    
  def visitMain_MainInner_Empty(self, main):
    st.endScope()
    
  def visitMainInner_InnerStatement_MainInner(self, mainInner):
    mainInner.innerStatement.accept(self)
    mainInner.mainInner.accept(self)
    
  def visitMainInner_InnerStatement(self, mainInner):
    mainInner.innerStatement.accept(self)
    
  def visitInnerStatement_FuncDecStatement(self, innerStatement):
    innerStatement.funcDecStatement.accept(self)

  def visitInnerStatement_Statement(self, innerStatement):
    innerStatement.statement.accept(self)

  def visitExprParentheses_Expr(self, exprParentheses):
    exprParentheses.expr.accept(self)

  def visitStatementBlockOpt_Statement(self, statementBlockOpt):
    statementBlockOpt.statement.accept(self)

  def visitStatementBlockOpt_StatementMul(self, statementBlockOpt):
    statementBlockOpt.statementmul.accept(self)
  
  def visitstatementMulSingle(self, statementMul):
    statementMul.statement.accept(self)

  def visitstatementMulMul(self, statementMul):
    statementMul.statement.accept(self)
    statementMul.statementMul.accept(self)

  def visitStatement_While(self, statement):
    statement.whilee.accept(self)

  def visitWhileStatementSingle(self, whileStatement):
    whileStatement.exprparentheses.accept(self)
    whileStatement.statement.accept(self)

  def visitFuncDecStatement_Function(self, funcDecStatement):
    funcId = funcDecStatement.fds_id.accept(self)
    params = funcDecStatement.fds_parameter.accept(self)
    functionExists = st.getBindable(funcId)
    if functionExists == None:
      st.addFunction(funcId, params)
      st.beginScope(funcId)
      for i in range(0, len(params)):
        st.addVar(params[i])
      funcDecStatement.fds_statements.accept(self)
      st.endScope()
    else:
      print('ERROR: Function', funcId, 'has already been declared.')
    
  def visitFds_id_withAmpersand(self, fds_id):
    return fds_id.id
    
  def visitFds_id_noAmpersand(self, fds_id):
    return fds_id.id
  
  def visitFds_parameter_noParameter(self):
    return []
  
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
    print(parameter.variable)
    return [parameter.variable]
  
  def visitFds_statements_withStatements(self, fds_statements):
    return fds_statements.inner_statement_MUL.accept(self)
    
  def visitFds_statements_noStatements(self, fds_statements):
    return 
  
  def visitInnerStatementMul_Mul(self, innerStatementMul):
    innerStatementMul.innerStatement.accept(self)
    innerStatementMul.innerStatementMul.accept(self)
    
  def visitInnerStatementMul_Single(self, innerStatementMul):
    innerStatementMul.innerStatement.accept(self)
    
  def visitStatement_Expr(self, statement):
    return statement.expr.accept(self)
    
  def visitExpr_Expr1(self, expr):
    return expr.expr1.accept(self)
  
  def visitExpr_Expr3(self, expr):
    return expr.expr3.accept(self)
  
  def visitExpr_Expr1_Expr2(self, expr):
    type1 = expr.expr1.accept(self)
    type2 = expr.expr2.accept(self)
    #verificar se os tipo da expressão é uma variável, para acessar o tipo dela
    if type1 != None and st.TYPE in type1:
      if type1[st.TYPE] == None:
        print('ERROR: The value of', type1[st.NAME], 'is undefined.')
      type1 = type1[st.TYPE]
      
    if type2 != None and st.TYPE in type2:
      if type2[st.TYPE] == None:
        print('ERROR: The value of', type2[st.NAME], 'is undefined.')
      type2 = type2[st.TYPE]
  
    c = coercion(type1, type2)
    if (c == None):
      print('ERROR: Expression ', end='')
      expr.expr1.accept(self.printer)
      print(' has type', type1, 'while expression "', end='')
      expr.expr2.accept(self.printer)
      print(' " has type', type2)
    return c
    
  def visitExpr2_ArithmeticOp(self, expr2):
    expr2.arithmeticOp.accept(self)
    return expr2.expr.accept(self)
  
  def visitExpr3_Var_Assign_Expr(self, expr3):
    bindable = expr3.variable.accept(self)
    assignOp = expr3.assignOp.accept(self)
    exprType = expr3.expr.accept(self)
    
    if assignOp == '=':
      if exprType != None:
        if st.TYPE in exprType:
          st.updateBindableType(bindable[st.NAME], exprType[st.TYPE])
        else:
          st.updateBindableType(bindable[st.NAME], exprType)
      else:
        st.updateBindableType(bindable[st.NAME], None)
    elif bindable[st.TYPE] == None:
        print('ERROR: Invalid atribution', assignOp, 'on variable', bindable[st.NAME], 'that has type', bindable[st.TYPE]) 
    else:
      if exprType != None:
        if st.TYPE in exprType:
          st.updateBindableType(bindable[st.NAME], exprType[st.TYPE])
        else:
          st.updateBindableType(bindable[st.NAME], exprType)
      else:
        st.updateBindableType(bindable[st.NAME], None)
    
  def visitExpr1_Variable(self, expr1):
    return expr1.variable.accept(self) 
  
  def visitExpr1_Variable_Increment(self, expr1):
    variable = expr1.variable.accept(self)
    if variable[st.TYPE] not in st.Number:
      print('ERROR: Cannot increment variable', variable[st.NAME], 'with type', variable[st.TYPE])
      
  def visitExpr1_Variable_Decrement(self, expr1):
    variable = expr1.variable.accept(self)
    if variable[st.TYPE] not in st.Number:
      print('ERROR: Cannot decrement variable', variable[st.NAME], 'with type', variable[st.TYPE])
    
  def visitExpr1_Increment_Variable(self, expr1):
    variable = expr1.variable.accept(self)
    if variable[st.TYPE] not in st.Number:
      print('ERROR: Cannot increment variable', variable[st.NAME], 'with type', variable[st.TYPE])
    
  def visitExpr1_Decrement_Variable(self, expr1):
    variable = expr1.variable.accept(self)
    if variable[st.TYPE] not in st.Number:
      print('ERROR: Cannot decrement variable', variable[st.NAME], 'with type', variable[st.TYPE])
    
  def visitExpr1_FunctionCall(self, expr1):
    return expr1.functionCall.accept(self)
    
  def visitExpr1_True(self, expr1):
    return st.BOOL
  
  def visitExpr1_False(self, expr1):
    return st.BOOL
  
  def visitExpr1_Scalar(self, expr1):
    return expr1.scalar.accept(self)
    
  def visitVariable_Reference_Variable(self, variable):
    return variable.reference_variable.accept(self)
    
  def visitReferenceVariable_Compound(self, referenceVariable):
    return referenceVariable.compoundvariable.accept(self)

  def visitCompoundVariableSingle(self, singleVariable):
    variable = st.getBindable(singleVariable.variable)
    if(variable == None):
      return st.addVar(singleVariable.variable)
    return variable
  
  def visitFunctionCall_NoParameter(self, functionCall):
    bindable = st.getBindable(functionCall.id)
    if bindable == None:
      print('ERROR: Function', functionCall.id,'called but never defined.')
      
  def visitFunctionCall_WithParameter(self, functionCall):
    bindable = st.getBindable(functionCall.id)
    if bindable == None:
      print('ERROR: Function', functionCall.id, 'called but never defined.')
    if bindable != None and bindable[st.BINDABLE] == st.FUNCTION:
      params = functionCall.parameterList.accept(self)
      if len(params) != len(bindable[st.PARAMS]):
        print('ERROR: Number of parameters of function', functionCall.id, 'differs from declaration.')
        
  def visitFCParameterList_Single(self, fcParameterList):
    return fcParameterList.fcParameter.accept(self) 

  def visitFCParameterList_Mul(self, fcParameterList):
    return fcParameterList.fcParameter.accept(self), fcParameterList.fcColonParameter.accept(self)
    
  def visitFCParameterListColonParameter_Single(self, fcParameterListColonParameter):
    return [fcParameterListColonParameter.fcParameter.accept(self)]
    
  def visitFCParameterListColonParameter_Mul(self, fcParameterListColonParameter):
    return [fcParameterListColonParameter.fcParameter.accept(self)] + fcParameterListColonParameter.fcplColonParameter.accept(self)
  
  def visitFunctionCallParameter_Expr(self, functionCallParameter):
    return functionCallParameter.expr.accept(self)
    
  def visitFunctionCallParameter_AmpersandVariable(self, functionCallParameter):
    return functionCallParameter.variable
  
  def visitScalar_Token(self, scalar):
    if isinstance(scalar.token, int):
      return st.INT
    elif isinstance(scalar.token, float):
      return st.FLOAT
    elif isinstance(scalar.token, str):
      return st.STRING
    
  def visitAssignOperator_Token(self, assignOp):
    return assignOp.token
  
  def visitArithmeticOperator_Token(self, arithmeticOp):
    return arithmeticOp.token

