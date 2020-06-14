from AbstractVisitor import AbstractVisitor
import SymbolTable as st
from Visitor import Visitor

import ErrorLog as el

import SintaxeAbstrata as sa

def isValidNumber(number):
    try:
        if(int(number)):
          return st.INT
    except ValueError:
        try:
          if(float(number)):
            return st.FLOAT
        except ValueError:
          return False
      
def isTypePrimitive(type):
  if(type in st.Number or type == st.BOOL or type == st.ARRAY or type == st.STRING):
    return True
  return False

def getTypeIfDict(self, exprType):
  if type(exprType) is dict:
      return exprType[st.TYPE] 
  return exprType

def getTypeExprBool(self,exprBool):
    type1 = exprBool.expr1.accept(self)
    type2 = exprBool.expr2.accept(self)
    return [getTypeIfDict(self, type1),getTypeIfDict(self, type2)]

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
      for i in range(0, len(params), 2):
        st.addVar(params[i], params[i+1])
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
    return [parameter.variable, None]
 
  def visitParameter_Full(self, parameter):
    typePrefix = parameter.prefix.accept(self)
    expr = parameter.expr.accept(self)
    exprType = getTypeIfDict(self,expr)
    if(typePrefix == expr and isTypePrimitive(typePrefix) != False and  isTypePrimitive(exprType)!=False ):
      return [parameter.variable,typePrefix]
    else:
      print('ERROR: Invalid atribution of type', typePrefix, end='') 
      print(' on variable ', parameter.variable ) 
      print(' that has type', exprType)
      return [parameter.variable,None]

  def visitParameter_Prefix_Var(self, parameter):
    parameterPrefix = parameter.prefix.accept(self)
    parameterVariable = parameter.variable
    return [parameterVariable, parameterPrefix ]
  
  def visitParameterPrefix_PType(self, parameterPrefix):
    return parameterPrefix.parameter_type.accept(self)
    
  def visitParameterPrefix_PType_Amp(self, parameterType):
    return parameterType.parameter_type.accept(self)
    
  def visitParameterPrefix_Ampersand(self, parameter):
    pass

  def visitArrayPair_Attr_Expr(self, arrPair):
    expr1 = arrPair.expr1.accept(self)
    expr2 = arrPair.expr2.accept(self)

    exprType = getTypeIfDict(self, expr1)
    if(exprType != st.STRING and exprType not in st.Number):
      print('ERROR: Expected key type of int, float or string, but got type:', exprType)
      return None

  def visitArrayPair_Attr_AmpersandVariable(self, arrPair):
    expr1 = arrPair.expr1.accept(self)
    expr2 = arrPair.expr2.accept(self)

    exprType = getTypeIfDict(self, expr1)
    if(exprType != st.STRING and exprType not in st.Number):
      print('ERROR: Expected key type of int, float or string, but got type:', exprType)
      return None

  def visitArrayPair_Variable(self, arrPair):
    arrPair.variable.accept(self)
  
  def visitParameterType_Type(self, parameterType):
    type = parameterType.type
    if   type == st.INT:
      return st.INT
    elif type == st.FLOAT:
      return st.FLOAT
    elif type == st.STRING:
      return st.STRING
    elif type == st.BOOL:
      return st.BOOL
    elif type == st.ARRAY:
      return st.ARRAY
    
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
    expr1 = exprPlus.expr1.accept(self)
    expr2 = exprPlus.expr2.accept(self)
    
    type1 = getTypeIfDict(self, expr1)
    type2 = getTypeIfDict(self, expr2)    

    if(type1 == st.STRING):
      type1 = isValidNumber(expr1[st.VALUE][1:-1])  
    if(type2 == st.STRING):
      type2 = isValidNumber(expr2[st.VALUE][1:-1])

    c = coercion(type1, type2) 
    if (c == None):
      el.ExpressionTypeError(self, exprPlus, type1, type2)
    return c
    
  def visitExpr_Minus(self, exprMinus):
    expr1 = exprMinus.expr1.accept(self)
    expr2 = exprMinus.expr2.accept(self)
    
    type1 = getTypeIfDict(self, expr1)
    type2 = getTypeIfDict(self, expr2)    

    if(type1 == st.STRING):
      type1 = isValidNumber(expr1[st.VALUE][1:-1])  
    if(type2 == st.STRING):
      type2 = isValidNumber(expr2[st.VALUE][1:-1])

    c = coercion(type1, type2) 
    if (c == None):
      el.ExpressionTypeError(self, exprMinus, type1, type2)
    return c

  def visitExpr_Times(self, exprTimes):
    expr1 = exprTimes.expr1.accept(self)
    expr2 = exprTimes.expr2.accept(self)
    
    type1 = getTypeIfDict(self, expr1)
    type2 = getTypeIfDict(self, expr2)    

    if(type1 == st.STRING):
      type1 = isValidNumber(expr1[st.VALUE][1:-1])  
    if(type2 == st.STRING):
      type2 = isValidNumber(expr2[st.VALUE][1:-1])

    c = coercion(type1, type2) 
    if (c == None):
      el.ExpressionTypeError(self, exprTimes, type1, type2)
    return c

  def visitExpr_Divide(self, exprDivide):
    expr1 = exprDivide.expr1.accept(self)
    expr2 = exprDivide.expr2.accept(self)
    
    type1 = getTypeIfDict(self, expr1)
    type2 = getTypeIfDict(self, expr2)    

    if(type1 == st.STRING):
      type1 = isValidNumber(expr1[st.VALUE][1:-1])  
    if(type2 == st.STRING):
      type2 = isValidNumber(expr2[st.VALUE][1:-1])

    c = coercion(type1, type2) 
    if (c == None):
      el.ExpressionTypeError(self, exprDivide, type1, type2)
    return c
  
  def visitExpr_Mod(self, exprMod):
    expr1 = exprMod.expr1.accept(self)
    expr2 = exprMod.expr2.accept(self)
    
    type1 = getTypeIfDict(self, expr1)
    type2 = getTypeIfDict(self, expr2)    

    if(type1 == st.STRING):
      type1 = isValidNumber(expr1[st.VALUE][1:-1])  
    if(type2 == st.STRING):
      type2 = isValidNumber(expr2[st.VALUE][1:-1])

    c = coercion(type1, type2) 
    if (c == None):
      el.ExpressionTypeError(self, exprMod, type1, type2)
    return c

  def visitExpr_Uminus(self, exprUminus):
    expr1 = exprUminus.expr.accept(self)

    type1 = getTypeIfDict(self, expr1)
    if(type1 == st.STRING):
      type1 = isValidNumber(expr1[st.VALUE][st.VALUE][1:-1])  

    if(type1 in st.Number):
      return expr1
    else:
      print('ERROR: Invalid unary expression: -',end='')
      exprUminus.expr.accept(self.printer)
      print('')

  def visitExpr_Equals(self, exprEqual):
    types = getTypeExprBool(self, exprEqual)
    if isTypePrimitive(types[0]) and isTypePrimitive(types[1]):
      return st.BOOL
    else:
      el.ExpressionBoolError(self,exprEqual," == ", types)

  def visitExpr_NotEqual(self, exprNotEqual):
    types = getTypeExprBool(self, exprNotEqual)
    if isTypePrimitive(types[0]) and isTypePrimitive(types[1]):
      return st.BOOL
    else:
      el.ExpressionBoolError(self, exprNotEqual," != ",types)

  def visitExpr_GreatThan(self, exprGreatThan):
    types = getTypeExprBool(self, exprGreatThan)
    if isTypePrimitive(types[0]) and isTypePrimitive(types[1]):
      return st.BOOL
    else:
      el.ExpressionBoolError(self, exprGreatThan," > ",types)
  
  def visitExpr_GreatEqual(self, exprGreatEqual):
    types = getTypeExprBool(self, exprGreatEqual)
    if isTypePrimitive(types[0]) and isTypePrimitive(types[1]):
      return st.BOOL
    else:
      el.ExpressionBoolError(self, exprGreatEqual," >= ",types)

  def visitExpr_LessThan(self, exprLessThan):
    types = getTypeExprBool(self, exprLessThan)
    if isTypePrimitive(types[0]) and isTypePrimitive(types[1]):
      return st.BOOL
    else:
      el.ExpressionBoolError(self, exprLessThan," < ",types)

  def visitExpr_LessEqual(self, exprLessEqual):
    types = getTypeExprBool(self, exprLessEqual)
    if isTypePrimitive(types[0]) and isTypePrimitive(types[1]):
      return st.BOOL
    else:
      el.ExpressionBoolError(self, exprLessEqual," <= ",types)   
      
  def visitExpr_AndLogical(self, exprAndLogical):
    types = getTypeExprBool(self, exprAndLogical)
    if isTypePrimitive(types[0]) and isTypePrimitive(types[1]):
      return st.BOOL
    else:
      el.ExpressionBoolError(self, exprAndLogical," && ",types)   

  def visitExpr_OrLogical(self, exprOrLogical):
    types = getTypeExprBool(self, exprEqual)
    if isTypePrimitive(types[0]) and isTypePrimitive(types[1]):
      return st.BOOL
    else:
      el.ExpressionBoolError(self, exprOrLogical," || ",types)

  def visitExpr_NotLogical(self, exprNotLogical):
    typeExpr = exprNotLogical.expr.accept(self) 
    if isTypePrimitive(typeExpr):
      return st.BOOL
    else:
     print('ERROR: Expected boolean expression, but got type: !%s'%typeExpr[st.NAME]) 

  def visitExpr_ParenExpr(self, parenExpr):
    parenExpr.expr.accept(self)

  def visitExpr_TernaryOp(self, exprTernary):
    exprTernary.expr1.accept(self)
    exprTernary.expr2.accept(self)
    exprTernary.expr3.accept(self)

  def visitExpr_FunctionCall(self, exprFunctionCall):
    exprFunctionCall.functionCall.accept(self) 
    

  def visitExpr_AssignExpr(self, assignExpr):
    bindable = assignExpr.variable.accept(self)
    expr = assignExpr.expr.accept(self)
    
    if(isinstance(expr, dict) and expr[st.TYPE] == st.STRING):
      if(bindable[st.ISGLOBAL] == True):
        st.updateGlobalBindableType(bindable[st.NAME], expr[st.TYPE], expr[st.VALUE])
      st.updateBindableType(bindable[st.NAME], expr[st.TYPE], expr[st.VALUE])
    else:
      exprType = getTypeIfDict(self, expr)
      if exprType == None:
        expr = getTypeIfDict(self, expr)
      if expr == None:
        el.AttributionTypeError(self, assignExpr, expr)
      if(bindable[st.ISGLOBAL] == True):
        st.updateGlobalBindableType(bindable[st.NAME], exprType)
      st.updateBindableType(bindable[st.NAME], exprType)
  

  def visitExpr_AddAssignExpr(self, assignExpr):
    bindable = assignExpr.variable.accept(self)
    expr = assignExpr.expr.accept(self)
    
    exprType = getTypeIfDict(self, expr)
    exprValue = expr[st.VALUE] if isinstance(expr, dict) else None
    
    if (exprType in st.Number or exprType == st.STRING) and (bindable[st.TYPE] in st.Number or bindable[st.TYPE] == st.STRING):
      if(bindable[st.ISGLOBAL] == True):
        st.updateGlobalBindableType(bindable[st.NAME], exprType, exprValue)
      st.updateBindableType(bindable[st.NAME], exprType, exprValue)
    else:
      el.AttributionInvalidTypeError(self, exprType, assignExpr, bindable)
    
  def visitExpr_SubAssignExpr(self, subAssignExpr):
    bindable = subAssignExpr.variable.accept(self)
    expr = subAssignExpr.expr.accept(self)
    
    exprType = getTypeIfDict(self, expr)
    exprValue = expr[st.VALUE] if isinstance(expr, dict) else None
    
    if (exprType in st.Number or exprType == st.STRING) and (bindable[st.TYPE] in st.Number or bindable[st.TYPE] == st.STRING):
      if(bindable[st.ISGLOBAL] == True):
        st.updateGlobalBindableType(bindable[st.NAME], exprType, exprValue)
      st.updateBindableType(bindable[st.NAME], exprType, exprValue)
    else:
      el.AttributionInvalidTypeError(self, exprType, subAssignExpr, bindable)
    
  def visitExpr_ModAssignExpr(self, modAssignExpr):
    bindable = modAssignExpr.variable.accept(self)
    expr = modAssignExpr.expr.accept(self)
    
    exprType = getTypeIfDict(self, expr)
    exprValue = expr[st.VALUE] if isinstance(expr, dict) else None
    
    if (exprType in st.Number or exprType == st.STRING) and (bindable[st.TYPE] in st.Number or bindable[st.TYPE] == st.STRING):
      if(bindable[st.ISGLOBAL] == True):
        st.updateGlobalBindableType(bindable[st.NAME], exprType, exprValue)
      st.updateBindableType(bindable[st.NAME], exprType, exprValue)
    else:
      el.AttributionInvalidTypeError(self, exprType, modAssignExpr, bindable)

  def visitExpr_TimesAssignExpr(self, timesAssignExpr):
    bindable = timesAssignExpr.variable.accept(self)
    expr = timesAssignExpr.expr.accept(self)
    
    exprType = getTypeIfDict(self, expr)
    exprValue = expr[st.VALUE] if isinstance(expr, dict) else None
    
    if (exprType in st.Number or exprType == st.STRING) and (bindable[st.TYPE] in st.Number or bindable[st.TYPE] == st.STRING):
      if(bindable[st.ISGLOBAL] == True):
        st.updateGlobalBindableType(bindable[st.NAME], exprType, exprValue)
      st.updateBindableType(bindable[st.NAME], exprType, exprValue)
    else:
      el.AttributionInvalidTypeError(self, exprType, timesAssignExpr, bindable)
    
  def visitExpr_DivideAssignExpr(self, divAssignExpr):
    bindable = divAssignExpr.variable.accept(self)
    expr = divAssignExpr.expr.accept(self)
    
    exprType = getTypeIfDict(self, expr)
    exprValue = expr[st.VALUE] if isinstance(expr, dict) else None
    
    if (exprType in st.Number or exprType == st.STRING) and (bindable[st.TYPE] in st.Number or bindable[st.TYPE] == st.STRING):
      if(bindable[st.ISGLOBAL] == True):
        st.updateGlobalBindableType(bindable[st.NAME], exprType, exprValue)
      st.updateBindableType(bindable[st.NAME], exprType, exprValue)
    else:
      el.AttributionInvalidTypeError(self, exprType, divAssignExpr, bindable)
    
  def visitExpr_PreIncrement(self, exprPreIncrement):
    variable = exprPreIncrement.variable.accept(self)
    
    if(variable[st.TYPE]==st.STRING):
      stringFormat = variable[st.VALUE][1:-1]
      validNumber = isValidNumber(stringFormat)  
      if not validNumber in st.Number:
        el.UnaryArithError(self,variable,'increment')
        return
      st.updateBindableType(variable[st.NAME], validNumber)
      return
    elif variable[st.TYPE] not in st.Number:
      el.IncrementVariableError(variable)

  def visitExpr_PosIncrement(self, exprPosIncrement):
    variable = exprPosIncrement.variable.accept(self)

    if(variable[st.TYPE]==st.STRING):
      stringFormat = variable[st.VALUE][1:-1]
      validNumber = isValidNumber(stringFormat)  
      if not validNumber in st.Number:
        el.UnaryArithError(self,variable,'increment')
        return
      st.updateBindableType(variable[st.NAME], validNumber)
      return
    elif variable[st.TYPE] not in st.Number:
      el.IncrementVariableError(variable)

  def visitExpr_PreDecrement(self, exprPreDecrement):
    variable = exprPreDecrement.variable.accept(self)

    if(variable[st.TYPE]==st.STRING):
      stringFormat = variable[st.VALUE][1:-1]
      validNumber = isValidNumber(stringFormat)  
      if not validNumber in st.Number:
        el.UnaryArithError(self,variable,'decrement')
        return
      st.updateBindableType(variable[st.NAME], validNumber)
      return
    elif variable[st.TYPE] not in st.Number:
      el.IncrementVariableError(variable)

  def visitExpr_PosDecrement(self, exprPosDecrement):
    variable = exprPosDecrement.variable.accept(self)

    if(variable[st.TYPE]==st.STRING):
      stringFormat = variable[st.VALUE][1:-1]
      validNumber = isValidNumber(stringFormat)  
      if not validNumber in st.Number:
        el.UnaryArithError(self,variable,'decrement')
        return
      st.updateBindableType(variable[st.NAME], validNumber)
      return
    elif variable[st.TYPE] not in st.Number:
      el.IncrementVariableError(variable)
      
  def visitExpr_ArrayDeclaration(self, exprArrayDecl):
    exprArrayDecl.arrayDecl.accept(self)
    return st.ARRAY
  
  def a(self ):
    pass 

  def visitExpr_TypeCastOp(self, typeCastOp):
    Type = typeCastOp.typeCast.accept(self)
    Expr = typeCastOp.expr.accept(self)
  
  def visitTypeCastOp_Token(self, typeCastOp):
    return typeCastOp.token
  
  def visitExpr_NumberInt(self, exprNumber):
    return st.INT
  
  def visitExpr_NumberFloat(self, exprNumber):
    return st.FLOAT
  
  def visitExpr_EncapsedString(self, exprEncapsed):
    return { st.TYPE: st.STRING, st.VALUE: exprEncapsed.encapsedString }
  
  def visitExpr_Boolean(self, exprBoolean):
    return st.BOOL
  
  def visitExpr_Variable(self, exprVariable):
    return exprVariable.variable.accept(self)
    
  def visitVariable_Single(self, variable):
    bindable = st.getBindable(variable.token)
    if(bindable == None):
      return st.addVar(variable.token)
    return bindable
  
  def visitVariable_Array(self, variable):
    bindable = st.getBindable(variable.token)
    if(bindable == None):
      print('ERROR: Undefined variable', variable.token, '. Trying to access array offset on value of type None')
      return None

    if bindable[st.TYPE] == st.ARRAY or bindable[st.TYPE] == st.STRING:
      variable.selector.accept(self)
    else:
      print('Trying to access array offset on value of type', bindable[st.TYPE])
      
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
    print('single')
    arrayPairList.arrayPair.accept(self)
    
  def visitArrayPair_Expr(self, arrayPair):
    arrayPair.expr.accept(self)
  
  def visitFunctionCall_NoParameter(self, functionCall):
    bindable = st.getBindable(functionCall.id)
    if bindable == None:
      print('ERROR: Function', functionCall.id,'called but never defined.')
      
  def visitFunctionCall_WithParameter(self, functionCall):
    bindable = st.getBindable(functionCall.id)
    st.updateParamsTypes(bindable[st.NAME], 'a')
    if bindable == None:
      print('ERROR: Function', functionCall.id, 'called but never defined.')
    
    if bindable != None and bindable[st.BINDABLE] == st.FUNCTION:
      params = functionCall.parameterList.accept(self)
      if len(params) != (len(bindable[st.PARAMS]) / 2):
        print('ERROR: Number of parameters of function', functionCall.id, 'differs from declaration.')
        
  def visitFCParameterList_Single(self, fcParameterList):
    return fcParameterList.fcParameter.accept(self) 

  def visitFCParameterList_Mul(self, fcParameterList):
    return fcParameterList.fcParameter.accept(self) + fcParameterList.fcColonParameter.accept(self)
    
  def visitFCParameterListColonParameter_Single(self, fcParameterListColonParameter):
    return fcParameterListColonParameter.fcParameter.accept(self)
    
  def visitFCParameterListColonParameter_Mul(self, fcParameterListColonParameter):
    return fcParameterListColonParameter.fcParameter.accept(self) + fcParameterListColonParameter.fcplColonParameter.accept(self)
  
  def visitFunctionCallParameter_Expr(self, functionCallParameter):
    exprType = functionCallParameter.expr.accept(self)
    return [getTypeIfDict(self, exprType)]
    
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
    return arrayPairList.arrayPair.accept(self)
    
  def visitArrayPair_Expr(self, arrayPair):
    return arrayPair.expr.accept(self)
    
  def visitVariableArraySelector_Mul(self, variableArraySelector):
    variableArraySelector.selector.accept(self)
    variableArraySelector.variableArray.accept(self)
  
  def visitVariableArraySelector_Single(self, variableArraySelector):
    variableArraySelector.selector.accept(self)
  
  def visitSelectorWithExpr(self, selector):
    exprType = selector.expr.accept(self)
    
    exprType = getTypeIfDict(self, exprType) 
    
    if exprType != st.INT and exprType != st.STRING:
      print('ERROR: Trying to access array offset with type', exprType, end='')
      print('. Valid types are int and string')
  
  def visitSelectorWithoutExpr(self, selector):
    return 

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

  def visitStatement_Foreach(self, statement):
    statement.foreach.accept(self)
  
  def visitForeachStatement_NoAssoc(self, foreachStatement):
    varArray = foreachStatement.expr.accept(self)
    valor = foreachStatement.ampVariable.accept(self)
    foreachStatement.statementBlockOpt.accept(self)

    if varArray[st.TYPE] != st.ARRAY:
     print('ERROR: Expected a array declaration, but got type:', varArray[st.TYPE], end='')
     foreachStatement.expr.accept(self.printer, '\n')

  def visitForeachStatement_WithAssoc(self, foreachStatement):
    varArray = foreachStatement.expr.accept(self)
    chaveArray = foreachStatement.ampVariableKey.accept(self)
    valorChaveArray = foreachStatement.ampVariableValue.accept(self)
    foreachStatement.statementBlockOpt.accept(self)
    if varArray[st.TYPE] != st.ARRAY:
     print('ERROR: Expected a array declaration, but got type:', varArray[st.TYPE], end=' ')
     foreachStatement.expr.accept(self.printer)
     print('')

  
  def visitAmpersandVariable_WithAmp(self, ampersandVariable):
    bindable = st.getBindable(ampersandVariable.variable_token)
    if bindable == None:
      print('ERROR: Foreach', ampersandVariable.variable_token,'variable never defined.')
    else:
      return st.addVar(bindable)
  
  def visitAmpersandVariable_NoAmp(self, ampersandVariable):
    bindable = ampersandVariable.variable_token
    if bindable == None:
      print('ERROR: Foreach', ampersandVariable.variable_token,'variable never defined.')
    else:
      return st.addVar(bindable)
    
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

  def visitStatement_Continue(self, statement):
    statement._continue.accept(self)
  
  def visitContinue_Expr(self, _continue):
    return _continue.expr.accept(self)
  
  def visitContinue_Empty(self):
    return
  
  def visitStatement_Return(self, statement):
    statement._return.accept(self)
  
  def visitReturn_Expr(self, _return):
    return _return.expr.accept(self)

  def visitReturn_Empty(self):
    return
  
  def visitStatement_Global(self, statement):
    globalvar = statement._global.accept(self)
    
  def visitGlobalStatement_Single(self, globalStatement):
    return globalStatement.globalVar.accept(self)
  
  def visitGlobalVar_Var(self, globalVar):
    bindable = st.getGlobalBindable(globalVar.variable)
    if(bindable == None):
      print('ERROR: Global variable', globalVar.variable, 'called but never defined in global scope.')
      return st.addVar(globalVar.variable)
    else:
      return st.addVar(bindable[st.NAME], bindable[st.TYPE], bindable[st.ISGLOBAL], bindable[st.VALUE])

  def visitGlobalStatement_Mul(self, globalStatement):
    globalStatement.globalVar.accept(self)
    globalStatement.colonGlobal.accept(self)

  def visitGlobalVarMul_Single(self, globalVarMul):
    globalVarMul.globalVar.accept(self)
  
  def visitGlobalVarMul_Mul(self, globalVarMul):
    globalVarMul.globalVar.accept(self) 
    globalVarMul.globalVarMul.accept(self)
    
  def visitStatementBlockOpt_Empty(self, statementblockopt):
    return