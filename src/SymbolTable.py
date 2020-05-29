symbolTable = []

INT     = 'int'
FLOAT   = 'float'
BOOL    = 'boolean'
STRING  = 'string'
ARRAY   = 'array'

SCOPE    = 'scope'
FUNCTION = 'function'
PARAMS   = 'params'
VARIABLE = 'var'

TYPE      = 'type'
NAME      = 'name' 
BINDABLE  = 'bindable'

Number = [INT, FLOAT]

def beginScope(nameScope):
  global symbolTable
  symbolTable.append({})
  symbolTable[-1][SCOPE] = nameScope
  print(symbolTable[-1][SCOPE], '- Create scope:', nameScope)

def endScope():
  global symbolTable
  print(symbolTable[-2][SCOPE], '- End scope:', symbolTable[-1][SCOPE ])
  symbolTable = symbolTable[0:-1]

def addVar(name, type = None):
  global symbolTable
  symbolTable[-1][name] = {BINDABLE: VARIABLE, TYPE: type}
  print(symbolTable[-1][SCOPE], '- Create variable', name, 'with type', type)
  return { NAME: name, TYPE: type }

def updateBindableType(name, type):
  global symbolTable
  for i in reversed(range(len(symbolTable))):
    if(name in symbolTable[i].keys()):
      symbolTable[i][name][TYPE] = type
      print(symbolTable[i][SCOPE], '- Update bindable type of', symbolTable[i][name][BINDABLE], name, 'to', type)
      # Adicionar o nome do bindable ao dicionario para uso em certos casos
      bindableInfo = symbolTable[i][name].copy()
      bindableInfo.update({ NAME: name })
      return bindableInfo 
  return None

def addFunction(name, params, type = None):
  global symbolTable
  print(symbolTable[-1][SCOPE], '- Create function', name, 'with params', params, 'and type', type)
  symbolTable[-1][name] = {BINDABLE: FUNCTION, PARAMS: params, TYPE: type}

def getBindable(name):
  global symbolTable
  for i in reversed(range(len(symbolTable))):
      if (name in symbolTable[i].keys()):
        # Adicionar o nome do bindable ao dicionario para uso em certos casos
        bindableInfo = symbolTable[i][name].copy()
        bindableInfo.update({ NAME: name })
        return bindableInfo 
  return None

def printTable():
  global symbolTable
  print(symbolTable)