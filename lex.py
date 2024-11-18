'''
# Declarar variaveis:

| Declaração                                      | Comando          |
| ----------------------------------------------- | --------------   |
| Criar inteiro "x"                               | INT x            |
| Criar inteiro "x" com valor v                   | INT x = y        |
| Criar array de inteiros "a" de tamanho x        | ARRAY a x        |
| Criar matriz de inteiros "b" de tamanho x X y   | MATRIX b x y     |

# Operações aritméticas:

| Operação                                         | Comando     |
| ------------------------------------------------ | ----------- |
| Somar "x" e "y"                                  |  x + y      |
| Subtrair "y" a "x"                               |  x - y      |
| Multiplicar "x" por "y"                          |  x * y      |
| Dividir "x" por "y"                              |  x / y      |
| Calcular resto da divisao inteira de "x" por "y" |  x % y      |

# Operações Relacionais:

| Operação | Comando           |
| -------- | -------------     |
| x > y    | x > y             |
| x < y    | x < y             |
| x == y   | x == y            |
| x >= y   | x >= y            |
| x <= y   | x <= y            |
| x != y   | x != y            |

# Operações Lógicas:

| Operação                 | Comando   |
| ------------------------ | --------- |
| Negar "x"                |  not(x)   |
| Conjunção de "x" com "y" |  x && y   |
| Disjunção de "x" e "y"   |  x || y   |

# Atribuição:

| Atribuição                      | Comando  |
| ------------------------------- | -------  |
| Atribuir a "x" o valor de "y"   | x = y  |
| Atribuir a "x" um valor inteiro | x = 5  |

# IO:

| IO                                | Comando            |
| --------------------------------- | ----------         |
| Ler do stdin                      | READ               |
| Escrever o valor de "x" no stdout | WRITE(I ou S) x    |

# Controlo de fluxo:

Executar algo se "x" for verdadeiro

    IF (x) THEN
    ...
    END

Executar algo se "x" for verdadeiro, e outra coisa se "x" for falso

    IF (x) THEN
    ...
    ELSE
    ...
    END

# Ciclos:

Ciclo while-do

    WHILE (x) DO
    ...
    END

# Indexação: (i, j inteiros)

Aceder indice "i" de um array

    ARRAY i

Aceder indice "i","j" de uma matriz (matrix[ i ][ j ] em C)

    MATRIX i j

'''

import ply.lex as lex
import sys

tokens = ('NUM', 'NAME', 'INT', 'ARRAY', 'MATRIX', 'ADD', 'SUB', 'MULT', 'DIV',
          'MOD', 'GREATER', 'LESS', 'EQUAL', 'GREATERE', 'LESSE', 'NEQUAL',
          'NOT', 'AND', 'OR', 'ATR', 'READ', 'WRITEI', 'IF', 'WHILE', 'THEN',
          'ELSE', 'DO', 'END', 'LPAREN', 'RPAREN','LSBRACKET',           
          'RSBRACKET','WRITES','STRING','COMMA')

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LSBRACKET = r'\['
t_RSBRACKET = r'\]'
t_COMMA = r','

def t_NUM(t):
  r'\d+'
  return t


def t_INT(t):
  r'int'
  return t


def t_ARRAY(t):
  r'array'
  return t


def t_MATRIX(t):
  r'matrix'
  return t


def t_ADD(t):
  r'\+'
  return t


def t_SUB(t):
  r'\-'
  return t


def t_MULT(t):
  r'\*'
  return t


def t_DIV(t):
  r'\/'
  return t


def t_MOD(t):
  r'\%'
  return t


def t_GREATERE(t):
  r'>='
  return t


def t_GREATER(t):
  r'>'
  return t


def t_LESSE(t):
  r'<='
  return t


def t_LESS(t):
  r'<'
  return t


def t_EQUAL(t):
  r'=='
  return t


def t_NEQUAL(t):
  r'!='
  return t


def t_NOT(t):
  r'not'
  return t


def t_OR(t):
  r'\|\|'
  return t


def t_ATR(t):
  r'='
  return t


def t_READ(t):
  r'read'
  return t


def t_WRITES(t):
  r'writes'
  return t


def t_WRITEI(t):
  r'writei'
  return t


def t_THEN(t):
  r'then'
  return t


def t_ELSE(t):
  r'else'
  return t


def t_IF(t):
  r'if'
  return t


def t_WHILE(t):
  r'while'
  return t


def t_DO(t):
  r'do'
  return t


def t_END(t):
  r'end'
  return t


def t_AND(t):
  r'&&'
  return t


def t_NAME(t):
  r'[a-z]\w*'
  return t

def t_STRING(t):
  r'\"[^"]*\"'
  return t


t_ignore = ' \r\t\n'


def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)


lexer = lex.lex()

# Reading input
'''
for linha in sys.stdin:
  lexer.input(linha)
  tok = lexer.token()
  while tok:
    print(tok)
    tok = lexer.token()
'''
