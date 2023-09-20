"""
Example of implementing a state machine model in Python

Key idea: actions of the state machine are determined
by the transition table that defines the automaton

Example: recognizing strings on {a, b} that have an even
number of a's

                   symbol
              'a'          'b'

        0      1            0
state 
        1      0            1

"""

# Represent the transition table as a dictionary
#
# Each tuple key represents a (current state, input symbol) pair
# Values are the next state associated with that pair
table = {}
table[(0, 'a')] = 1
table[(0, 'b')] = 0
table[(1, 'a')] = 0
table[(1, 'b')] = 1

start_state = 0

# List of accepting states
#
# If you had more than one accepting state, you could have multiple
# items in the list
accepting_states = [0]


def recognize(s):
  """
  Loop through the symbols of s and apply the rules
  of the transition table

  If, at the end, the model is in an accepting state,
  return True; otherwise return False
  """

  # Variable state keeps track of the current state of the model
  state = start_state

  # Loop over the symbols in the input string
  for symbol in s:
    # For the combination of (state, symbol) choose
    # the next state from the table
    next_state = table[(state, symbol)]
    print('%d\t%s\t%d' % (state, symbol, next_state))
    state = next_state

  # If the model ends in an accepting state, return True
  return state in accepting_states

### Main
print(recognize('aabba'))
