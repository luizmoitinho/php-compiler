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
    
  def visitInnerStatementMul_Single(self, innerstatementMul):
    innerstatementMul.innerStatement.accept(self)
    
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
    print('{', end='')
    fds_statements.inner_statement_MUL.accept(self)
    print('}', end='')
    
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
  
  def visitStatement_Expr(self, statement_expr):
    statement_expr.expr.accept(self)
    print(';')

  def visitExpr_True(self, expr):
    print('true', end=' ')
    
  def visitExpr_False(self, expr):
    print('false', end=' ')