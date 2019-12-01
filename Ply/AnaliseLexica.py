# LFT -  compilador para linguagem PHP
# Fase atual: Análise Léxica
# Luiz Moitinho

#OBJETIVO: TOKENIZAR UMA SIMPLES EXPRESSAO

import ply.lex as lex;

reserved = {
    'include':'INCLUDE',
    'require':'REQUIRE',
    'require_once':'REQUIRE_ONCE',
    'function':'FUNCTION',
    'use':'USE',
    'as':'AS',
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
    'BEGIN_PROGRAM',
    'END_PROGRAM',
    'NUMBER_INTEGER',
    'ID',
    'NUMBER_REAL',
    'ASSIGN',
    'INCREMENT',
    'DECREMENT',
    'POS_INCREMENT',
    'PRE_INCREMENT',
    'POS_DECREMENT',
    'PRE_DECREMENT',
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
    'TAB'] + list(reserved.values())

#EXPRESSOES REGULARES: No ply é indenficado usando o sufixo t_[nome do token] 
       

t_TAB = r'\t'
t_COMMENT_LINE = r'\//.* | \#.*'
t_COMMENT_LINE2 = r'\/\*(.|\n)*\*\/'

        #operadores aritméticos
t_ASSIGN =  r'\='
t_INCREMENT =  r'\+\+'
t_DECREMENT =  r'\-\-'
t_POS_INCREMENT = r'\+\+'
t_PRE_INCREMENT = r'\+\='
t_POS_DECREMENT = r'\=\-'
t_PRE_DECREMENT = r'\-\='

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
    t.lexer.skip(1);



#Execução do lexico
arquivo = "-="
lexer = lex.lex()

#inputa o arquivo no classe lexer para gerar os tokens
lexer.input(arquivo)

while True:
    token = lexer.token()
    if not token:
        break # Quando nao haver mais tokens a serem buscados -  fim do arquivo
    print(token)

