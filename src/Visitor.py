class Visitor():

  def visitMain_MainInner(self, main):
    print('<?php', end=' ')
    main.mainInner.accept(self)
    print('?>', end=' ')
  
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
    
  def visitFuncDecStatement_Function(self, funcDecStatement):
    print('function', end=' ')
    funcDecStatement.fds_id.accept(self)
    funcDecStatement.fds_parameter.accept(self)
    funcDecStatement.fds_statements.accept(self)
    
  def visitFds_id_withAmpersand(self, fds_id):
    print('&', end='')
    print(fds_id.id)
    
  def visitFds_id_noAmpersand(self, fds_id):
    print(fds_id.id)
    
  def visitFds_parameter_withParameter(self, fds_parameter):
    print('(', end='')
    fds_parameter.parameter_list.accept(self)
    print(')', end='')
    
  def visitFds_parameter_noParameter(self, fds_parameter):
    print('(', end='')
    print(')', end='')
    
  def visitFds_statements_withStatements(self, fds_statements):
    print('{', end='')
    fds_statements.inner_statement_MUL.accept(self)
    print('}', end='')
    
  def visitFds_statements_noStatements(self, fds_statements):
    print('{', end='')
    print('}', end='')
  
  def visitStatement_Expr(self, statement_expr):
    statement_expr.expr.accept(self)
    print(';')

  def visitExpr_True(self, expr):
    print('true', end=' ')
    
  def visitExpr_False(self, expr):
    print('false', end=' ')