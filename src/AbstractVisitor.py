from abc import abstractmethod
from abc import ABCMeta

class AbstractVisitor(metaclass = ABCMeta):
  
  @abstractmethod
  def visitMain_MainProgram(self, main):
    pass
  
  @abstractmethod
  def visitMain_Empty(self):
    pass
  
  @abstractmethod
  def visitMainProgram_InnerStatement_Recursive(self):
    pass
  
  @abstractmethod
  def visitMainProgram_InnerStatement(self, mainInner):
    pass
  
  @abstractmethod
  def visitInnerStatement_FuncDecStatement(self, innerStatement):
    pass
  
  @abstractmethod
  def visitInnerStatement_Statement(self, innerStatement):
    pass
  
  @abstractmethod
  def visitFuncDecStatement_Function(self, funcDecStatement):
    pass

  @abstractmethod
  def visitFds_id_withAmpersand(self, fds_id):
    pass
  
  @abstractmethod
  def visitFds_id_noAmpersand(self, fds_id):
    pass
  
  @abstractmethod
  def visitFds_parameter_withParameter(self, fds_parameter):
    pass
  
  @abstractmethod
  def visitFds_parameter_noParameter(self):
    pass
  
  @abstractmethod
  def visitParameterList_Parameter_Mul(self, parameterList):
    pass
  
  @abstractmethod
  def visitParameterList_Parameter_Single(self, parameterList):
    pass
  
  @abstractmethod
  def visitParameterListColonParameter_Mul(self, parameterListColonParameter):
    pass
  
  @abstractmethod
  def visitParameterListColonParameter_Single(self, parameterListColonParameter):
    pass
  
  @abstractmethod
  def visitFds_statements_withStatements(self, fds_statements):
    pass
  
  @abstractmethod
  def visitFds_statements_noStatements(self):
    pass
  
  @abstractmethod
  def visitParameter_Var(self, parameter):
    pass
  
  @abstractmethod
  def visitInnerStatementMul_Mul(self, innerStatementMul):
    pass
  
  @abstractmethod
  def visitInnerStatementMul_Single(self, innerStatementMul):
    pass

  # ================ P_EXPR ===============================
  
  @abstractmethod
  def visitStatement_Expr(self, statement):
    pass
  
  @abstractmethod
  def visitExpr_Plus(self, exprPlus):
    pass

  @abstractmethod
  def visitExpr_Minus(self, exprMinus):
    pass
  
  @abstractmethod
  def visitExpr_Uminus(self, exprUminus):
    pass
  
  @abstractmethod
  def visitExpr_Times(self, exprTimes):
    pass

  @abstractmethod  
  def visitExpr_Divide(self, exprDivide):
    pass
  
  @abstractmethod
  def visitExpr_Equals(self, exprEqual):
    pass

  @abstractmethod
  def visitExpr_NotEqual(self, exprNotEqual):
    pass

  @abstractmethod
  def visitExpr_GreatThan(self, exprGreatThan):
    pass

  @abstractmethod
  def visitExpr_GreatEqual(self, exprGreatEqual):
    pass

  @abstractmethod
  def visitExpr_LessThan(self, exprLessThan):
    pass

  @abstractmethod
  def visitExpr_LessEqual(self, exprLessEqual):
    pass
  
  @abstractmethod
  def visitExpr_AndLogical(self, exprAndLogical):
    pass
  
  @abstractmethod
  def visitExpr_OrLogical(self, exprOrLogical):
    pass
  
  
  @abstractmethod
  def visitExpr_NotLogical(self, exprOrLogical):
    pass
    
  @abstractmethod
  def visitExpr_ParenExpr(self, parenExpr):
    pass

  @abstractmethod
  def visitExpr_PreIncrement(self, exprPreIncrement):
    pass

  @abstractmethod
  def visitExpr_PosIncrement(self, exprPosIncrement):
    pass

  @abstractmethod
  def visitExpr_PreDecrement(self, exprPreDecrement):
    pass

  @abstractmethod
  def visitExpr_PosDecrement(self, exprPosDecrement):
    pass

  @abstractmethod
  def visitExpr_AssignExpr(self, assignExpr):
    pass
  
  @abstractmethod
  def visitExpr_AddAssignExpr(self, assignExpr):
    pass
  
  @abstractmethod
  def visitExpr_SubAssignExpr(self, subAssignExpr):
    pass
  
  @abstractmethod
  def visitExpr_ModAssignExpr(self, modAssignExpr):
    pass
  
  @abstractmethod
  def visitExpr_TimesAssignExpr(self, timesAssignExpr):
    pass
  
  @abstractmethod
  def visitExpr_DivideAssignExpr(self, divAssignExpr):
    pass
  
  @abstractmethod
  def visitExpr_ArrayDeclaration(self, exprArrayDecl):
    pass
  
  @abstractmethod
  def visitExpr_NumberInt(self, exprNumber):
    pass
  
  @abstractmethod
  def visitExpr_NumberFloat(self, exprNumber):
    pass

  @abstractmethod
  def visitExpr_EncapsedString(self, exprEncapsed):
    pass
  
  @abstractmethod  
  def visitExpr_Boolean(self, exprBoolean):
    pass

  @abstractmethod  
  def visitExpr_Mod(self, exprMod):
    pass

  @abstractmethod  
  def visitExpr_FunctionCall(self, exprFunctionCall):
    pass
  
  #@abstractmethod
  #def visitExpr_TypeCastOp(self, typeCastOp):
    #pass
  
  # ================ END P_EXPR ===================
  
  @abstractmethod
  def visitFunctionCall_NoParameter(self, functionCall):
    pass
  
  @abstractmethod
  def visitFunctionCall_WithParameter(self, functionCall):
    pass
  
  @abstractmethod
  def visitFCParameterList_Single(self, fcParameterList):
    pass
  
  @abstractmethod
  def visitFCParameterList_Mul(self, fcParameterList):
    pass
  
  @abstractmethod
  def visitFCParameterListColonParameter_Single(self, fcParameterListColonParameter):
    pass
  
  @abstractmethod
  def visitFCParameterListColonParameter_Mul(self, fcParameterListColonParameter):
    pass
  
  @abstractmethod
  def visitFunctionCallParameter_Expr(self, functionCallParameter):
    pass
  
  @abstractmethod
  def visitFunctionCallParameter_AmpersandVariable(self, functionCallParameter):
    pass
  
  @abstractmethod
  def visitAssignOperator_Token(self, assignOp):
    pass
  
  @abstractmethod
  def visitArrayDec_NoPairList(self, arrayDec):
    pass
  
  @abstractmethod
  def visitArrayDec_WithPairList(self, arrayDec):
    pass
  
  @abstractmethod
  def visitArrayPairList_ArrayPair_Single(self, arrayPairList):
    pass
  
  @abstractmethod
  def visitArrayPairList_ArrayPair_Mul(self, arrayPairList):
    pass
  
  @abstractmethod
  def visitArrayPair_Expr(self, arrayPair):
    pass
  
  @abstractmethod
  def visitArrayPairList_Mul(self, arrayPairList):
    pass
  
  @abstractmethod
  def visitArrayPairListArr_Single(self, arrayPairList):
    pass
  
  @abstractmethod
  def visitStatementBlockOpt_Statement(self, statementBlockOpt):
    pass

  @abstractmethod
  def visitStatementBlockOpt_StatementMul(self, statementBlockOpt):
    pass

  @abstractmethod
  def visitstatementMulSingle(self, statementMul):
    pass
  
  @abstractmethod
  def visitstatementMulMul(self, statementMul):
    pass

  @abstractmethod
  def visitExprParentheses_Expr(self, exprParentheses):
    pass

  @abstractmethod
  def visitExpr_Variable(self, exprVariable):
    pass

  @abstractmethod
  def visitVariable_Single(self, variable):
    pass
  
  @abstractmethod
  def visitVariable_Array(self, variable):
    pass
  
  @abstractmethod
  def visitArrayDec_NoPairList(self, arrayDec):
    pass
  
  @abstractmethod
  def visitArrayDec_WithPairList(self, arrayDec):
    pass
  
  @abstractmethod
  def visitArrayPairList_ArrayPair_Single(self, arrayPairList):
    pass
  
  @abstractmethod
  def visitArrayPairList_ArrayPair_Mul(self, arrayPairList):
    pass
  
  @abstractmethod
  def visitArrayPair_Expr(self, arrayPair):
    pass
  
  @abstractmethod
  def visitArrayPairList_Mul(self, arrayPairList):
    pass
  
  @abstractmethod
  def visitArrayPairListArr_Single(self, arrayPairList):
    pass
  
  @abstractmethod
  def visitStatement_While(self, statement):
    pass

  @abstractmethod
  def visitWhileStatementSingle(self, whileStatement):
    pass

  @abstractmethod
  def visitStatement_Do_While(self, whilestatement):
    pass

  @abstractmethod
  def visitDoWhileStatementSingle(self, whilestatement):
    pass

  @abstractmethod
  def visitStatement_For(self, statement):
    pass
  
  @abstractmethod
  def visitForStatement_For(self, forStatement):
    pass
  
  @abstractmethod
  def visitForParameters_Empty(self):
    pass
  @abstractmethod
  def visitForParameters_Left(self, forParameters):
    pass
  
  @abstractmethod
  def visitForParameters_Left_Mid(self, forParameters):
    pass

  @abstractmethod 
  def visitForParameters_Left_Right(self, forParameters):
    pass
  
  @abstractmethod
  def visitForParameters_Mid(self, forParameters):
    pass

  @abstractmethod 
  def visitForParameters_Mid_Right(self, forParameters):
    pass
    
  @abstractmethod
  def visitForParameters_Right(self, forParameters):
    pass

  @abstractmethod 
  def visitForParameters_Full(self, forParameters):
    pass

  @abstractmethod 
  def visitForExprOpt_Mul(self, forExprOpt):
    pass

  @abstractmethod 
  def visitForExprOpt_Single(self, forExprOpt):
    pass

  @abstractmethod 
  def visitForExprColonExpr_Single(self, forExprColonExpr):
    pass

  @abstractmethod 
  def visitForExprColonExpr_Mul(self, forExprColonExpr):
    pass

  @abstractmethod
  def visitStatement_Exit(self, statement):
    pass

  @abstractmethod
  def visitExit_ExitExpr(self, _exit):
    pass

  @abstractmethod
  def visitExit_Empty(self):
    pass
  
  @abstractmethod
  def visitExitExpr_Expr(self, exitExpr):
    pass

  @abstractmethod
  def visitExitExpr_Empty(self):
    pass

  @abstractmethod
  def visitStatement_Break(self, statement):
    pass

  @abstractmethod
  def visitBreak_Expr(self, _break):
    pass
  
  @abstractmethod
  def visitBreak_Empty(self):
    pass

  @abstractmethod
  def visitStatement_Die(self, statement):
    pass

  @abstractmethod
  def visitDie_ExitExpr(self, die):
    pass

  @abstractmethod
  def visitDie_Empty(self):
    pass

  @abstractmethod
  def visitExpr_TernaryOp(self, exprTernary):
    pass

  @abstractmethod
  def visitStatement_Continue(self, statement):
    pass

  @abstractmethod
  def visitContinue_Expr(self, _continue):
    pass

  @abstractmethod
  def visitContinue_Empty(self):
    pass

  @abstractmethod
  def visitStatement_Return(self, statement):
    pass

  @abstractmethod
  def visitReturn_Expr(self, _return):
    pass

  @abstractmethod
  def visitReturn_Empty(self):
    pass

  @abstractmethod
  def visitStatement_Foreach(self, statement):
    pass

  @abstractmethod
  def visitForeachStatement_NoAssoc(self, foreachStatement):
    pass

  @abstractmethod
  def visitForeachStatement_WithAssoc(self, foreachStatement):
    pass


  '''      
  @abstractmethod
  def visitStatementBlockOpt_ParenEmpty():
  pass
  
  @abstractmethod
  def visitParameter_Prefix_Var():
    pass
  
  @abstractmethod
  def visitParameter_Var_Sufix():
    pass
  
  @abstractmethod
  def visitParameter_Full():
    pass
  
  @abstractmethod
  def visitParameterPrefix_PType_Amp():
    pass
  
  @abstractmethod
  def visitParameterPrefix_Ampersand():
    pass
  
  @abstractmethod
  def visitParameterPrefix_PType():
    pass
  
  @abstractmethod
  def visitParameterType_Type():
    pass
  
  @abstractmethod
  def visitStaticScalar_CommonScalar():
    pass
  
  @abstractmethod
  def visitStaticScalar_Plus_Static():
    pass
  
  @abstractmethod
  def visitStaticScalar_Minus_Static():
    pass
  
  @abstractmethod
  def visitCommonScalar_Token():
    pass
  
  @abstractmethod
  def visitStatementElse_Else():
    pass
  
  @abstractmethod
  def visitStatement_Global():
    pass
  
  @abstractmethod
  def visitIfStatement_Single():
    pass
  
  @abstractmethod
  def visitIfStatement_Complement():
    pass
  
  @abstractmethod
  def visitStatementIf_ExprParen():
    pass
  
  @abstractmethod
  def visitExprParentheses_Expr():
    pass
  
  @abstractmethod
  def visitIfStatemnet_Else():
    pass
  
  @abstractmethod
  def visitTypeCastOp_Token():
    pass
  
  @abstractmethod
  def visitArrayPair_Variable():
    pass
  
  @abstractmethod
  def visitArrayPair_Attr_AmpersandVariable():
    pass
  
  @abstractmethod
  def visitArrayPair_Attr_Expr():
    pass
  
  @abstractmethod
  def visitAmpersandVariable_WithAmp():
    pass
  
  @abstractmethod
  def visitAmpersandVariable_NoAmp():
    pass
  
  @abstractmethod
  def visitGlobalStatement_Mul():
    pass
  
  @abstractmethod
  def visitGlobalVar_Var():
    pass
  
  @abstractmethod
  def visitGlobalVar_DolarVar():
    pass
  
  @abstractmethod
  def visitGlobalVar_DolarExpr():
    pass
  
  @abstractmethod
  def visitGlobalVarMul_Single():
    pass
  
  @abstractmethod
  def visitGlobalVarMul_Mul():
    pass

  @abstractmethod
  def visitSelectorWithExpr():
    pass
  
  @abstractmethod
  def visitWhileStatementSingle():
    pass
  
  @abstractmethod
  def visitStatementBlockOpt_Empty():
    pass
'''