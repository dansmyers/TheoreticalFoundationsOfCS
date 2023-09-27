# Nondeterministic Finite Automata and the Pumping Lemma

## Due 10/6

## Overview

This is a short assignment to let you practice proofs using the Pumping Lemma and constructing NFAs.

The second part includes some tips and practice questions on preparing for the midterm, which will be on October 4. **You do not have to submit the review questions**.


## Pump

1. Consider the language *L* on {*a*, *b*} consisting of strings with the form *ww*, where *w* is any string of *a*'s and *b*'s. That is, *L* consists of strings formed from two consecutive identical copies of a substring of *a*'s and *b*'s. For example, *abab*, *abbaabba*, and *bbababbaba* are all in this language. Use the Pumping Lemma to prove that this language is not regular.

2. Prove that *L* = {0<sup>i</sup> 1<sup>j</sup> 0<sup>i + j</sup>; *i*, *j* ≥ 0} is not regular.

Tips:

- Use the script for Pumping Lemma proofs. You **do** need to write out the starting and ending paragraphs beacuse they're part of the proof. [The forms must be obeyed](https://dune.fandom.com/wiki/Great_Convention).

- Find one specific string *s* that has length at least *n* to use for your contradiction. It's not required, but helpful, if *s* starts with *n* copies of the same character.

- Once you've identified a candidate *s*, reason about the *x*, *y*, and *z* pieces required by the Lemma. See if you can establish restrictions on *y*.

- Then find one specific value of *m* that makes *x* *y*<sup>*m*</sup> *z* not part of the language. This is the contradiction that you need to show that *s* cannot be pumped.

## Construction

Use the NFA construction algorithm to build machines that recognize the following regular expressions. You don't have to perform any simplification of the resulting NFAs.

1. *a*<sup>\*</sup>*b*<sup>\*</sup>

2. (*aa* | *bb*) (*ab* | *ba*)

3. *a* *b*<sup>\*</sup> *a* *b*<sup>\*</sup>

4. (*a*|*b*)<sup>\*</sup> | (*c*|*d*)<sup>\*</sup>
