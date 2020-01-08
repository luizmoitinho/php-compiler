import ply.lex as lex

reserved = {
    'function':'FUNCTION',
    'and':'AND',
    'or':'OR',
    'if' : 'IF',
    'else' : 'ELSE',
    'endif':'ENDIF',
    'switch':'SWITCH',
    'case':'CASE',
    'break':'BREAK',
    'continue':'CONTINUE',
    'echo':'ECHO',
    'true':'TRUE',
    'false':'FALSE',
    'while' : 'WHILE',
    'for' : 'FOR',
    'do':'DO',
}

tokens =[
    'COMMENT_SINGLE',
    'COMMENT_MULTI',
    'BEGIN_PROGRAM',
    'END_PROGRAM',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'PERCENT',
    'ASSIGN',
    'CONCATENATE',
    'INCREMENT',
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
    'LESS_THAN',
    'LESS_EQUAL',
    'GREAT_THAN',
    'GREAT_EQUAL',
    'EQUAL',
    'NOT_EQUAL',
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
t_FUNCTION = r'function'
t_AND = r'and'
t_OR = r'or'
t_IF = r'if'
t_ELSE = r'else'
t_ENDIF = r'endif'
t_SWITCH = r'switch'
t_CASE = r'case'
t_BREAK = r'break'
t_CONTINUE = r'continue'
t_ECHO = r'echo'
t_TRUE = r'true'
t_FALSE = r'false'
t_WHILE = r'while'
t_FOR = r'for'
t_DO = r'do'
t_COMMENT_SINGLE = r'\//.* | \#.*'
t_COMMENT_MULTI = r'\/\*(.|\n)*\*\/'
t_BEGIN_PROGRAM =  r'\<\?php | \<\?\= | \<\?'
t_END_PROGRAM   =  r'\?\>'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
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
t_LESS_THAN = r'\<'
t_LESS_EQUAL = r'\<\='
t_GREAT_THAN =  r'\>'
t_GREAT_EQUAL = r'\>\='
t_EQUAL = r'\=\='
t_NOT_EQUAL = r'\!\='
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

if (  $valor1 > $valor2  )
  echo "A variável $valor1 é maior que a variável $valor2";
else if (  $valor2 > $valor1 )
  echo "A variável $valor2 é maior que a variável $valor1";
 else
   echo "A variável $valor1 é igual à variável $valor2";
?>'''

lexer = lex.lex()
lexer.input(arquivo)

while True:
    token = lexer.token()
    if not token:
        break
    print(token)