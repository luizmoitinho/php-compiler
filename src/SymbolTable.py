symbolTable = []
INT = 'int'
FLOAT = 'float'
BOOL = 'boolean'
STRING = 'string'
ARRAY = 'array'

SCOPE = 'scope'
BINDABLE = 'bindable'
FUNCTION = 'function'
PARAMS = 'params'

VARIABLE = 'var'
TYPE     = 'type'
NAME     = 'name' 
VALUE    = 'value'

COMP = 'compOp'
ARITH = 'arithOp'

ISGLOBAL = 'isGlobal'

Number = [INT, FLOAT]

def beginScope(nameScope):
  global symbolTable
  symbolTable.append({})
  symbolTable[-1][SCOPE] = nameScope
  print(symbolTable[-1][SCOPE], '- Create scope:', nameScope)
  
def endScope():
  global symbolTable
  print(symbolTable[-2][SCOPE], '- End scope:', symbolTable[-1][SCOPE])
  symbolTable = symbolTable[0:-1]

def addVar(name, type = None, isGlobal = False, value = None):
  global symbolTable
  varInfo = {}
  if symbolTable[-1][SCOPE] == 'global':
    symbolTable[-1][name] = { NAME: name, BINDABLE: VARIABLE, TYPE: type, ISGLOBAL: True, VALUE: value }
    varInfo = { NAME: name, TYPE: type, ISGLOBAL: True, VALUE: value }
  else:
    symbolTable[-1][name] = { NAME: name, BINDABLE: VARIABLE, TYPE: type, ISGLOBAL: isGlobal, VALUE: value }
    varInfo = { NAME: name, TYPE: type, ISGLOBAL: isGlobal, VALUE: value }
  print(symbolTable[-1][SCOPE], '- Create variable', name, 'with type', type)
  return varInfo

def addFunction(name, params, type = None):
  global symbolTable
  print(symbolTable[-1][SCOPE], '- Create function', name, 'with params', params, 'and type', type)
  symbolTable[-1][name] = {BINDABLE: FUNCTION, PARAMS: params, TYPE: type}

def updateBindableType(name, type, value = None):
  global symbolTable
  for i in reversed(range(1, len(symbolTable))):
    if(name in symbolTable[i].keys()):
      symbolTable[i][name][TYPE] = type
      symbolTable[i][name][VALUE] = value
      print(symbolTable[i][SCOPE], '- Update bindable type of', name, 'to', type)
      return symbolTable[i][name] 
  return None

def updateGlobalBindableType(name, type, value = None):
  global symbolTable
  if (name in symbolTable[0].keys()):
    symbolTable[0][name][TYPE] = type
    symbolTable[0][name][VALUE] = value
    print(symbolTable[0][SCOPE], '- Update global bindable type of', name, 'to', type)
    return symbolTable[0][name] 
  return None

def getBindable(name):
  global symbolTable
  if len(symbolTable) > 1:  
    for i in reversed(range(1, len(symbolTable))):
      if (name in symbolTable[i].keys()):
        return symbolTable[i][name]
  else:
    return getGlobalBindable(name)

def getGlobalBindable(name):
  global symbolTable
  if (name in symbolTable[0].keys()):
    return symbolTable[0][name]
  return None

def printTable():
  global symbolTable
  print(symbolTable)