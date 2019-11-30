# LFT -  compilador para linguagem PHP
# Fase atual: Análise Léxica
# Luiz Moitinho

#OBJETIVO: TOKENIZAR UMA SIMPLES EXPRESSAO

import ply.lex as lex;

# LISTA DE NOME DOS TOKENS
tokens = (

    'NUMBER_INTEGER',
    'NUMBER_REAL',
    'ASSIGN',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'PERCENT',
    'LPAREN',
    'RPAREN',
    'LKEY',
    'RKEY',
    'BEGIN_COMMENT',
    'END_COMMENT',
    'COMMENT_LINE',
    'LESS_THAN',
    'LESS_EQUAL',
    'GREAT_THAN',
    'GREAT_EQUAL',
    'EQUAL',
    'NOT_EQUAL'
);

#EXPRESSOES REGULARES: No ply é indenficado usando o sufixo t_[nome do token] 
        #operadores aritméticos
t_ASSIGN =  r'\='
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


t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LKEY = r'\{}'
t_RKEY = r'}'
t_COMMENT_LINE=r'\//'




#EXPRESSOES REGULARES COM FUNÇÕES
def t_IDENTIFIER(t):
    r'\[a-ZA-Z]'

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

t_ignore = ' \t'


#Regra de tratamento de erros
def t_error(t):
    print("Um caracter ilegal foi encontrado: '%s'" % t.value[0])
    t.lexer.skip(1);



#Execução do lexico
arquivo =  'x=10.20';
lexer = lex.lex()

#inputa o arquivo no classe lexer para gerar os tokens
lexer.input(arquivo)

while True:
    token = lexer.token()
    if not token:
        break # Quando nao haver mais tokens a serem buscados -  fim do arquivo
    print(token)

