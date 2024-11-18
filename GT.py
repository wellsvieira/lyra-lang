import re
from lex import tokens
import sys
from enum import Enum
import ply.yacc as yacc


class DataType(Enum):
  INT = -1
  ARRAY = 0
  MATRIX = 1


class StackItem:

  def __init__(self, name, address, column):
    self.name = name
    self.address = address
    self.column = column


class Stack:

  def __init__(self):
    self.items = {DataType.INT: [], DataType.ARRAY: [], DataType.MATRIX: []}

  def push(self, dataType: DataType, name, address, column):
    item = StackItem(name, address, column)
    self.items[dataType].append(item)

  # Funções que podem ser úteis no futuro
  def pop(self, dataType: DataType):
    if not self.is_empty(dataType):
      return self.items[dataType].pop()
    return None

  def is_empty(self, dataType: DataType):
    return len(self.items[dataType]) == 0

  def peek(self, dataType: DataType):
    if not self.is_empty(dataType):
      return self.items[dataType][-1]
    return None

  def size(self, dataType: DataType):
    return len(self.items[dataType])


def p_program(p):
  'Program : Body'
  print(p[1])


def p_program_declares_body(p):
  'Program : Declares Body'
  p[0] = p[1] + p[2]
  print(p[0])


def p_program_declares(p):
  'Program : Declares'
  p[0] = p[1]
  print(p[0])


def p_declares_declare(p):
  'Declares : Declare'
  p[0] = p[1]


def p_declares_declares(p):
  'Declares : Declares Declare'
  p[0] = p[1] + p[2]


def p_declare(p):
  'Declare : INT NAME'
  if p[2] not in [item.name for item in stack.items[DataType.INT]]:
    stack.push(DataType.INT, p[2], parser.address, False)
    p[0] = "PUSHI 0\n"
    parser.address += 1
  else:
    p[0] = "Erro, variavel já declarada"
    parser.success = False


def p_declare_atr(p):
  'Declare : INT NAME ATR NUM'
  if p[2] not in [item.name for item in stack.items[DataType.INT]]:
    stack.push(DataType.INT, p[2], parser.address, False)
    p[0] = "PUSHI " + p[4] + "\n"
    parser.address += 1
  else:
    p[0] = "Erro, variavel já declarada"
    parser.success = False


def p_declare_array(p):
  'Declare : ARRAY NAME LSBRACKET NUM RSBRACKET'
  if p[2] not in [item.name for item in stack.items[DataType.ARRAY]]:
    stack.push(DataType.ARRAY, p[2], parser.address, False)
    parser.address += int(p[4])
    p[0] = "PUSHN " + str(p[4]) + "\n"
  else:
    p[0] = "Erro, variavel já declarada"
    parser.success = False

def p_declare_array_atr(p):
  'Declare : ARRAY NAME LSBRACKET NUM RSBRACKET ATR LPAREN List RPAREN'
  list_values = re.findall(r'\d+', p[8])
  if (len(list_values) == int(p[4])):  
    if p[2] not in [item.name for item in stack.items[DataType.ARRAY]]:
      stack.push(DataType.ARRAY, p[2], parser.address, False)
      parser.address += int(p[4])
      p[0] = p[8]
    else:
      p[0] = "Erro, variavel já declarada"
      parser.success = False
  else:
    p[0] = "Erro, tamanho da lista não corresponde ao tamanho do array"
    parser.success = False

def p_declare_matrix(p):
  'Declare : MATRIX NAME LSBRACKET NUM RSBRACKET LSBRACKET  NUM RSBRACKET'
  if p[2] not in [item.name for item in stack.items[DataType.MATRIX]]:
    stack.push(DataType.MATRIX, p[2], parser.address, p[7])
    size = int(p[4]) * int(p[7])
    p[0] = "PUSHN " + str(size) + "\n"
    parser.address += size
  else:
    p[0] = "Erro, variavel já declarada"
    parser.success = False



def p_declare_matrix_atr(p):
  'Declare : MATRIX NAME LSBRACKET NUM RSBRACKET LSBRACKET  NUM RSBRACKET ATR LPAREN ListOfLists RPAREN'
  list_values = re.findall(r'\d+', p[11])
  if (len(list_values) == int(p[4]) * int(p[7]) and len(list_values)/int(p[7]) == int(p[4])):
    if p[2] not in [item.name for item in stack.items[DataType.MATRIX]]:
      stack.push(DataType.MATRIX, p[2], parser.address, p[7])
      size = int(p[4]) * int(p[7])
      p[0] = p[11]
      parser.address += size
    else:
      p[0] = "Erro, variavel já declarada"
      parser.success = False
  else:
    p[0] = "Erro, tamanho da lista não corresponde ao tamanho da matriz"
    parser.success = False

def p_list_rec(p):
  'List : NUM COMMA List' 
  p[0] = "PUSHI " + p[1] + "\n" + p[3]

