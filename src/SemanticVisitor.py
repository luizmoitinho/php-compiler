from AbstractVisitor import AbstractVisitor
import SymbolTable as st
from Visitor import Visitor

import ErrorLog as el

import SintaxeAbstrata as sa

def isValidNumber(number):
    try:
        if(number in st.Number and int(number) or float(number) ):
            return True
    except ValueError:
        return False
      
def isTypePrimitive(type):
  if(type in st.Number or type == st.BOOL or type == st.ARRAY):
    return True
  return False

def isVariable(self, exprType):
  if type(exprType) is dict:
      return exprType[st.TYPE] 
  return exprType

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
    
  def visitMain_MainProgram(self, main):
    main.mainInner.accept(self)
    
  def visitMain_Empty(self, main):
    st.endScope()
    
  def visitMainProgram_InnerStatement_Recursive(self, mainInner):
    mainInner.innerStatement.accept(self)
    mainInner.mainInner.accept(self)
    
  def visitMainProgram_InnerStatement(self, mainInner):
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
    
  def visitStatement_If(self, statementIf):
    statementIf._if.accept(self)
  
  def visitStatementIf_Mul(self, statementIfMul):
    statementIfMul.expr_parentheses.accept(self)
    statementIfMul.statement_BLOCK_OPT.accept(self)
    statementIfMul.statement_if.accept(self)

  def visitStatementIf_Single(self, ifSingle):
    ifSingle.expr_parentheses.accept(self)
    ifSingle.statement_BLOCK_OPT.accept(self)

  def visitStatement_While(self, statement):
    statement.whilee.accept(self)

  def visitWhileStatementSingle(self, whileStatement):
    st.beginScope('while')
    exprBool = whileStatement.exprparentheses.accept(self)
    whileStatement.statement.accept(self)
    st.endScope()

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
  
  def visitExpr_Plus(self, exprPlus):
    type1 = exprPlus.expr1.accept(self)
    type2 = exprPlus.expr2.accept(self)
    
    type1 = isVariable(self, type1)
    type2 = isVariable(self, type2)
    
    c = coercion(type1, type2) 
    if (c == None):
      el.ExpressionTypeError(self, exprPlus, type1, type2)
    return c
    
  def visitExpr_Minus(self, exprMinus):
    type1 = exprMinus.expr1.accept(self)
    type2 = exprMinus.expr2.accept(self)
    
    type1 = isVariable(self, type1)
    type2 = isVariable(self, type2)
    
    c = coercion(type1, type2) 
    if (c == None):
      el.ExpressionTypeError(self, exprMinus, type1, type2)
    return c

  def visitExpr_Times(self, exprTimes):
    type1 = exprTimes.expr1.accept(self)
    type2 = exprTimes.expr2.accept(self)
    
    type1 = isVariable(self, type1)
    type2 = isVariable(self, type2)
    
    c = coercion(type1, type2) 
    if (c == None):
      el.ExpressionTypeError(self, exprTimes, type1, type2)
    return c

  def visitExpr_Divide(self, exprDivide):
    type1 = exprDivide.expr1.accept(self)
    type2 = exprDivide.expr2.accept(self)
    
    type1 = isVariable(self, type1)
    type2 = isVariable(self, type2)
    
    c = coercion(type1, type2) 
    if (c == None):
      el.ExpressionTypeError(self, exprDivide, type1, type2)
    return c

  def visitExpr_Uminus(self, exprUminus):
    exprType = exprUminus.expr.accept(self)
    if type(exprType) is dict:
      exprType = exprType[st.TYPE]
    if(exprType in st.Number):
      return exprType
    else:
      print('ERROR: Invalid unary expression: -',end='')
      exprUminus.expr.accept(self.printer)
      print('')

  def visitExpr_Equals(self, exprEqual):
    type1 = exprEqual.expr1.accept(self)
    type2 = exprEqual.expr2.accept(self)
    
    type1 = isVariable(self, type1)
    type2 = isVariable(self, type2)
    
    if isTypePrimitive(type1) and isTypePrimitive(type2):
      return st.BOOL
    else:
      print('ERROR: Invalid boolean expression: ', end='') 
      exprEqual.expr1.accept(self.printer)
      print(' == ',end='')
      exprEqual.expr2.accept(self.printer)
      print('')
    
  def visitExpr_AssignExpr(self, assignExpr):
    bindable = assignExpr.variable.accept(self)
    exprType = assignExpr.expr.accept(self)
    
    exprType = isVariable(self, exprType)
    
    if exprType == None:
      el.AttributionTypeError(self, assignExpr, exprType)

    st.updateBindableType(bindable[st.NAME], exprType)
  
  def visitExpr_AddAssignExpr(self, assignExpr):
    bindable = assignExpr.variable.accept(self)
    exprType = assignExpr.expr.accept(self)
    
    exprType = isVariable(self, exprType)
    
    if exprType == None:
      el.AttributionTypeError(self, assignExpr, exprType)
      
    if bindable[st.TYPE] not in st.Number:
      el.AttributionInvalidTypeError(self, exprType, assignExpr, bindable)

    st.updateBindableType(bindable[st.NAME], exprType)
    
  def visitExpr_SubAssignExpr(self, subAssignExpr):
    bindable = subAssignExpr.variable.accept(self)
    exprType = subAssignExpr.expr.accept(self)
    
    exprType = getTypeIfVariable(self, exprType)
    
    if exprType == None:
      el.AttributionTypeError(self, subAssignExpr, exprType)
      
    if bindable[st.TYPE] not in st.Number:
      el.AttributionInvalidTypeError(self, exprType, subAssignExpr, bindable)

    st.updateBindableType(bindable[st.NAME], exprType)
    
  def visitExpr_ModAssignExpr(self, modAssignExpr):
    bindable = modAssignExpr.variable.accept(self)
    exprType = modAssignExpr.expr.accept(self)
    
    exprType = getTypeIfVariable(self, exprType)
    
    if exprType == None:
      el.AttributionTypeError(self, modAssignExpr, exprType)
      
    if bindable[st.TYPE] not in st.Number:
      el.AttributionInvalidTypeError(self, exprType, modAssignExpr, bindable)

    st.updateBindableType(bindable[st.NAME], exprType)
    
  def visitExpr_TimesAssignExpr(self, timesAssignExpr):
    bindable = timesAssignExpr.variable.accept(self)
    exprType = timesAssignExpr.expr.accept(self)
    
    exprType = getTypeIfVariable(self, exprType)
    
    if exprType == None:
      el.AttributionTypeError(self, timesAssignExpr, exprType)
      
    if bindable[st.TYPE] not in st.Number:
      el.AttributionInvalidTypeError(self, exprType, timesAssignExpr, bindable)

    st.updateBindableType(bindable[st.NAME], exprType)
    
  def visitExpr_DivideAssignExpr(self, divAssignExpr):
    bindable = divAssignExpr.variable.accept(self)
    exprType = divAssignExpr.expr.accept(self)
    
    exprType = getTypeIfVariable(self, exprType)
    
    if exprType == None:
      el.AttributionTypeError(self, divAssignExpr, exprType)
      
    if bindable[st.TYPE] not in st.Number:
      el.AttributionInvalidTypeError(self, exprType, divAssignExpr, bindable)

    st.updateBindableType(bindable[st.NAME], exprType)
    
  def visitExpr_PreIncrement(self, exprPreIncrement):
    variable = exprPreIncrement.variable.accept(self)
    if variable[st.TYPE] not in st.Number:
      el.IncrementVariableError(variable)

  def visitExpr_PosIncrement(self, exprPosIncrement):
    variable = exprPosIncrement.variable.accept(self)
    if variable[st.TYPE] not in st.Number:
      el.IncrementVariableError(variable)

  def visitExpr_PreDecrement(self, exprPreDecrement):
    variable = exprPreDecrement.variable.accept(self)
    if variable[st.TYPE] not in st.Number:
      el.DecrementVariableError(variable)

  def visitExpr_PosDecrement(self, exprPosDecrement):
    variable = exprPosDecrement.variable.accept(self)
    if variable[st.TYPE] not in st.Number:
      el.DecrementVariableError(variable)
  
  def visitExpr_NumberInt(self, exprNumber):
    return st.INT
  
  def visitExpr_NumberFloat(self, exprNumber):
    return st.FLOAT
  
  def visitExpr_EncapsedString(self, exprEncapsed):
    return st.STRING
  
  def visitExpr_Boolean(self, exprBoolean):
    return st.BOOL
  
  def visitExpr_Variable(self, exprVariable):
    return exprVariable.variable.accept(self)
    
  def visitVariable_Single(self, variable):
    bindable = st.getBindable(variable.token)
    if(bindable == None):
      return st.addVar(variable.token)
    return bindable

  '''
  def visitExpr1_ArrayDeclaration(self, expr1):
    expr1.arrayDeclaration.accept(self)
    return st.ARRAY
  '''
  
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
  
  def visitAssignOperator_Token(self, assignOp):
    return assignOp.token
  
  def visitArrayDec_NoPairList(self, arrayDec):
    return
  
  def visitArrayDec_WithPairList(self, arrayDec):
    arrayDec.arrayPairList.accept(self)
    
  def visitArrayPairList_ArrayPair_Single(self, arrayPairList):
    arrayPairList.arrayPair.accept(self)
    
  def visitArrayPairList_ArrayPair_Mul(self, arrayPairList):
    arrayPairList.arrayPair.accept(self)
    arrayPairList.arrayPairListArrPair.accept(self)
    
  def visitArrayPairList_Mul(self, arrayPairList):
    arrayPairList.arrayPair.accept(self)
    arrayPairList.arrayPairListArr.accept(self)
  
  def visitArrayPairListArr_Single(self, arrayPairList):
    arrayPairList.arrayPair.accept(self)
    
  def visitArrayPair_Expr(self, arrayPair):
    arrayPair.expr.accept(self)

  def visitStatement_Do_While(self, statement):
    statement.dowhilee.accept(self)
  
  def visitDoWhileStatementSingle(self, whilestatement):
    st.beginScope('dowhile')
    whilestatement.statementblockopt.accept(self)
    exprBool = whilestatement.exprparentheses.accept(self)
    st.endScope()

  def visitStatement_For(self, statement):
    statement._for.accept(self)
  
  def visitForStatement_For(self, forStatement):
    st.beginScope('loopfor')
    forStatement.forParameters.accept(self)
    forStatement.statementBlock.accept(self)
    st.endScope()
  
  def visitForParameters_Empty(self):
    return
  
  def visitForParameters_Left(self, forParameters):
    Atribuicao = forParameters.forExprLeft.accept(self)
     
  def visitForParameters_Left_Mid(self, forParameters):
    Atribuicao = forParameters.forExprLeft.accept(self)
    Condicao = forParameters.forExprMid.accept(self)
        
  def visitForParameters_Left_Right(self, forParameters):
    Atribuicao = forParameters.forExprLeft.accept(self)
    Incremento = forParameters.forExprRight.accept(self)
  
  def visitForParameters_Mid(self, forParameters):
    Condicao = forParameters.forExprMid.accept(self)
    
  def visitForParameters_Mid_Right(self, forParameters):
    Condicao = forParameters.forExprMid.accept(self)
    Incremento = forParameters.forExprRight.accept(self)
    
  def visitForParameters_Right(self, forParameters):
    Incremento = forParameters.forExprRight.accept(self)
    
  def visitForParameters_Full(self, forParameters):   
    Atribuicao = forParameters.forExprLeft.accept(self)
    Condicao = forParameters.forExprMid.accept(self)
    Incremento = forParameters.forExprRight.accept(self)
    
  def visitForExprOpt_Mul(self, forExprOpt):
    forExprOpt.forExprOpt.accept(self)
    return forExprOpt.expr.accept(self)
  
  def visitForExprOpt_Single(self, forExprOpt):
    return forExprOpt.expr.accept(self)
  
  def visitForExprColonExpr_Single(self, forExprColonExpr):
    return forExprColonExpr.expr.accept(self)
        
  def visitForExprColonExpr_Mul(self, forExprColonExpr):
    forExprColonExpr.forExprColonExpr.accept(self)
    return forExprColonExpr.expr.accept(self)
  
  def visitStatement_Exit(self, statement):
    statement.exit.accept(self)
  
  def visitExit_ExitExpr(self, _exit):
    _exit.exitExpr.accept(self)
  
  def visitExit_Empty(self):
    return
  
  def visitExitExpr_Expr(self, exitExpr):
    exitExpr.expr.accept(self)
  
  def visitExitExpr_Empty(self):
    return
  
  def visitStatement_Break(self, statement):
    statement._break.accept(self)
  
  def visitBreak_Expr(self, _break):
    return _break.expr.accept(self)
  
  def visitBreak_Empty(self):
    return
  
  def visitStatement_Die(self, statement):
    statement.die.accept(self)
  
  def visitDie_ExitExpr(self, die):
    return die.exitExpr.accept(self)
  
  def visitDie_Empty(self):
    return
