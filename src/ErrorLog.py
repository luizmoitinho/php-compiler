import SymbolTable as st

def AttributionTypeError(self, assignExpr, exprType):
  print('ERROR: Atribution to variable ', end='')
  assignExpr.variable.accept(self.printer)
  print(' returned type', exprType)
  
def AttributionInvalidTypeError(self, exprType, assignExpr, bindable):
  print('ERROR: Invalid atribution of type', exprType, end='') 
  print(' on variable ', end='') 
  assignExpr.variable.accept(self.printer)
  print(' that has type', bindable[st.TYPE])
  
def IncrementVariableError(variable):
  print('ERROR: Cannot increment variable', variable[st.NAME], 'with type', variable[st.TYPE])
  
def DecrementVariableError(variable):
  print('ERROR: Cannot decrement variable', variable[st.NAME], 'with type', variable[st.TYPE])
  
def ExpressionTypeError(self, expr, type1, type2):
  print('ERROR: Expression ', end='')
  expr.expr1.accept(self.printer)
  print(' has type', type1, 'while expression ', end='')
  expr.expr2.accept(self.printer)
  print(' has type', type2)