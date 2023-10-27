# Implement a basic lexical analyzer

# Create a class to represent a token
#
# The class will have fields that represent the properties
# of the token. For now, the only property we care about is
# type, but there will be other for certain kinds of tokens
class Token:
  def __init__(self, type, value=None):
    self.type = type
    self.value = value

  def __str__(self):
    """
    Return a string representation of this object's data
    """
    return '%s, %s' % (self.type, self.value)

def analyze(s):
  """
  Analyze input string s
  Return a list of the tokens identified in s
  """

  tokens = []

  next = 0
  while next < len(s):
    if s[next] == ' ':
      next += 1

    elif s[next] == '=':
      tokens.append(Token('EQUAL'))
      next += 1

    elif s[next] == '>':
      if next < len(s) - 1 and s[next + 1] == '=':
        tokens.append(Token('GREATER_THAN_OR_EQUAL'))
        next += 2
      else:
        tokens.append(Token('GREATER_THAN'))
        next += 1

    elif s[next] == '<':
      if next < len(s) - 1 and s[next + 1] == '=':
        tokens.append(Token('LESS_THAN_OR_EQUAL'))
        next += 2
      elif next < len(s) - 1 and s[next + 1] == '>':
        tokens.append(Token('NOT_EQUAL'))
        next += 2
      else:
        tokens.append(Token('LESS_THAN'))
        next += 1

    # Recognize arithmetic operators
    elif s[next] == '+':
      tokens.append(Token('PLUS'))
      next += 1
    
    elif s[next] == '-':
      tokens.append(Token('MINUS'))
      next += 1

    elif s[next] == '*':
      tokens.append(Token('MULTIPLY'))
      next += 1 

    elif s[next] == '/':
      tokens.append(Token('DIVIDE'))
      next += 1  

    
    elif s[next].isalpha():
      # Recognize identifiers
      identifier = s[next]
      next += 1
      while next < len(s) and s[next].isalnum():
        identifier += s[next]
        next += 1

      # Check for keyword matches
      if identifier == 'for':
        tokens.append(Token('FOR'))
      elif identifier == 'if':
        tokens.append(Token('IF'))
      elif identifier == 'else':
        tokens.append(Token('ELSE'))
      elif identifier == 'while':
        tokens.append(Token('WHILE'))
      else:
        tokens.append(Token('IDENTIFIER', identifier))
      
    # Add a case to check for numbers
    # Add a NUMBER token, made from a sequence of 0-9 characters
    # The value of the token is the int value of the number
    elif s[next].isdigit():
      # Recognize numbers
      number = s[next]
      next += 1
      while next < len(s) and s[next].isdigit():
        number += s[next]
        next += 1
      tokens.append(Token('NUMBER', int(number)))
      
  return tokens

if __name__ == 'main':
  """
  This code runs if lexer.py is the entry point for the program
  It doesn't run if lexer is imported from another file

  Standard strategy: put test code in a block like this
  """

  tokens = analyze('x = 2 * y + 1')
  for t in tokens:
    print(t)
