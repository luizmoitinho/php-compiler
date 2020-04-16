import ply.lex as lex

reserved = {
    'as'        : 'AS',
    'function'  : 'FUNCTION',
    'and'       : 'AND',
    'or'        : 'OR',
    'if'        : 'IF',
    'else'      : 'ELSE',
    'elseif'    : 'ELSEIF',
    'case'      : 'CASE',
    'break'     : 'BREAK',
    'continue'  : 'CONTINUE',
    'true'      : 'TRUE',
    'false'     : 'FALSE',
    'while'     : 'WHILE',
    'for'       : 'FOR',
    'foreach'   : 'FOREACH',
    'declare'   : 'DECLARE',
    'enddeclare': 'ENDDECLARE',
    'do'        : 'DO',
    'int'       : 'INT_TYPE',
    'double'    : 'DOUBLE_TYPE',
    'float'     : 'FLOAT_TYPE',
    'real'      : 'REAL_TYPE',
    'string'    : 'STRING_TYPE',
    'array'     : 'ARRAY_TYPE',
    'bool'      : 'BOOL_TYPE',
    'boolean'   : 'BOOLEAN_TYPE',
    'unset'     : 'UNSET',
    'exit'      : 'EXIT',
    'die'       : 'DIE',
    'list'      : 'LIST',
    'clone'     : 'CLONE',
    'return'    : 'RETURN',
    'global'    : 'GLOBAL',
    'var'       : 'VAR' #Remover se não existir
}

tokens = [
    'ID',
    'ASPAS',
    'APOSTROFE',
    'ARROBA',
    'AMPERSAND',
    'ATTR_ASSOC',
    'DOLAR',
    'COMMENT_SINGLE',
    'COMMENT_MULTI',
    'CRASE',
    'BEGIN_PROGRAM',
    'END_PROGRAM',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'DDOT',
    'PERCENT',
    'ASSIGN',
    'CONCATENATE',
    'INCREMENT',
    'INTE_DOT',
    'DECREMENT',
    'ADD_ASSIGN',
    'SUB_ASSIGN',
    'MOD_ASSIGN',
    'PLUS_ASSIGN',
    'DIVIDE_ASSIGN',
    'LPAREN',
    'RPAREN',
    'LKEY',
    'RKEY',
    'LBRACKET',
    'RBRACKET',
    'LESS_THAN',
    'LESS_EQUAL',
    'GREAT_THAN',
    'GREAT_EQUAL',
    'EQUALS',
    'NOT_EQUAL',
    'COLON',    
    'SEMICOLON',
    'LEFT_LOGICAL',
    'RIGHT_LOGICAL',
    'IDENTATION',
    'STRING',
    'NUMBER_REAL',
    'NUMBER_INTEGER',
    'VARIABLE',
    'CONSTANT_ENCAPSED_STRING',
    'EXC_DOT',
] + list(reserved.values())

t_ignore = ' \t'
t_COMMENT_SINGLE = r'\//.* | \#.*'
t_COMMENT_MULTI = r'\/\*(.|\n)*\*\/'
t_BEGIN_PROGRAM = r'\<\?php'
t_END_PROGRAM =  r'\?\>'
t_DOLAR =  r'\$'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_PERCENT = r'\%'
t_ASSIGN =  r'\='
t_CONCATENATE =  r'\.\='
t_INCREMENT =  r'\+\+'
t_DECREMENT =  r'\-\-'
t_ADD_ASSIGN = r'\+\='
t_SUB_ASSIGN = r'\-\='
t_MOD_ASSIGN = r'\%\='
t_PLUS_ASSIGN = r'\*\='
t_DIVIDE_ASSIGN =  r'\/\='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LKEY = r'\{'
t_RKEY = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LESS_THAN = r'\<'
t_LESS_EQUAL = r'\<\='
t_GREAT_THAN =  r'\>'
t_GREAT_EQUAL = r'\>\='
t_EQUALS = r'\=\='
t_NOT_EQUAL = r'\!\='
t_COLON = r'\,'
t_SEMICOLON = r'\;'
t_LEFT_LOGICAL = r'\<\<'
t_RIGHT_LOGICAL = r'\>\>'
t_AND = r'\&\&'
t_OR = r'\|\|'
t_AMPERSAND = r'\&'
t_ATTR_ASSOC = r'\=\>'
t_CRASE  = r'\`'
t_APOSTROFE  = r'\''
t_ASPAS =  r'\"'
t_DDOT = r'\:'
t_INTE_DOT = r'\?'
t_EXC_DOT = r'\!'
t_ARROBA = r'\@'
t_CONSTANT_ENCAPSED_STRING = r'\'[^\']*\'|\"[^\"]*\"'

ArrayTabulacao = [0]
IndicePosicao  =  0
ConstTabulacao =  8

def t_IDENTATION(t):
    r'\n[ \t]*'
    global IndicePosicao
    global ConstTabulacao
    Tamanho = 0
    
    for i in t.value:
        if(i == ' '):
            Tamanho += 1
        else:
            if(i != '\n'):
                Auxiliar = Tamanho // ConstTabulacao
                Tamanho = (Auxiliar + 1) * ConstTabulacao

    if(ArrayTabulacao[IndicePosicao] < Tamanho):
        ArrayTabulacao.append(Tamanho)
        IndicePosicao += 1
    if(ArrayTabulacao[IndicePosicao] > Tamanho):
        if(Tamanho in ArrayTabulacao):
            del ArrayTabulacao[ArrayTabulacao.index(Tamanho)+1:len(ArrayTabulacao)]
            IndicePosicao = ArrayTabulacao.index(Tamanho)
        else:
            print("Identação ilegal foi encontrada")

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

def t_NUMBER_REAL(t):
    r'\d*\.\d+'
    t.value = float(t.value)
    return t
    
def t_NUMBER_INTEGER(t):
    r'\d+'
    t.value = int(t.value) 
    return t

def t_VARIABLE(t):
    r'\$[_a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'VARIABLE')
    return t

def t_newline(t):
    r'\n+'
    pass

def t_error(t):
    print("Um caracter ilegal foi encontrado: '%s'" % t.value[0])
    t.lexer.skip(1)