def p_list_num(p):
  'List : NUM'
  p[0] = "PUSHI " + p[1] + "\n"

def p_list_of_lists_rec(p):
  'ListOfLists : LPAREN List RPAREN COMMA ListOfLists'
  p[0] = p[2] + p[5]

def p_list_of_lists(p):
  'ListOfLists : LPAREN List RPAREN'
  p[0] = p[2]


def p_body_statement(p):
  'Body : Statement'
  p[0] = p[1]


def p_body_body_statement(p):
  'Body : Body Statement'
  p[0] = p[1] + p[2]


def p_statement_attribution(p):
  'Statement : Attribution'
  p[0] = p[1]


def p_statement_if(p):
  'Statement : If'
  p[0] = p[1]


def p_statement_while(p):
  'Statement : While'
  p[0] = p[1]


def p_statement_write(p):
  'Statement : Write'
  p[0] = p[1]


def p_attribution_name_atr(p):
  'Attribution : NAME ATR Expression'
  if p[1] not in [item.name for item in stack.items[DataType.INT]]:
    p[0] = "Erro, variavel não declarada"
    parser.success = False
  else:
    for item in stack.items[DataType.INT]:
      if item.name == p[1]:
        older_address = item.address
    p[0] = p[3] + "STOREG " + str(older_address) + "\n"


def p_attribution_name_exp_atr_exp(p):
  'Attribution : NAME LSBRACKET Expression RSBRACKET ATR Expression'
  if p[1] not in [item.name for item in stack.items[DataType.ARRAY]]:
    p[0] = "Erro, variavel não declarada"
    parser.success = False
  else:
    for item in stack.items[DataType.ARRAY]:
      if item.name == p[1]:
        older_address = item.address
    p[0] = "PUSHGP\n" + "PUSHI " + str(
        older_address) + "\n" + "PADD\n" + p[3] + p[6] + "STOREN\n"


def p_attribution_name_exp_exp_atr_exp(p):
  'Attribution : NAME LSBRACKET Expression RSBRACKET LSBRACKET Expression RSBRACKET ATR Expression'
  if p[1] not in [item.name for item in stack.items[DataType.MATRIX]]:
    p[0] = "Erro, variavel não declarada"
    parser.success = False
  else:
    for item in stack.items[DataType.MATRIX]:
      if item.name == p[1]:
        older_address = item.address
        older_column = item.column
    p[0] = "PUSHGP\n" + "PUSHI " + str(
        older_address) + "\n" + "PADD\n" + p[3] + "PUSHI " + str(
            older_column) + "\n" + "MUL\n" + p[6] + "ADD\n" + p[9] + "STOREN\n"


def p_attribution_name_atr_read(p):
  'Attribution : NAME ATR READ'
  if p[1] not in [item.name for item in stack.items[DataType.INT]]:
    p[0] = "Erro, variavel não declarada"
    parser.success = False
  else:
    for item in stack.items[DataType.INT]:
      if item.name == p[1]:
        older_address = item.address
    p[0] = "READ\n" + "ATOI\n" + "STOREG " + str(older_address) + "\n"


def p_attribution_name_exp_atr_read(p):
  'Attribution : NAME LSBRACKET Expression RSBRACKET ATR READ'
  if p[1] not in [item.name for item in stack.items[DataType.ARRAY]]:
    p[0] = "Erro, variavel não declarada"
    parser.success = False
  else:
    for item in stack.items[DataType.ARRAY]:
      if item.name == p[1]:
        older_address = item.address
    p[0] = 'PUSHGP\n' + 'PUSHI ' + str(older_address) + '\n' + 'PADD\n' + p[
        3] + 'READ\n' + 'ATOI\n' + 'STOREN\n'


def p_attribution_name_exp_exp_atr_read(p):
  'Attribution : NAME LSBRACKET Expression LSBRACKET Expression RSBRACKET ATR READ'
  if p[1] not in [item.name for item in stack.items[DataType.MATRIX]]:
    p[0] = "Erro, variavel não declarada"
    parser.success = False
  else:
    for item in stack.items[DataType.MATRIX]:
      if item.name == p[1]:
        older_address = item.address
        older_column = item.column
    p[0] = "PUSHGP\n" + "PUSHI " + str(
        older_adress) + "\nPADD" + "\n" + p[3] + "PUSHI " + str(
            older_column
        ) + "\nMUL" + "\n" + p[5] + "ADD\n" + "READ\n" + "ATOI\n" + "STOREN\n"


def p_if_condition(p):
  'If : IF LPAREN Condition RPAREN THEN Body END'
  p[0] = f'{p[3]}JZ label{p.parser.labels}\n{p[6]}label{p.parser.labels}: NOP\n'
  p.parser.labels += 1


def p_if_else(p):
  'If : IF LPAREN Condition RPAREN THEN Body ELSE Body END'
  p[0] = f'{p[3]}JZ label{p.parser.labels}\n{p[6]}JUMP label{p.parser.labels}f\nlabel{p.parser.labels}: NOP\n{p[8]}label{p.parser.labels}f: NOP\n'
  p.parser.labels += 1


