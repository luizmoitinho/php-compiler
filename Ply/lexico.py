# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------

import ply.lex as lex
# List of token names. This is always required
tokens = ['ID','NUMBER','REAL','PLUS','MINUS','TIMES','DIVIDE',
'LPAREN','RPAREN','EQUAL','COMMENT_LINES','STRING','DPOINTS'
'LBRACKETS','RBRACKETS','LBRACE','RBRACE','SEMICOLON','BEGIN_COMMENT','END_COMMENT']


# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUAL = r'\='

#t_COMMENT_LINES = r'(/\* .* \*/) | (//.*)'
reserved = {
'if' : 'IF',
'then' : 'THEN',
'else' : 'ELSE',
'while' : 'WHILE',
'for':'FOR',
'int':'INT',
'float':'FLOAT' ,
'function':'FUNCTION'
}


literals =  ['{','}','[',']',':',';']
tokens += list(reserved.values())

# ================ literais ====================
def T_LBRACE(t):
    r'\{'
    t.type =  '{'
    return t

def T_RBRACE(t):
    r'\}'
    t.type =  '}'
    return t

def T_LBRACKET(t):
    r'\['
    t.type =  '['
    return t

def T_RBRACKET(t):
    r'\]'
    t.type =  ']'
    return t

def T_DPOINTS(t):
    r'\:'
    t.type =  ':'
    return t


def t_COMMENT_LINES(t):
    r'(/\* .* \*/) | (//.*)'
    pass

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID') # Check for reserved words
    return t

def t_STRING(t):
    r"\"+[a-zA-Z_]*\"+"
    t.value =  str(t.value)
    return t

# A regular expression rule with some action code
def t_REAL(t):
    r'\d*\.\d+'
    t.value = float(t.value)
    return t   
# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
expression = ' les /*ASDAS*/ // asd'
#Gerar os tokens da análise lexica
lexer.input(expression);
print("-----------------------")
while True:
    tok = lexer.token()
    if not tok:
        break #não possui mais tokens
    print(tok)