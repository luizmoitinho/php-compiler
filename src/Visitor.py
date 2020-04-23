class Visitor():

  def visitMain_MainInner(self, main):
    print('<?php')
    main.mainInner.accept(self)
    print('?>')
  
  def visitMain_MainInner_Empty(self, main):
    print('<?php', end=' ')
    print('?>', end=' ')
    
  def visitMainInner_InnerStatement_MainInner(self, mainInner):
    mainInner.innerStatement.accept(self)
    mainInner.mainInner.accept(self)
    
  def visitMainInner_InnerStatement(self, mainInner):
    mainInner.innerStatement.accept(self)

  def visitInnerStatement_Statement(self, innerStatement):
    innerStatement.statement.accept(self)
    
  def visitInnerStatement_FuncDecStatement(self, innerStatement):
    innerStatement.funcDecStatement.accept(self)
    
  def visitInnerStatementMul_Mul(self, innerStatementMul):
    innerStatementMul.innerStatement.accept(self)
    innerStatementMul.innerStatementMul.accept(self)
    
  def visitInnerStatementMul_Single(self, innerStatementMul):
    innerStatementMul.innerStatement.accept(self)
    
  def visitFuncDecStatement_Function(self, funcDecStatement):
    print('function', end=' ')
    funcDecStatement.fds_id.accept(self)
    funcDecStatement.fds_parameter.accept(self)
    funcDecStatement.fds_statements.accept(self)
    
  def visitFds_id_withAmpersand(self, fds_id):
    print('&', end='')
    print(fds_id.id)
    
  def visitFds_id_noAmpersand(self, fds_id):
    print(fds_id.id, end='')
    
  def visitFds_parameter_withParameter(self, fds_parameter):
    print('(', end='')
    fds_parameter.parameter_list.accept(self)
    print(')', end='')
    
  def visitFds_parameter_noParameter(self, fds_parameter):
    print('(', end='')
    print(')', end='')
    
  def visitFds_statements_withStatements(self, fds_statements):
    print('{')
    fds_statements.inner_statement_MUL.accept(self)
    print('}')
    
  def visitFds_statements_noStatements(self, fds_statements):
    print('{')
    print('}')
    
  def visitParameterList_Parameter_Mul(self, parameterList):
    parameterList.parameter.accept(self)
    parameterList.parameter_list_colon_parameter.accept(self)
    
  def visitParameterList_Parameter_Single(self, parameterList):
    parameterList.parameter.accept(self)
    
  def visitParameterListColonParameter_Mul(self, parameterListColonParameter):
    print(',', end=' ')
    parameterListColonParameter.parameter.accept(self)
    parameterListColonParameter.parameterListColonParameter.accept(self)
    
  def visitParameterListColonParameter_Single(self, parameterListColonParameter):
    print(',', end=' ')
    parameterListColonParameter.parameter.accept(self)
  
  def visitParameter_Var(self, parameter):
    print(parameter.variable, end='')
    
  def visitParameter_Prefix_Var(self, parameter):
    parameter.prefix.accept(self)
    print(parameter.variable, end='')
    
  def visitParameter_Var_Sufix(self, parameter):
    print(parameter.variable, end='')
    print('=', end='')
    parameter.static_scalar.accept(self)
  
  def visitParameter_Full(self, parameter):
    parameter.prefix.accept(self)
    print(parameter.variable, end='')
    print('=', end='')
    parameter.static_scalar.accept(self)
  
  def visitParameterPrefix_PType_Amp(self, parameterPrefix):
    parameterPrefix.parameter_type.accept(self)
    print('&', end='')
    
  def visitParameterPrefix_Ampersand(self, parameterPrefix):
    print('&', end='')
    
  def visitParameterPrefix_PType(self, parameterPrefix):
    parameterPrefix.parameter_type.accept(self)
    
  def visitParameterType_Type(self, parameterType):
    print(parameterType.type, end=' ')
    
  def visitStaticScalar_CommonScalar(self, staticScalar):
    staticScalar.common_scalar.accept(self)
  
  def visitStaticScalar_Plus_Static(self, staticScalar):
    print('+', end='')
    staticScalar.static_scalar.accept(self)
    
  def visitStaticScalar_Minus_Static(self, staticScalar):
    print('-', end='')
    staticScalar.static_scalar.accept(self)
    
  def visitCommonScalar_Token(self, commonScalar):
    print(commonScalar.token, end='')
    
  def visitScalar_Token(self, scalar):
    print(scalar.token, end='')
  
  def visitStatement_Expr(self, statement):
    statement.expr.accept(self)
    print(';')
    
  def visitStatement_Break(self, statement):
    statement._break.accept(self)
    
  def visitStatement_Continue(self, statement):
    statement._continue.accept(self)
    
  def visitStatement_Return(self, statement):
    statement._return.accept(self)
    
  def visitStatement_Exit(self, statement):
    statement.exit.accept(self)
    print(';')
    
  def visitStatement_Die(self, statement):
    statement.die.accept(self)
    print(';')
    
  def visitExpr_Expr1_Expr2(self, expr):
    expr.expr1.accept(self)
    expr.expr2.accept(self)

  def visitExpr_Expr1(self, expr):
    expr.expr1.accept(self)
    
  def visitExpr_Expr3(self, expr):
    expr.expr3.accept(self)

  def visitExpr3_TypeCast(self, expr3):
    print('(', end='')
    expr3.typeCast.accept(self)
    print(')', end=' ')
    expr3.expr.accept(self)
    
  def visitTypeCastOp_Token(self, typeCastOp):
    print(typeCastOp.token, end='')

  def visitExpr1_FunctionCall(self, expr1):
    expr1.functionCall.accept(self)
    
  def visitExpr1_ExprPar(self, expr1):
    print('(', end='')
    expr1.expr.accept(self)
    print(')', end='')
    
  def visitExpr1_Variable_Increment(self, expr1):
    expr1.variable.accept(self)
    print('++', end='')
    
  def visitExpr1_Variable(self, expr1):
    expr1.variable.accept(self)

  def visitExpr1_ArrayDeclaration(self, expr1):
    print('array', end='')
    expr1.arrayDeclaration.accept(self)

  def visitArrayDec_WithPairList(self, arrayDec):
    print('(',end='')
    arrayDec.arrayPairList.accept(self)
    print(')',end='')

  def visitArrayDec_NoPairList(self, ArrayDec):
    print('( )',end='')
    
  def visitArrayPair_Expr(self, arrayPair):
    arrayPair.expr.accept(self)
  
  def visitArrayPairList_Mul(self, arrayPairList):
    print(',',end='')
    arrayPairList.arrayPair.accept(self)
    arrayPairList.arrayPairListArr.accept(self)
  
  def visitArrayPairListArr_Single(self,ArrayPairListArr):
    print(',',end='')
    ArrayPairListArr.arrayPair.accept(self)

  def visitArrayPairList_ArrayPair_Mul(self, arrayPairList):
    arrayPairList.arrayPair.accept(self)
    arrayPairList.arrayPairListArrPair.accept(self)
  
  def visitArrayPairList_ArrayPair_Single(self, arrayPairList):
    arrayPairList.arrayPair.accept(self)

  def visitArrayPair_Variable(self, arrayPair):
    print('&', end='')
    arrayPair.variable.accept(self)

  def visitArrayPair_Attr_AmpersandVariable(self, arrayPair):
    arrayPair.expr1.accept(self)
    print('=',end='')
    print('&',end='')
    arrayPair.expr2.accept(self)

  def visitArrayPair_Attr_Expr(self, arrayPair):
    arrayPair.expr1.accept(self)
    print('=', end='')
    arrayPair.expr2.accept(self)

  def visitExpr1_Scalar(self, expr1):
    expr1.scalar.accept(self)
  
  def visitExpr1_True(self, expr1):
    print('true', end='')
    
  def visitExpr1_False(self, expr1):
    print('false', end='')
    
  def visitFunctionCall_NoParameter(self, functionCall):
    print(functionCall.id, '()')
    
  def visitFunctionCall_WithParameter(self, functionCall):
    print(functionCall.id, end='')
    print('(', end='')
    functionCall.parameterList.accept(self)
    print(')', end='')
    
  def visitFCParameterList_Single(self, fcParameterList):
    fcParameterList.fcParameter.accept(self) 

  def visitFCParameterList_Mul(self, fcParameterList):
    fcParameterList.fcParameter.accept(self)
    fcParameterList.fcColonParameter.accept(self)
    
  def visitFCParameterListColonParameter_Single(self, fcParameterListColonParameter):
    print(',', end='')
    fcParameterListColonParameter.fcParameter.accept(self)
    
  def visitFCParameterListColonParameter_Mul(self, fcParameterListColonParameter):
    print(',', end='')
    fcParameterListColonParameter.fcParameter.accept(self)
    fcParameterListColonParameter.fcplColonParameter.accept(self)
    
  def visitFunctionCallParameter_Expr(self, functionCallParameter):
    functionCallParameter.expr.accept(self)
    
  def visitFunctionCallParameter_AmpersandVariable(self, functionCallParameter):
    print('&', end='')
    print(functionCallParameter.variable, end='')
  
  def visitVariable_Reference_Variable(self, variable):
    variable.reference_variable.accept(self)

  def visitVariable_Simple_Indirect(self, variable):
    variable.simple_indirect.accept(self)
    variable.reference_variable.accept(self)

  def visitReferenceVariable_Compound_Reference(self, referenceVariable):
    referenceVariable.compoundvariable.accept(self)
    referenceVariable.referencevariableSELECTOR.accept(self)
  
  def visitReferenceVariable_Compound(self, referenceVariable):
    referenceVariable.compoundvariable.accept(self)
  
  def visitSimpleIndirectReference_Mul(self, simpleIndirectReference):
    print('$', end='')
    simpleIndirectReference.simpleindirect.accept(self)
  
  def visitSimpleIndirectReference_Single(self, simpleIndirectReference):
    print('$', end='')
    
  def visitExit_ExitExpr(self, _exit):
    print('exit', end='')
    _exit.exitExpr.accept(self)
    
  def visitExit_Empty(self):
    print('exit', end='')
    
  def visitDie_ExitExpr(self, die):
    print('die', end='')
    die.exitExpr.accept(self)
  
  def visitDie_Empty(self):
    print('die', end='')

  def visitExitExpr_Expr(self, exitExpr):
    print('(', end='')
    exitExpr.expr.accept(self)
    print(')', end='')

  def visitExitExpr_Empty(self):
    print('()', end='')

  def visitBreak_Expr(self, _break):
    print('break', end=' ')
    _break.expr.accept(self)
    print(';')

  def visitBreak_Empty(self):
    print('break', end='')
    print(';')

  def visitContinue_Expr(self, _continue):
    print('continue', end=' ')
    _continue.expr.accept(self)
    print(';')
    
  def visitContinue_Empty(self):
    print('continue', end='')
    print(';')
    
  def visitReturn_Expr(self, _return):
    print('return', end=' ')
    _return.expr.accept(self)
    print(';')
    
  def visitReturn_Empty(self):
    print('return', end='')
    print(';')

  def visitCompoundVariableSingle(self, singleVariable):
    print(singleVariable.variable, end='')
    
  def visitCompoundVariableMul(self, compoundVariable):
      print('$', end='')
      print('{', end='')
      compoundVariable.expr.accept(self)
      print('}', end='')

  def visitReferenceVariableSelectorSingle(self, referenceVariableSelector):
      referenceVariableSelector.selector.accept(self)

  def visitReferenceVariableSelectorMul(self, referenceVariableSelector):
      referenceVariableSelector.selector.accept(self)
      referenceVariableSelector.referencevariableselector.accept(self)

  def visitSelectorWithExpr(self, selector):
      print('[', end='')
      selector.expr.accept(self)
      print(']', end='')

  def SelectorWithoutExpr(self, selector):
      print('[', end='')
      print(']', end='')
