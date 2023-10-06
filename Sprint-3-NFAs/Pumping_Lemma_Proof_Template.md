# Pumping Lemma Proof Template

Goal: Prove that language *L* is not regular.

Strategy: Proof by contradiction.

We'll assume that *L* really is regular, which means it should obey the Pumping Lemma. We'll show, however, that there's at least one sufficiently long string in *L* that **can't** be pumped according to the rules of the lemma, which is a contradiction. Therefore, *L* can't really be regular.

### Step 1

State the following: "Assume that *L* really is regular. If so, the Pumping Lemma applies to it, and there is some length *n* such that any string *w* in *L* with length at least *n* can be divided into *x*, *y*, and *z* according to the lemma and pumped to create new strings that are also in *L*."

### Step 2

Choose one specific string in *L* that has length at least *n*.

Often, the best way to do this is to set all variable lengths in the language definition to *n*. The following steps will also be easier if the first *n* symbols of the string are all the same.

### Step 3

Argue, based on the rules of the lemma, that your chosen string can't be pumped.

- Use the fact that |*xy*| is at most *n* *(that is, *x* and *y* must be in the first *n* symbols of the string) to establish restrictions on *y*.
- Argue that there's some *m* for which *x* *y*<sup>*m*</sup> *z* is not in *L*.

Remember that you only need to find one counterexample.

## Step 4

"This is a contradiction! If *L* really is regular, then evert string with length *n* or greater can be pumped, but we've shown that there is at least one string that violates the Pumping Lemma. Therefore, our original assumption was false and *L* can't be regular."
