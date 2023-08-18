# Sprint 1 Deliverables

## Writing logical statements



## Truth

1. Let *h* = "Maria is healthy", *w* = "Maria is wealthy", and *z* = "Maria is wise." Write each of the following compound statements:

- Maria is healthy and wealthy but not wise.
- Maria is not healthy but she is wealthy and wise.
- Maria is neither healthy, wealthy, nor wise.
- Maria is neither healthy nor wise, but she is wealthy.
- Maria is wealthy, but she is not both healthy and wise.

2. Draw a truth table for each of the following statements:

- *p* ∧ ¬*q*
- *p* ∨ (*q* ∧ ¬*r*)
- ¬(*p* ∧ *q*)
- *p* ∧ ¬(*q* → *r*)
- (*p* → (*q* → *r*)) ↔ ((*p* ∧ *q*) → *r*


## Laws

3. Prove that (¬*p* ∨ *q*) ∨ (*p* ∧ ¬*q*) is a tautology by

- Using a truth table.
- Using the laws of Boolean algebra


4. The equivalences *p* ∨ (*p* ∧ *q*) ≡ *p* and *p* ∧ (*p* ∨ *q*) ≡ *p* are often known as the
*Absorption Laws* of Boolean Algebra. Using other Boolean Algebra laws, prove that
these equivalences are true.

5. Use a truth table to verify that

- A conditional statement is not logically equivalent to its inverse.
- A conditional statement and its contrapositive are logically equivalent.

## Data representations

6. Convert the following numbers from decimal to binary. Show your work.

- 10
- 31
- 66
- 201
- 2769

7. Convert the following from binary to hexadecimal. Tip: divide each number into nibble-sized chunks, then convert each nibble into its hex equivalent.

- 1101
- 10011011
- 111100111011
- 1010011111000001

8. Compute the following bitwise operations. Give your answers in hexadecimal and show your work:

- `0xC7 | 0xA8`
- `0xC7 & 0xA8`
- `~0xC7`
- `0xC7 ^ 0xA8` (where ^ is the exclusive-or operator)


## Sets

9. Let the set *A* = {*a*, *b*, *c*} and set *B* = {*c*, *d*, *e*}. Find the following:

- |*A*|
- *P*(*A*)
- |*P*(*A*)|
- *A* x *B*
- *A* ∪ *B*
- *A* ∩ *B*
- *A* - *B*
- *B* - *A*

10. Let *A* = {2, 4, 6}, *B* = {6, 2, 4}, and *C* = {1, 2, 3, 4}. Mark each statement below as true or false; if a statement is false, provide a brief explanation why.

- *A* ⊆ *B*
- *B* ⊆ *A*
- *A* ⊄ *C*
- *A*  ⊆ *C*
- *B* ⊄ *A*

## Code

11. Consider the two different code fragments below.

```
if (1 < x && x < 5) {
  ...
}
```

```
if (!(x >= 1 || x <- 5)) {
   ...
}
```

Let *a* be the proposition `1 < x` and *b* be `x < 5`. Write logical statements corresponding to the two `if` statements, then, without using a truth table, prove that they're equivalent to each other.
