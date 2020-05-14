symbolTable = []

SCOPE = 'scope'
BINDABLE = 'bindable'
FUNCTION = 'function'
PARAMS = 'params'
VARIABLE = 'var'
TYPE = 'type'

def beginScope(nameScope):
  global symbolTable
  symbolTable.append({})
  symbolTable[-1][SCOPE] = nameScope
  print(symbolTable)

def endScope():
  global symbolTable
  symbolTable = symbolTable[0:-1]
  print(symbolTable)
  
def addVar(name):
  global symbolTable
  symbolTable[-1][name] = {BINDABLE: VARIABLE}
  print(symbolTable)
    
#Função não vai necessitar de tipo?, linguagem fracamente tipada
def addFunction(name, params):
  global symbolTable
  symbolTable[-1][name] = {BINDABLE: FUNCTION, PARAMS: params}
  
def getBindable(bindableName):
    global symbolTable
    for i in reversed(range(len(symbolTable))):
        if (bindableName in symbolTable[i].keys()):
            return symbolTable[i][bindableName]
    return None