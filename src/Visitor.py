class Visitor():

  def visitMain_MainInner(self, main_mainInner):
    main_mainInner.mainInner.accept(self)

  def visitMainInner_InnerStatement(self, mainInner_innerStatement):
    mainInner_innerStatement.innerStatement.accept(self)
    mainInner_innerStatement.mainInner.accept(self)
    
  def visitMainInner_Empty(self, mainInner_empty):
    print('', end='')

  def visitInnerStatement_Statement(self, innerStatement):
    innerStatement.statement.accept(self)

  def visitStatement_Expr(self, statement_expr):
    statement_expr.expr.accept(self)
    print(';')

  def visitExpr_True(self, expr_true):
    print('true', end=' ')