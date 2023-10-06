# Pumping Lemma Proof Template

Goal: Prove that language *L* is not regular.

Strategy: Proof by contradiction.

We'll assume that *L* really is regular, which means it should obey the Pumping Lemma. We'll show, however, that there's at least one sufficiently long string in *L* that **can't** be pumped according to the rules of the lemma, which is a contradiction. Therefore, *L* can't really be regular.

# Step 1

State the following: "Assume that *L* really is regular. If so, the Pumping Lemma applies to it, and there is some length *n* such that any string *w* in *L* with length at least *n* can be divided into *x*, *y*, and *z* according to the lemma and pumped to create new strings that are also in *L*."

This establishes the 
