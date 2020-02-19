# -------------------------
# ExpressionLanguageLex.py
#----------------------

import ply.lex as lex

tokens = ('COMMA', 'SOMA', 'ID', 'NUMBER', 'VEZES', 'POT', 'LPAREN', 'RPAREN', 'IGUAL',)
t_IGUAL= r'='
t_SOMA = r'\+'
t_VEZES = r'\*'
t_POT = r'\^'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_ID = r'[a-zA-Z_][a-zA-Z_0-9]*'
t_ignore = ' \t'

def t_NUMBER(t):
  r'\d+'
  t.value = int(t.value)
  return t

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)
  
def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)
  
lexer = lex.lex()

# # Test it out
data = '''
fat ( wedson )
'''
lexer.input(data)