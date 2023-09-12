# Regular Expressions

This short lab will let you practice using regular expressions with `grep`, a standard Unix program for searching files.

## Now You Have Two Problems

There's a famous programming joke:

```
You need to solve a problem. You decide to use regular expressions. Now you have two problems.
```

`grep` is short for *globally search a regular expression and print*. Its basic use case takes two arguments:

- A regular expression
- A file name
    
`grep` searches the target file for any strings matching the pattern described by the regular expression and prints them to the screen.

### Wordlist

Do this lab in the workspace I've created for you. The workspace contains a file named `words.txt` that contains a large number of words taken from crossword puzzle solutions.

### Searching for a substring

The simplest `grep` case is to search target file for a specified substring. Run the following command **at the shell prompt**.

```
grep "cat" words.txt
```

The first argument is the search string enclosed in quotes. It isn't strictly required to use quotes with every regex string, 
but some complex patterns require it, so I like to use it as a default. You could also enclose the string in single quotes.

The second argument is the complete path to the dictionary file. In this case, `words.txt` is in the local directory, so we can type its name without specifying an entire path.

The command prints all words in the file containing the string `cat`. This is a lot of words! Other substring choices may yield fewer results:

```
grep "platypus" words.txt
```

**Question: Find all the words that contain two consecutive `a`'s. Are there any words that contain three consecutive `a`'s?**

### Matching beginnings and endings

Use the `^` symbol to denote the beginning of a line. Patterns that start with `^` will only be matched if they occur at the beginning of the line. To find all words that begin with `x`:

```
grep "^x" words.txt
```

**Question: Find all the words that begin with `q`.**

Use `$` to match the end of a line. To find all of the words that end with `esses`:

```
grep "esses$" words.txt
```

**Question: Find all the words that end with `ingly`.**

If you combine both `^` and `$`, you can specify a line that must be matched exactly:

```
grep "^platypus$" words.txt
```

### Character sets

`grep` becomes more powerful when you allow it to match patterns that contain multiple options. Sets of characters are enclosed in square brackets. For example,

- `[aeiou]` is the set of lowercase vowels
    
- `[aeiouAEIOU]` is the set of lowercase and uppercase vowel characters

- `[a-zA-Z0-9]` is the compact way or writing the set of all lowercase letters, uppercase letters, and digits
    
When you give `grep` a character set, it's allowed to match any of the options that occur within the set. For example, find all the words in the wordlist that start with `q` but not `qu`:

```
grep "^q[aeio]" words.txt
```

Questions like the previous one can be made easier by using `^` as the first symbol in a set, which matches everything *except* the
characters in the set:

- `[^aeiou]` is the set of all characters *except* the lowercase vowels
    
- `[^a-z]` is the set of all characters *except* the lowercase letters
    
This is tricky! The `^` symbol has two different meanings depending on how you use it. *Outside* the square braces it signifies the beginning of the line; *inside* the braces it represents an excluded character set.

Find all the words that contain characters other than a normal lowercase or uppercase letter:

```
prompt$ grep "[^a-zA-Z]" words.txt
```
    
**Question: Find all the words that start with `q` but not `qu` using the exclusionary character set approach**.

### Kleene closure

Use `*` to match 0 or more instances of a pattern. This is often combined with `.` as a generic placeholder that can match any character. `.*` is therefore a wildcard that matches any number (including zero) of arbitrary characters.

Find the words of any length that start with `q` and end with `ing`. This example shows off using both `^` and `$` to match the beginning and ending of a line, with arbitrary characters in between:

```
grep "^q.*ing$" words.txt
```

**Question: I'm thinking of a word that starts with `he` and ends with `he`. What could it be?**

**Question: Find all the words that contain no vowels. Hint: use `^` and `$` to specify that the entire line must have no vowels.**

### Repeating

The syntax `\{n\}` lets you repeat a pattern `n` times. This is a little weird. The `\` functions as an escape character to indicate
that you're using `{` and `}` as control characters, rather than the literal left and right brace characters. This is one of the
frustrating things about regular expressions: some control characters, like `*`, are used as-is, but others need the special 
backslash escape prefix.

Find all the words with 4 vowels:

```
grep "[aeiou]\{4\}" words.txt
```

**Question: Find all the words with 5 consecutive consonants, then find the words with the most consecutive consonants by trying larger values of `n`.**

### Union

Use `\|` to match one of a set of options. Again, the use of the `\` is obnoxious. Find all the words that start or end with `x`:

```
grep "^x\|x$" words.txt
```

Parentheses `\(` and `\)` can be used to group expressions. For example, to match all words starting with either `aa` or `ee`:

```
grep "^\(aa\|ee\)" words.txt
```

### Pain

Here's one last advanced regex feature. If you enclose a pattern in parentheses, the string that matches that pattern is said to
be "captured". The evaluator will keep track of the captured pattern in case you want to refer to it later, which you can do using 
`\1`. For example, match any words having double letters:

```
grep "\(.\)\1" words.txt
```

The parentheses grouping `\(.\)` matches any character. The `\1` then requires the analyzer to match whatever character was captured
during the evaluation of the parenthesis expression. Note that this could not be acheived by using `[a-z]\{2\}`. Try it out if you're unsure why.

What if we wanted to match words with consecutive pairs of double letters? Use a second pair of parentheses to capture a second letter, 
then match it a second time with `\2`:

```
grep "\(.\)\1\(.\)\2"
```

I'm thinking of a word that has three consecutive pairs of double letters:

```
grep "\(.\)\1\(.\)\2\(.\)\3"
```

This example also illustrates how the regex evaluators contained in real programming environments are more powerful than the default
theoretical model of regular expressions, which assumed that we had no available memory for elements of the string and therefore
couldn't keep track of anything.

**Question: Print all the words in the list that contain a doubled vowel.**

**Question: Are there any words in the list that have the same letter occurring three times in a row?***

## Wrap-Up

This is really just a cursory overview of the features of `grep` and regular expressions in Unix. A few final notes:

- I do not expect you to memorize the syntax for regular expressions.
    
- There are actually a few different syntaxes in circulation; the Perl language has its own built-in regex evaluator with its own syntax.
    
- The general answer to questions about pattern matching, substring replacement, etc. is "Use 'grep' and regular expressions."
