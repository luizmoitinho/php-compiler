from AbstractVisitor import AbstractVisitor
from PrettyPrinter import PrettyPrinter as pp

class Visitor(AbstractVisitor):

  def visitMain_MainProgram(self, main):
    print('<?php')
    pp.incrementTab()
    main.mainInner.accept(self)
    print('?>')
  
  def visitMain_Empty(self):
    print('<?php', end=' ')
    print('?>', end=' ')
    
  def visitMainProgram_InnerStatement_Recursive(self, mainInner):
    mainInner.innerStatement.accept(self)
    mainInner.mainInner.accept(self)
    
  def visitMainProgram_InnerStatement(self, mainInner):
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
    pp.printTab()
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
    
  def visitFds_parameter_noParameter(self):
    print('(', end='')
    print(')', end='')
    
  def visitFds_statements_withStatements(self, fds_statements):
    print('{')
    pp.incrementTab()
    fds_statements.inner_statement_MUL.accept(self)
    pp.decrementTab()
    pp.printTab()
    print('}')
    
  def visitFds_statements_noStatements(self, fds_statements):
    print('{')
    pp.printTab()
    print('}')
  
  def visitStatementMul_Mul(self, StatementMul):
    StatementMul.statement.accept(self)
    StatementMul.statementMul.accept(self)

  def visitStatementMul_Single(self, StatementMul):
    StatementMul.statement.accept(self)

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
    parameter.expr.accept(self)
  
  def visitParameterPrefix_PType_Amp(self, parameterPrefix):
    parameterPrefix.parameter_type.accept(self)
    print('&', end='')
    
  def visitParameterPrefix_Ampersand(self, parameterPrefix):
    print('&', end='')
    
  def visitParameterPrefix_PType(self, parameterPrefix):
    parameterPrefix.parameter_type.accept(self)
    
  def visitParameterType_Type(self, parameterType):
    print(parameterType.type, end=' ')
    

  
  def visitStatement_Expr(self, statement):
    pp.printTab()
    statement.expr.accept(self)
    print(';')
    
  def visitStatement_Break(self, statement):
    pp.printTab()
    statement._break.accept(self)
    
  def visitStatement_Continue(self, statement):
    pp.printTab()
    statement._continue.accept(self)
    
  def visitStatement_Return(self, statement):
    pp.printTab()
    statement._return.accept(self)
  
  def visitStatement_Exit(self, statement):
    pp.printTab()
    statement.exit.accept(self)
    print(';')
  
  def visitStatement_While(self, statement):
    pp.printTab()
    statement.whilee.accept(self)
  
  def visitStatement_Do_While(self, statement):
    pp.printTab()
    statement.dowhilee.accept(self)
    print(';')

  def visitStatement_Foreach(self, statement):
    pp.printTab()
    statement.foreach.accept(self)

  def visitStatement_Die(self, statement):
    pp.printTab()
    statement.die.accept(self)
    print(';')
    
  def visitStatement_Global(self, statement):
    pp.printTab()
    statement._global.accept(self)
    print(';')
    
  def visitStatement_For(self, statement):
    pp.printTab()
    statement._for.accept(self)

  def visitExprParentheses_Expr(self, exprParentheses_Expr):
    print('(',end='')
    exprParentheses_Expr.expr.accept(self)
    print(')',end='')
   
  def visitTypeCastOp_Token(self, typeCastOp):
    print(typeCastOp.token, end='')
    
  def visitAssignOperator_Token(self, assignOp):
    print('',assignOp.token, end=' ')

  def visitArrayDec_WithPairList(self, arrayDec):
    print('(',end='')
    arrayDec.arrayPairList.accept(self)
    print(')',end='')

  def visitArrayDec_NoPairList(self, ArrayDec):
    print('()',end='')
    
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
    print('=>',end='')
    print('&',end='')
    arrayPair.expr2.accept(self)

  def visitArrayPair_Attr_Expr(self, arrayPair):
    arrayPair.expr1.accept(self)
    print('=', end='')
    arrayPair.expr2.accept(self)
    
  def visitFunctionCall_NoParameter(self, functionCall):
    print(functionCall.id, end='')
    print('()', end='')
    
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
  
  def visitVariable_Single(self, variable):
    print(variable.token, end='')
    
  def visitVariable_Array(self, variable):
    print(variable.token, end='')
    variable.selector.accept(self)
    
  def visitAmpersandVariable_WithAmp(self, ampersandVariable):
    print('&', end='')
    print(ampersandVariable.variable_token, end='')
    
  def visitAmpersandVariable_NoAmp(self, ampersandVariable):
    print(ampersandVariable.variable_token, end='')
    
  def visitForStatement_For(self, forStatement):
    print('for', end='')
    print('(', end='')
    forStatement.forParameters.accept(self)
    print(')', end='')
    forStatement.statementBlock.accept(self)
    
  def visitForParameters_Empty(self):
    print(';;', end='')
    
  def visitForParameters_Left(self, forParameters):
    forParameters.forExprLeft.accept(self)
    print(';;',end='')
  
  def visitForParameters_Left_Mid(self, forParameters):
    forParameters.forExprLeft.accept(self)
    print(';', end=' ')
    forParameters.forExprMid.accept(self)
    print(';', end='')
    
  def visitForParameters_Left_Right(self, forParameters):
    forParameters.forExprLeft.accept(self)
    print(';', end='')
    print(';', end=' ')
    forParameters.forExprRight.accept(self)
  
  def visitForParameters_Mid(self, forParameters):
    print(';', end=' ')
    forParameters.forExprMid.accept(self)
    print(';', end='')
    
  def visitForParameters_Mid_Right(self, forParameters):
    print(';', end=' ')
    forParameters.forExprMid.accept(self)
    print(';', end=' ')
    forParameters.forExprRight.accept(self)
    
  def visitForParameters_Right(self, forParameters):
    print(';;', end=' ')
    forParameters.forExprRight.accept(self)
    
  def visitForParameters_Full(self, forParameters):
    forParameters.forExprLeft.accept(self)
    print(';', end=' ')
    forParameters.forExprMid.accept(self)
    print(';', end=' ')
    forParameters.forExprRight.accept(self)

  def visitForExprOpt_Single(self, forExprOpt):
    forExprOpt.expr.accept(self)
    
  def visitForExprOpt_Mul(self, forExprOpt):
    forExprOpt.expr.accept(self)
    forExprOpt.forExprOpt.accept(self)
    
  def visitForExprColonExpr_Single(self, forExprColonExpr):
    print(',', end=' ')
    forExprColonExpr.expr.accept(self)
    
  def visitForExprColonExpr_Mul(self, forExprColonExpr):
    print(',', end=' ')
    forExprColonExpr.expr.accept(self)
    forExprColonExpr.forExprColonExpr.accept(self)
    
  def visitGlobalStatement_Single(self, globalStatement):
    print('global', end=' ')
    globalStatement.globalVar.accept(self)
    
  def visitGlobalStatement_Mul(self, globalStatement):
    print('global', end=' ')
    globalStatement.globalVar.accept(self)
    globalStatement.colonGlobal.accept(self)
    
  def visitGlobalVar_Var(self, globalVar):
    print(globalVar.variable, end='')
    
  def visitGlobalVarMul_Single(self, globalVarMul):
    print(',', end=' ')
    globalVarMul.globalVar.accept(self)
  
  def visitGlobalVarMul_Mul(self, globalVarMul):
    print(',', end=' ')
    globalVarMul.globalVar.accept(self)
    globalVarMul.globalVarMul.accept(self)
    
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
    
  def visitVariableArraySelector_Mul(self, variableArraySelector):
    variableArraySelector.selector.accept(self)
    variableArraySelector.variableArray.accept(self)
    
  def visitVariableArraySelector_Single(self, variableArraySelector):
    variableArraySelector.selector.accept(self)

  def visitSelectorWithExpr(self, selector):
      print('[', end='')
      selector.expr.accept(self)
      print(']', end='')

  def visitSelectorWithoutExpr(self, selector):
      print('[', end='')
      print(']', end='')
      
  def visitForeachStatement_NoAssoc(self, foreachStatement):
    print('foreach', end='')
    print('(', end='')
    foreachStatement.expr.accept(self)
    print('', 'as', end=' ')
    foreachStatement.ampVariable.accept(self)
    print(')', end='')
    foreachStatement.statementBlockOpt.accept(self)
    
  def visitForeachStatement_WithAssoc(self, foreachStatement):
    print('foreach', end='')
    print('(', end='')
    foreachStatement.expr.accept(self)
    print('', 'as', end=' ')
    foreachStatement.ampVariableKey.accept(self)
    print('', '=>', end=' ')
    foreachStatement.ampVariableValue.accept(self)
    print(')', end='')
    foreachStatement.statementBlockOpt.accept(self)

  def visitWhileStatementSingle(self, whilestatement):
      print('while', end='')
      whilestatement.exprparentheses.accept(self)
      whilestatement.statement.accept(self)
  
  def visitStatementBlockOpt_Statement(self, statementblockopt):
      print()
      pp.incrementTab()
      statementblockopt.statement.accept(self)
      pp.decrementTab()
  
  def visitStatementBlockOpt_StatementMul(self, statementBlockOpt):
      print('{')
      pp.incrementTab()
      statementBlockOpt.statementmul.accept(self)
      pp.decrementTab()
      pp.printTab()
      print('}')
  
  def visitStatementBlockOpt_Empty(self, statementblockopt):
      print('{')
      pp.printTab()
      print('}')
  
  def visitstatementMulSingle(self, statementMul):
      statementMul.statement.accept(self)
  
  def visitstatementMulMul(self, statementMul):
      statementMul.statement.accept(self)
      statementMul.statementMul.accept(self)
  
  def visitDoWhileStatementSingle(self, whilestatement):
      print('do', end='')
      whilestatement.statementblockopt.accept(self)
      pp.printTab()
      print('while', end='')
      whilestatement.exprparentheses.accept(self)

  # ============== NOVAS REGRAS =============================
  def visitExpr_Plus(self, exprPlus):
    exprPlus.expr1.accept(self)
    print(' + ', end='')
    exprPlus.expr2.accept(self)
  
  def visitExpr_Minus(self, exprMinus):
    exprMinus.expr1.accept(self)
    print(' - ', end='')
    exprMinus.expr2.accept(self)
    
  def visitExpr_Uminus(self, exprUminus):
    print('-', end='')
    exprUminus.expr.accept(self)

  def visitExpr_Times(self, exprTimes):
    exprTimes.expr1.accept(self)
    print(' * ', end='')
    exprTimes.expr2.accept(self)

  def visitExpr_Divide(self, exprDivide):
    exprDivide.expr1.accept(self)
    print(' / ', end='')
    exprDivide.expr2.accept(self)

  def visitExpr_Mod(self, exprMod):
    exprMod.expr1.accept(self)
    print(' % ', end='')
    exprMod.expr2.accept(self)

  def visitExpr_Equals(self, exprEqual):
    exprEqual.expr1.accept(self)
    print(' == ', end='')
    exprEqual.expr2.accept(self) 

  def visitExpr_NotEqual(self, exprNotEqual):
    exprNotEqual.expr1.accept(self)
    print(' != ', end='')
    exprNotEqual.expr2.accept(self) 

  def visitExpr_GreatThan(self, exprGreatThan):
    exprGreatThan.expr1.accept(self)
    print(' > ', end='')
    exprGreatThan.expr2.accept(self) 

  def visitExpr_GreatEqual(self, exprGreatEqual):
    exprGreatEqual.expr1.accept(self)
    print(' >= ', end='')
    exprGreatEqual.expr2.accept(self) 

  def visitExpr_LessThan(self, exprLessThan):
    exprLessThan.expr1.accept(self)
    print(' < ', end='')
    exprLessThan.expr2.accept(self) 

  def visitExpr_LessEqual(self, exprLessEqual):
    exprLessEqual.expr1.accept(self)
    print(' <= ', end='')
    exprLessEqual.expr2.accept(self) 

  def visitExpr_AndLogical(self, exprAndLogical):
    exprAndLogical.expr1.accept(self)
    print(' && ', end='')
    exprAndLogical.expr2.accept(self) 

  def visitExpr_OrLogical(self, exprOrLogical):
    exprOrLogical.expr1.accept(self)
    print(' || ', end='')
    exprOrLogical.expr2.accept(self) 
    
  def visitExpr_NotLogical(self, exprNotLogical):
    print('!', end='')
    exprNotLogical.expr.accept(self)

  def visitExpr_PreIncrement(self, exprPreIncrement):
    print('++',end='')
    exprPreIncrement.variable.accept(self)
  
  def visitExpr_PosIncrement(self, exprPosIncrement):
    exprPosIncrement.variable.accept(self)
    print('++',end='')

  def visitExpr_PreDecrement(self, exprPreDecrement):
    print('--',end='')
    exprPreDecrement.variable.accept(self)
  
  def visitExpr_PosDecrement(self, exprPosDecrement):
    exprPosDecrement.variable.accept(self)
    print('--',end='')

  def visitExpr_Variable(self, exprVariable):
    exprVariable.variable.accept(self)

  def visitExpr_ParenExpr(self, parenExpr):
    print('(',end='')
    parenExpr.expr.accept(self)
    print(')',end='')
  
  def visitExpr_ArrayDeclaration(self, exprArrayDecl):
    print('array', end='')
    exprArrayDecl.arrayDecl.accept(self)

  def visitExpr_FunctionCall(self, exprFunctionCall):
    exprFunctionCall.functionCall.accept(self)

  def visitExpr_Boolean(self,exprBoolean):
    print(exprBoolean.token, end='')
  
  def visitExpr_TernaryOp(self, exprTernary):
    exprTernary.expr1.accept(self)
    print(' ? ',end='')
    exprTernary.expr2.accept(self)
    print(' : ',end='')
    exprTernary.expr3.accept(self)  
  
  def visitExpr_AssignExpr(self, assignExpr):
    assignExpr.variable.accept(self)
    print(' = ',end='')
    assignExpr.expr.accept(self)

  def visitExpr_AddAssignExpr(self, addAssignExpr):
    addAssignExpr.variable.accept(self)
    print(' += ',end='')
    addAssignExpr.expr.accept(self)

  def visitExpr_SubAssignExpr(self, subAssignExpr):
    subAssignExpr.variable.accept(self)
    print(' -= ',end='')
    subAssignExpr.expr.accept(self)
  
  def visitExpr_ModAssignExpr(self, modAssignExpr):
    modAssignExpr.variable.accept(self)
    print(' %= ',end='')
    modAssignExpr.expr.accept(self)

  def visitExpr_DivideAssignExpr(self, divAssignExpr):
    divAssignExpr.variable.accept(self)
    print(' /= ',end='')
    divAssignExpr.expr.accept(self)

  def visitExpr_TimesAssignExpr(self, timesAssignExpr):
    timesAssignExpr.variable.accept(self)
    print(' *= ',end='')
    timesAssignExpr.expr.accept(self)

  def visitExpr_TypeCastOp(self, typeCastOp):
    print('(',end='')
    typeCastOp.typeCast.accept(self)
    print(') ',end='')
    typeCastOp.expr.accept(self)

  def visitExpr_NumberInt(self, exprNumber):
    print(exprNumber.numberInt,end='')

  def visitExpr_NumberFloat(self, exprNumber):
    print(exprNumber.numberFloat,end='')

  def visitExpr_EncapsedString(self, exprEncapsed):
    print(exprEncapsed.encapsedString,end='')
