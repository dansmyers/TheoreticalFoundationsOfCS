## Challenge Project 3: Finish the Interpreter

## Due 12/8

## You can work with a partner to complete this project

## Description

Complete the interpreter by implementing the `while` and `for` statements. In addition, add **one more new feature**, which can be whatever you want.

The basic strategy for the `while` loop is an extension of the `if` from the previous project: check the condition and decide whether to enter the loop or not. When the condition becomes `False`, skip around the body and advance to the next statement. To implement `while`, you'll need to keep track of the starting position in the token sequence, so you can return there and reëvaluate the condition to decide if you need to perform another iteration.

The `for` loop is a bit more complex, but uses the same approach:

- Determine the starting and ending values of the loop by evaluating the two expressions
- Initialize the loop index variable to the starting value (by assigning it in the symbol table)
- Execute the body, then increment the index variable
- Check if the index variable has exceeded the stopping value; if not, return back to the top and execute the body again

As in the `while` loop, you need to save the starting position in the token sequence so you can return back to it and execute the body again.

For your new feature, choose anything that you want to add, as long as it requires you add new code to the interpreter program. If you want to add a new type of statement or operator, you might need to also add new tokens to the lexer, which should be easy at this point.
