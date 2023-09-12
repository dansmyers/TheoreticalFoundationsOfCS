# Deterministic Finite Automata

We've spent the last few classes practicing working with DFAs. The goal of this assignment is to allow you to further practice working with these models, in preparation for our next unit, which will cover *non-deterministic* finite automata and the Pumping Lemma.

Review **Chapter 3** in the online text (the link is in the front-page syllabus).

## Submission

Make an account on replit.com if you haven't done so. I will send you a link to join the class workspace there, where you'll find a workspace for Assignment 2.

Use that workspace to complete the programming portions of the assignment. Upload your answers to the written questions into the workspace. Submit the workspace, using the button in the upper-right corner, when you're done.

## Questions

### More `grep`

Complete the `grep` lab in this directory if you haven't done so, then write regular expressions to answer the following using `words.txt`. Put all of your solutions in a file called `regex.txt`.

1. Find all the words that end with `zz`.

2. I'm thinking of a word that ends with `zz` and also contains another `z`. Write a regex to find that word.

3. I'm thinking of a word that has five consecutive vowels. What could it be?

4. Find all the words that contain no vowels and no `y`. Hint: use `^` and `$` to specify that the entire line must have no vowels.

5. Find all words that start and end with the same letter. Tip: use `^\(.\)` to capture the letter at the beginning of the word, then use `\1$` to check for that same letter at the end of the word. There can be any combination of letters in between the two.

6. Now I'm thinking of a seven-letter palindrome. Write a regex to find that word. 

### Finite Languages

1. Design a DFA over the alphabet {a, b, c, ..., z} that can recognize the string `love`, but no other string.

2. Next, design DFA that can recognize the language consisting of the two strings, {`love`, `cats`}, but no other strings.

3. Suppose you have a language that contains only a finite number of strings. Make an argument that this language must be regular.

### DFA Creation

Design DFAs to recognize the following languages over {*a*, *b*}.

1. All strings with zero or one *b*, but not more than one.

2. All strings that contain the substring *abba*.

3. All strings that contain more than two *a*'s and more than two *b*'s.

4. All strings that contain both *ab* and *ba* as substrings. The two substrings don't have to be consecutive. Assume that the same *b* doesn't appear in both substrings.

5. The number of *a*'s plus the number of *b*'s is even.

6. *aa*\* | *aba*\**b*\*

### Formalities

Consider the DFA defined by

{{*Q1*, *Q2*, *Q3*}, {*a*, *b*}, *t*, *Q1*, {*Q3*}}

The transition table *t* is:

```
      a     b
---------------
Q1 | Q2     Q1  
Q2 | Q3     Q1
Q3 | Q3     Q1
```

1. Draw a state diagram for this DFA.

2. Which of the following strings are accepted by the DFA? 
- *bbbaaab*
- *ababaaa*
- *bbaabaa*
- *baba*

3. In your words, describe the set of strings accepted by this automaton.

4. Write a regular expression for that set.

5. Implement a Python program with a function called `recognize` that takes a string as input, iterates through the state model using the characters in the string, and returns `True` if the string is accepted and `False` otherwise. Test your function on the examples in question 2.

