"""
Predictive parser for the example arithmetic grammar

Key idea: every production rule will get one function in the parser
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

def term_prime(tokens):
  """
  term_prime --> * factor term_prime | empty
  """

  # First case: next token in sequence is a MULTIPLY
  if len(tokens) > 0 and tokens[0].type == 'MULTIPLY':
    match(tokens, 'MULTIPLY')
    factor(tokens)
    term_prime(tokens)

  # Otherwise, this term_prime is empty, return without doing anything

def expr_prime(tokens):
  """
  expr_prime --> + term expr_prime | empty
  """

  # First case: next token in sequence is a PLUS
  if len(tokens) > 0 and tokens[0].type == 'PLUS':
    match(tokens, 'PLUS')
    term(tokens)
    expr_prime(tokens)

  # Otherwise, this expr_prime is empty, do nothing


def expr(tokens):
  """
  This functions parses an expression

  expr --> term expr_prime
  """

  # Call the functions that correspond to the
  # right-hand side of the production
  term(tokens)
  expr_prime(tokens)


def parse(tokens):
  """
  Top-level method to parse an input token sequence
  """

  # Call the method to parse a top-level expr
  expr(tokens)

  # If parsing succeeds, then the sequence of tokens should be
  # empty after expr returns
  #
  # Every token should be matched during the parsing process
  if len(tokens) > 0:
    print('Parsing failed.')
    print('Unmatched token', tokens[0])
    quit()
  

### Main

# Turn an input string into its sequence of tokens
tokens = lexer.analyze('9 + 2 * +')
for t in tokens:
  print(t)

# Parse the sequence of tokens
parse(tokens)
print('Parsing complete.')
