# Grammars and Programming Languages

## Due November 10

## You can work with a partner to complete this project

## Overview

We've spent the last couple of weeks working through some of the theory and tools of programming languages. In this project, you're going to use what you've learned to implement a lexical analyzer and parser for a small example programming language.

The next two challenge projects will both build on this project and ask you to add more features to the program.

Use the workspace on Repl.it:

- Complete `lexer.py` and `parser.py` according to the details below.
  
- Both are set up to take a file name as a command-line input for testing. For example, to run the parser on `test.pl`, use
```
python3 parser.py test.pl
```

- I've given you five test programs you can use to incrementally develop the parser.

- Write three more example programs that show three different failure examples. Name your programs `error1.pl`, `error2.pl`, and `error3.pl`.


## AI Guidelines

You can use Repl.it's built-in AI to help you. It's very good at completing blocks of statements, particularly if they're similar to previous statements. Tip: Use descriptive comments in your code to give the AI context. Read what it produces carefully: it may create solutions that are perfectly reasonable in isolation, but don't mesh with the rest of your implementation. Remember that you can also give it a prompt to describe what you want.

Don't use ChatGPT or similar tools for this project: you really need to develop incrementally and Repl.it's autocomplete AI is better for that.


## Example language grammar

Here's a grammar for the tiny language that we're going to be using for this project. It has elements of Python, Pascal, and the old-school BASIC language.

- Literal tokens are enclosed in single quotes.
- Capitalized words are synatactic variables.
- Curly braces indicate 0 or more copies of a statement
- Square brackets indicate 0 or 1 copies of a statement

Read this carefully! It looks long, but it's very similar to the previous examples we saw in class.

```
Program --> 'program' Name ':' Block 'end'

Block --> {Statement}

Statement --> PrintStatement
              | InputStatement
              | AssignStatement
              | IfStatement
              | WhileStatement
              | ForStatement
              
AssignStatement --> Name ':=' Expression

PrintStatement --> 'print' Expression

InputStatement --> 'input' Name
        
IfStatement --> 'if' Condition ':' Block [ElseClause] 'end'

ElseClause --> 'else' ':' Block
 
WhileStatement --> 'while' Condition ':' Block 'end'

RelOp --> '=' | '<>' | '>' | '<' | '>=' | '<='

ForStatement --> 'for' '(' Name ':=' Expression 'to' Expression ')' Statement

Condition --> Expression RelOp Expression

Expression --> Term [('+' | '-') Expression]

Term --> Factor [('*' | '/') MultExpr]

Factor --> '-' Factor
           | Atom
                        
Atom --> Name
         | Number
         | '(' Expression ')'
```


Here's an example program written in this language:

```
program test4:
  x := 10
  while x > 0:
    print x
    x := x - 1
  end
end
```

## Lexical Analyzer

Extend the lexical analyzer we built in class to recognize tokens for the example language above. Specifically, you need to recognize the following:

| Token       | Keyword or Symbol |
| ----------- | ----------- |
| `PROGRAM`      | `program`       |
| `END`      | `end`       |
| `PRINT`   | `print`        |
| `INPUT`   | `input`        |
| `IF`   | `if`        |
| `ELSE`   | `else`        |
| `FOR`   | `for`        |
| `TO`   | `to`        |
| `WHILE`   | `while`        |
| `COLON`   | `:`        |
| `PLUS` | '+' |
| `MINUS` | '-' |
| `MULTIPLY` | '*' |
| `DIVIDE` | '/' |
| `ASSIGN` | ':=' |
| `EQUALS` | '=' |
| `NOT_EQUAL` | '<>' |
| `LESS_THAN` | '<' |
| `GREATER_THAN` | '>' |
| `LESS_THAN_OR_EQUAL` | '<=' |
| `GREATER_THAN_OR_EQUAL` | '>=' |
| `LPAREN`   | `(`        |
| `RPAREN`   | `)`        |

There are two other tokens that have values:

| Token       | Value |
| ----------- | ----------- |
| `NAME`      | any non-keyword sequence of characters       |
| `NUMBER`    | sequence of 0-9 digits |


## Parser

Write a top-down predictive parser for the language grammar, using the one we built in class as a starting point.

Tip: use the structure of the grammar to guide your development.

- Each left-hand side nonterminal symbol corresponds to one function in the program
- Each terminal on the right-hand side corresponds to a call to `match` to identify that token
- Each nonterminal on the right-hand side corresponds to a call to that nonterminal's function

For example, the first rule yields a function like the following:

```
def program(tokens):
  """
  Program --> 'program' Name ':' Block 'end'
  """

  # Match the program keyword
  match(tokens, 'PROGRAM')

  # The name of the program
  match(tokens, 'NAME')

  # Colon
  match(tokens, 'COLON')

  # Call the block() function to process the statement block
  block(tokens)

  # Match the closing 'end'
  match(tokens, 'END')
```

The project workspace contains a starting parser with some example functions to help you get started. Your job is to fill out the rest of the function.
Work step-by-step! Consider writing small programs in the example language to test each new element that you add.


  

