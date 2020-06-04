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
TYPE = 'type'
NAME = 'name' 

COMP = 'compOp'
ARITH = 'arithOp'

COMP = 'compOp'
ARITH = 'arithOp'

Number = [INT, FLOAT]

def beginScope(nameScope):
  global symbolTable
  symbolTable.append({})
  symbolTable[-1][SCOPE] = nameScope
  print(symbolTable[-1][SCOPE], '- Create scope:', nameScope)
  
def endScope():
  global symbolTable
  print(symbolTable[-2][SCOPE], '- End scope:', symbolTable[-1][SCOPE]) 
  data = getDataBindable(symbolTable[-1][SCOPE])
  if data != None and data[BINDABLE]!=FUNCTION:
   updateVariableScope(-1,-2)
  symbolTable = symbolTable[0:-1]

def updateVariableScope(indexScope1, indexScope2):
  data=[]
  for elemCurrentScope in symbolTable[indexScope1]:
    info = getDataBindable(elemCurrentScope)
    if info != None and (type(info) == dict and info[BINDABLE]==VARIABLE): 
      for elemPreviousScope in symbolTable[indexScope2]:
        if elemCurrentScope == elemPreviousScope:
          symbolTable[indexScope2][elemPreviousScope][TYPE] = symbolTable[indexScope1][elemCurrentScope][TYPE]

def addVar(name, type = None):
  global symbolTable
  symbolTable[-1][name] = {BINDABLE: VARIABLE, TYPE: type}
  print(symbolTable[-1][SCOPE], '- Create variable', name, 'with type', type)
  return { NAME: name, TYPE: type }
  
def getDataBindable(bindableName):
    global symbolTable
    for i in reversed(range(len(symbolTable))):
        if (bindableName in symbolTable[i].keys()):
            return symbolTable[i][bindableName]
    return None

def addFunction(name, params, type = None):
  global symbolTable
  print(symbolTable[-1][SCOPE], '- Create function', name, 'with params', params, 'and type', type)
  symbolTable[-1][name] = {BINDABLE: FUNCTION, PARAMS: params, TYPE: type}

# ==== ANALISAR =====
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