"""
Write a predictive parser for the example arithmetic grammar

Key idea: every production rule will get one function
in the parser
"""

import lexer


def match(tokens, expected):
  """
  Check if the next token matches what's expected

  If so, remove that token from the front
  If not, print and error and quit
  """
  if len(tokens) == 0:
    print("Unexpected end of input")
    quit()
  
  if tokens[0].type != expected:
    print("Expected", expected, "got", tokens[0].type)
    quit()

  # Remove the first token, advance to the next token
  tokens.pop(0)


def factor(tokens):
  """
  factor -> ( expr )  | number
  """

  if tokens[0].type == 'LPAREN':
    match(tokens, 'LPAREN')
    expr(tokens)
    match(tokens, 'RPAREN')
  else:
    match(tokens, 'NUMBER')


def term(tokens):
  """
  term -> factor term_prime
  """

  # Calling functions for each thing on the right side
  factor(tokens)
  term_prime(tokens)


def expr(tokens):
  """
  This functions parses an expression
  """

  # Call the functions that correspond to the
  # right-hand side of the production
  term(tokens)
  expr_prime(tokens)


### Main

# The input to the parser is a sequence of tokens produced by the
# lexical analyzer
tokens = lexer.analyze('9 + 2 * 5')
for t in tokens:
  print(t)
