# Challenge Project 2: Conditions

## Due 12/8

## You can work with a partner to complete this project

## Description

Continue working on the "Pyscal" interpreter. Your goal for this project is to implement the `if` statement. That's it.

Finish Challenge Project 1 before doing this one. You don't have to write that much code, but you **must** understand how the interpreter interacts with the token sequence to be able to implement conditional blocks.

## Tips

The basic strategy for the `if` statement is to first evaluate the condition, then based on that result, determine whether you should execute its internal `block` or skip it. 

```
if x < 0:
  x := 1
else:
  x := -1
end
```

Start by implementing `condition`:

  - Evaluate the left-hand expression and save its value
  - Determine the relational operator and record what it is
  - Evaluate the right-hand expression and save its value
  - Use the given operator to compare the two expression values and return `True` or `False` as the result of `condition`

If the condition is `True`, simply continue forward and execute the `block`. If it's `False`, you need to **skip ahead** in the token sequence until you reach either the matching `end` token (signaling that you've reached the end of the `if` statement), or an `else` token, in which case you execute the `else` block. The basic version of this action is straightforward: use a loop to scan through the token list until you reach either `else` or `end`.

It gets complicated, though, if you have to deal with **nested `if` statements**.

```
if x = 0:
  if y = 0:
    print x
    print y
  end
end
```

If you're trying to skip the first `if` statement, you can't simply look for a single `end`, because that might be the `end` of an internal `if` statement, rather than the outer `if` statement.

- When you need to skip a block, initialize a counter called `depth` that's set to zero
- As you scan through the block, look for any `if`, `for`, or `while` declarations. Every time you see one, increment `depth`
- When you see an `end`, decrement `depth`
- If you see an `end` or `else` and have `depth == 0`, then it corresponds to the real end of the outer `if` statement

## Testing

Write test programs (with the `.p` extension) in your workspace to show that your code works. Make sure you have one that shows you can handle `if`-`else` structures and one that shows you can handle nested `if` statements.