def p_while_condition(p):
  'While : WHILE LPAREN Condition RPAREN DO Body END'
  p[0] = f'label{p.parser.labels}c: NOP\n{p[3]}JZ label{p.parser.labels}f\n{p[6]}JUMP label{p.parser.labels}c\nlabel{p.parser.labels}f: NOP\n'
  p.parser.labels += 1


def p_write_string(p):
  'Write : WRITES LPAREN STRING RPAREN  '
  p[0] = "PUSHS " + p[3] + "\n" + "WRITES\n"


def p_write_exp(p):
  'Write : WRITEI LPAREN Expression RPAREN'
  p[0] = p[3] + "WRITEI\n"


def p_expression_add(p):
  'Expression : Expression ADD Term'
  p[0] = p[1] + p[3] + "ADD\n"


def p_expression_sub(p):
  'Expression : Expression SUB Term'
  p[0] = p[1] + p[3] + "SUB\n"


def p_expression_or_term(p):
  'Expression : Expression OR Term'
  p[0] = p[1] + p[3] + "OR\n"


def p_expression_term(p):
  'Expression : Term'
  p[0] = p[1]


def p_term_mult(p):
  'Term : Term MULT Factor'
  p[0] = p[1] + p[3] + "MUL\n"


def p_term_div(p):
  'Term : Term DIV Factor'
  p[0] = p[1] + p[3] + "DIV\n"


def p_term_mod(p):
  'Term : Term MOD Factor'
  p[0] = p[1] + p[3] + "MOD\n"


def p_term_and_factor(p):
  'Term : Term AND Factor'
  p[0] = p[1] + p[3] + "AND\n"


def p_term_factor(p):
  'Term : Factor'
  p[0] = p[1]


def p_factor_num(p):
  'Factor : NUM'
  p[0] = "PUSHI " + p[1] + "\n"


def p_factor_variable(p):
  'Factor : Variable'
  p[0] = p[1]


def p_factor_paren_expr(p):
  'Factor : LPAREN Expression RPAREN'
  p[0] = p[2]

def p_factor_cond(p):
  'Factor : Condition'
  p[0] = p[1]

def p_factor_not_cond(p):
  'Factor : NOT LPAREN Condition RPAREN'
  p[0] = p[3] + "NOT\n"


def p_condition_greater(p):
  'Condition : Expression GREATER Expression'
  p[0] = p[1] + p[3] + "SUP\n"


def p_condition_less(p):
  'Condition : Expression LESS Expression'
  p[0] = p[1] + p[3] + "INF\n"


def p_condition_greatere(p):
  'Condition : Expression GREATERE Expression'
  p[0] = p[1] + p[3] + "SUPEQ\n"


def p_condition_lesse(p):
  'Condition : Expression LESSE Expression'
  p[0] = p[1] + p[3] + "INFEQ\n"


def p_condition_equal(p):
  'Condition : Expression EQUAL Expression'
  p[0] = p[1] + p[3] + "EQUAL\n"


def p_condition_nequal(p):
  'Condition : Expression NEQUAL Expression'
  p[0] = p[1] + p[3] + "EQUAL\n" + "NOT\n"


def p_condition_expr(p):
  'Condition : Expression'
  p[0] = p[1]


def p_variable_array(p):
  'Variable : NAME LSBRACKET Expression RSBRACKET'
  if p[1] not in [item.name for item in stack.items[DataType.ARRAY]]:
    p[0] = "Erro, variavel não declarada"
    parser.success = False
  else:
    for item in stack.items[DataType.ARRAY]:
      if item.name == p[1]:
        older_address = item.address
    p[0] = "PUSHGP\n" + "PUSHI " + str(older_address) + "\nPADD\n" + str(
        p[3]) + "LOADN\n"


def p_variable_matrix(p):
  'Variable : NAME LSBRACKET Expression RSBRACKET LSBRACKET Expression RSBRACKET'
  if p[1] not in [item.name for item in stack.items[DataType.MATRIX]]:
    p[0] = "Erro, variavel não declarada"
    parser.success = False
  else:
    for item in stack.items[DataType.MATRIX]:
      if item.name == p[1]:
        older_address = item.address
        older_column = item.column
    p[0] = "PUSHGP\n" + "PUSHI " + str(
        older_address) + "\nPADD\n" + p[3] + "PUSHI " + str(
            older_column) + "\nMUL\n" + p[6] + "ADD\n" + "LOADN\n"


def p_variable(p):
  'Variable : NAME'
  for item in stack.items[DataType.INT]:
    if item.name == p[1]:
      older_address = item.address
  p[0] = "PUSHG " + str(older_address) + "\n"


def p_error(p):
  parser.success = False
  print('error')
  exit()


parser = yacc.yacc()
parser.success = True
parser.labels = 0
parser.address = 0
stack = Stack()
