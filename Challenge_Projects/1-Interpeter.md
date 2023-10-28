# Challenge Project: Interpreter

## Due 12/8 (Friday after classes end)

## You can work with a partner to complete this project

## Description

This project is an extension of the parser project from Assignment 4. You're going to modify the parser to create an **interpreter** that actually executes programs.

The general interpretation strategy, discussed in more detail below, is to use the same top-down predictive approach as the parser, but, when a part of the program produces a value, **return that value** so it can be used by other parts of the program.

For this project, you need to implement the following features:

- `input` and `print` statements
- Variable assignments using the symbol table, discussed in more detail below
- Evaluating arithmetic expressions
- Write three more test programs of your own and modify the `main` section to read the program name from the command line, as in Assignment 4

You don't need to implement `if`, `while, or `for` statements. Those will be the goal of the second challenge project.


## AI

You can use the Repl.it autocomplete AI. Remember to think carefully about how its suggestions fit into the program.

## Submission and Grading

Use the workspace on Repl.it to complete your project. It includes `interpreter.py` to help you get started. Copy your `lexer.py` from Assignment 4.

This project is *optional*, but completing it will raise your final grade by one part of a letter, (e.g. B to B+, or B+ to A-). To get an A for the course, you need to complete all three challenge projects and the regular course work.

## Code

Start by completing Assignment 4. You need to do that before you work on this.

Look at `interpreter.py` in the project workspace. The overall structure should be familiar from the parser project. Each rule of the language grammar corresponds to a function in the program.

There are a few changes.

- Observe that `tokens` has now been moved to the top of the program to become a global, module-level variable. You can access it from any function without needing to pass it as a parameter.

- The `match` function has also changed. Our original version *consumed* each token it matched. The current version keeps all tokens in one list and uses an index called `next` to keep track of the next token in sequence. When `match` identifies a token, it increments `next`, but it doesn't delete any tokens. This change will be helpful when you're implementing loops in the next section.

The last major change is the **symbol table**, called `symbols` in the program. The symbol table is a dictionary that stores mappings from each variable name to its value. The example `input_statement` function I've given you shows how to use it to update the value of a variable:

```
def input_statement():
  """
  InputStatement --> 'input' Name
  """

  # Match the input token
  match('INPUT')

  # Get the variable name from the next token
  name = tokens[next].value
  match('NAME')

  # Read an input int
  print('Enter an integer value: ')
  value = int(input())

  # Assign that value to the variable name in the symbol table
  symbols[name] = value
```

Assignment statements will use the symbol table to update the value of a variable and expressions that contain variables will look up their values in the symbol table.

## Specific functions

Here's some information on the basic functions that are given as part of the starter code.

### `program`

This is straightforward and really just a wrapper around `block`.

### `block`

`block` is the primary method for representing a body of statements. A block can be any number of statements, so it repeatedly checks the next token. If the next token is the start of a statement (e.g., `input`, `print`, etc.) it calls the appropriate method to process that statement.

```
def block():
  """
  block --> {Statement}

  A block can be any number of statements. This function uses a
  loop that runs as long as the next token corresponds to the
  beginning of some statement.

  Extend this function to add calls to the different statement
  functions.
  """
  
  in_block = True

  while in_block:

    # The next token determines the statement type
    if check('INPUT'):
      input_statement()
    elif check('NAME'):
      assign_statement()
    else:
      in_block = False
```

You'll gradually extend this function to add more cases until you're processing all of the statements in the language.


### `atom`

An atom is a single value used in an expression. It's the bottom-level of the expression syntax. The starter code shows the case of getting a variable's value from the symbol table and returning it. You'll extend this to handle numbers and parenthesized expressions.

```
def atom():
  """
  Atom --> Name | Number | '(' Expression ')'

  Atom returns a single value used in an expression

  For variables, it looks up the variable's associated value
  in the symbol table

  For numbers, it returns the number value saved in the token

  For parenthesized expressions, it evaluates that expression and
  returns the result
  """

  # Return the value of a variable
  if check('NAME'):
    var = symbols[tokens[next].value]
    match('NAME')
    return var

  ### Add more cases to handle Number and ( Expression )
```

### `expression`, `term`, `factor`

These aren't written yet. You'll need to complete them to handle expression evaluations. At each step, you'll want to evaluate the relevant subparts, combine them in the appropriate way, then return the result so it can be used at the higher evaluation level. I'm being slightly vague here, because figuring out how this works is the main goal of the project.
