# LFT -  compilador para linguagem PHP
# Fase atual: Análise Léxica
# Luiz Moitinho

#OBJETIVO: TOKENIZAR UMA SIMPLES EXPRESSAO

import ply.lex as lex

reserved = {
    'include':'INCLUDE',
    'require':'REQUIRE',
    'require_once':'REQUIRE_ONCE',
    'function':'FUNCTION',
    'use':'USE',
    'as':'AS',
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
    'var_dump':'VAR_DUMP',
    'true':'TRUE',
    'false':'FALSE',
    'for' : 'FOR',
    'while' : 'WHILE',
    'do':'DO'

}

tokens =[
    'STRING',
    'BEGIN_PROGRAM',
    'END_PROGRAM',
    'NUMBER_INTEGER',
    'ID',
    'NUMBER_REAL',
    'ASSIGN',
    'CONCATENATE',
    'INCREMENT',
    'DECREMENT',
    'ADD_ASSIGN',
    'SUB_ASSIGN',
    'MOD_ASSIGN',
    'PLUS_ASSIGN',
    'DIVIDE_ASSIGN',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'PERCENT',
    'LPAREN',
    'RPAREN',
    'LKEY',
    'RKEY',
    'COMMENT_LINE',
    'COMMENT_LINE2',
    'LESS_THAN',
    'LESS_EQUAL',
    'GREAT_THAN',
    'GREAT_EQUAL',
    'EQUAL',
    'NOT_EQUAL',
    'SEMICOLON',
    'LEFT_LOGICAL',
    'RIGHT_LOGICAL',
    'TAB'
] + list(reserved.values())

#EXPRESSOES REGULARES: No ply é indenficado usando o sufixo t_[nome do token] 
       
t_TAB = r'\t'

t_COMMENT_LINE = r'\//.* | \#.*'
t_COMMENT_LINE2 = r'\/\*(.|\n)*\*\/'
t_CONCATENATE =  r'\.\='
        #operadores aritméticos
t_ASSIGN =  r'\='
t_ADD_ASSIGN = r'\+\='
t_SUB_ASSIGN = r'\-\='
t_MOD_ASSIGN = r'\%\='
t_PLUS_ASSIGN = r'\*\='
t_DIVIDE_ASSIGN =  r'\/\='
t_LEFT_LOGICAL = r'\<\<'
t_RIGHT_LOGICAL = r'\>\>'
t_INCREMENT =  r'\+\+'
t_DECREMENT =  r'\-\-'


t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_PERCENT = r'\%'

        #operadores relacionais
t_LESS_THAN = r'\<'
t_GREAT_THAN =  r'\>'
t_LESS_EQUAL = r'\<\='
t_GREAT_EQUAL = r'\>\='
t_EQUAL = r'\=\='
t_NOT_EQUAL = r'\!\='


t_BEGIN_PROGRAM =  r'\<\?php | \<\?\= | \<\?'
t_END_PROGRAM   =  r'\?\>'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LKEY = r'\{'
t_RKEY = r'\}'
t_SEMICOLON = r'\;'
t_ignore = ' '




#EXPRESSOES REGULARES COM FUNÇÕES

#definição de uma string
'''
    - No php a quebra de linha na string insere espaços em branco em vez de quebra de linha
'''
def t_STRING(t):
    r'\".*\"'
    return t



'''
    - Validar palavras sem acento
    - definição de um identificador
    [\wÀ-ú]
'''
def t_ID(t):
    r'\$[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t
    
def t_NUMBER_REAL(t):
    r'\d*\.\d+'
    t.value = float(t.value)
    return t
    
def t_NUMBER_INTEGER(t):
    r'\d+'
    t.value = int(t.value) # Faz o cast do atributo value para inteiro.
    return t

def t_newline(t):
    r'\n+'
    pass

#Regra de tratamento de erros
def t_error(t):
    print("Um caracter ilegal foi encontrado: '%s'" % t.value[0])
    t.lexer.skip(1)


#Execução do lexico
arquivo = '$joão .= "gay"'
lexer = lex.lex()

#inputa o arquivo no classe lexer para gerar os tokens
lexer.input(arquivo)

while True:
    token = lexer.token()
    if not token:
        break # Quando nao haver mais tokens a serem buscados -  fim do arquivo
    print(token)

