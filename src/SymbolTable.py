symbolTable = []

#======== TIPOS ============

INT      = 'int'
FLOAT    = 'float'
BOOL     = 'boolean'
STRING   = 'string'
ARRAY    = 'array'
VARIABLE = 'var'

#======= FUNÇÕES =========

FUNCTION = 'function'
PARAMS   = 'params'

#========== GERAL =========

SCOPE    = 'scope'
BINDABLE = 'bindable'
TYPE     = 'type'
NAME     = 'name'

Number = [INT,FLOAT]


#=====  FUNCOES DA SYMBOLTABLE

def beginScope(nameScope):
    global symbolTable
    symbolTable.append({})
    symbolTable[-1][SCOPE] =  nameScope
    print(symbolTable[-1][SCOPE],-' - SCOPE CREATED: ',nameScope)

def endScope():
    global symbolTable
    print(symbolTable[-2][SCOPE], ' - END SCOPE:', symbolTable[-1][SCOPE ])
    symbolTable = symbolTable[0:-1]

def addVar(name, type):
    global symbolTable
    data = {BINDABLE:VARIABLE, TYPE = type}
    symbolTable[-1][name] = data
    print(symbolTable[-1][SCOPE],' - VARIABLE CREATED: {name: ',name,', type: ',type,'}')
    return data

def addFunction(name, params, returnType =  None):
    global symbolTable
    print(symbolTable[-1][SCOPE], ' - FUNCTION CREATED: {name: ', name, ', params: ', params, ', type:', type,'}')
    symbolTable[-1][name] = {BINDABLE: FUNCTION, PARAMS:params,TYPE:returnType}

def getBindable(bindableName):
    global symbolTable
    for i in reverse(range(len(symbolTable))):
        if(bindableName in symbolTable[i].key()):
            return symbolTable[i][bindableName]
    return None


def printTable():
  global symbolTable
  print(symbolTable)