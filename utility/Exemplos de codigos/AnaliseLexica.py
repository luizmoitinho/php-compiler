import ply.lex as lex

reserved = {
    'var' : 'VAR',
    'array' : 'ARRAY',
    'const' : 'CONST',
    'if' : 'IF',
    'else' : 'ELSE',
    'elseif' : 'ELSEIF',
    'for' : 'FOR',
    'while' : 'WHILE',
    'do' : 'DO',
    'foreach' : 'FOREACH',
    'switch' : 'SWITCH',
    'case' : 'CASE',
    'break' : 'BREAK',
    'continue' : 'CONTINUE',
    'return' : 'RETURN',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'null' : 'NULL',
    'and' : 'AND',
    'or' : 'OR',
    'xor' : 'XOR',
    'new' : 'NEW',
    'instanceof' : 'INSTANCEOF',
    'function' : 'FUNCTION',
    'class' : 'CLASS',
    'default' : 'DEFAULT',
}

tokens =[
    'COMMENT_SINGLE',
    'COMMENT_MULTI',
    'BEGIN_PROGRAM',
    'END_PROGRAM',
    'EQUAL',
    'NOT_EQUAL',
    'GREAT_THAN',
    'LESS_THAN',
    'LESS_EQUAL',
    'GREAT_EQUAL',
    'LPAREN',
    'RPAREN',
    'LBRACKT',
    'RBRACKT',
    'LKEY',
    'RKEY',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'TIMES',
    'PERCENT',
    'ANDLCC',
    'ORLCC',
    'ANDL',
    'ORL',
    'INCREMENT',
    'DECREMENT',
    'ASSIGN',
    'SEMICOLON',
    'LEFT_LOGICAL',
    'RIGHT_LOGICAL',
    'IDENTATION',
    'STRING',
    'NUMBER_REAL',
    'NUMBER_INTEGER',
    'ID',
] + list(reserved.values())

t_ignore = ' \t'
t_VAR = r'var'
t_ARRAY = r'array'
t_CONST = r'const'
t_IF = r'if'
t_ELSE = r'else'
t_ELSEIF = r'elseif'
t_FOR = r'for'
t_WHILE = r'while'
t_DO = r'do'
t_FOREACH = r'foreach'
t_SWITCH = r'switch'
t_CASE = r'case'
t_BREAK = r'break'
t_CONTINUE = r'continue'
t_RETURN = r'return'
t_TRUE = r'true'
t_FALSE = r'false'
t_NULL = r'null'
t_AND = r'and'
t_OR = r'or'
t_XOR = r'xor'
t_NEW = r'new'
t_INSTANCEOF = r'instanceof'
t_FUNCTION = r'function'
t_CLASS = r'class'
t_DEFAULT = r'default' 

t_COMMENT_SINGLE = r'\//.* | \#.*'
t_COMMENT_MULTI = r'\/\*(.|\n)*\*\/'
t_BEGIN_PROGRAM =  r'\<\?php | \<\?\= | \<\?'
t_END_PROGRAM   =  r'\?\>'
t_EQUAL = r'\=\='
t_NOT_EQUAL = r'\!\='
t_GREAT_THAN =  r'\>'
t_LESS_THAN = r'\<'
t_LESS_EQUAL = r'\<\='
t_GREAT_EQUAL = r'\>\='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKT = r'\['
t_RBRACKT = r'\]'
t_LKEY = r'{'
t_RKEY = r'}'
t_PLUS = r'\+'
t_MINUS = r'-'
t_DIVIDE = r'/'
t_TIMES = r'\*'
t_PERCENT = r'\%'
t_ANDLCC = r'\&&'
t_ORLCC = r'\|\|'
t_ANDL = r'\&'
t_ORL = r'\|'
t_INCREMENT = r'\++'
t_DECREMENT = r'\--'
t_ASSIGN =  r'\='
t_SEMICOLON = r'\;'
t_LEFT_LOGICAL = r'\<\<'
t_RIGHT_LOGICAL = r'\>\>'

ArrayTabulacao = [0]
IndicePosicao = 0
ConstTabulacao = 8

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

def t_STRING(t):
    r'\".*\"'
    return t
  
def t_NUMBER_REAL(t):
    r'\d*\.\d+'
    t.value = float(t.value)
    return t
    
def t_NUMBER_INTEGER(t):
    r'\d+'
    t.value = int(t.value) 
    return t

def t_ID(t):
    r'\$[_a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

def t_newline(t):
    r'\n+'
    pass

def t_error(t):
    print("Um caracter ilegal foi encontrado: '%s'" % t.value[0])
    t.lexer.skip(1)
    

 
arquivo ='''<?php
$valor1 = 40;
$valor2 = 20;
?>'''

lexer = lex.lex()
lexer.input(arquivo)

while True:
    token = lexer.token()
    if not token:
        break
    print(token)
