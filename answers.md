# Lab 7: answers

Your name:

For each issue, fill in Reproduce to Confirm **before** you change any code. Then fix it and test it.

## Issue 3: report.py crashes

- Reproduce (the command, and the last line it printed):
- Where (the lowest frame: file, line, and the code on that line):
- Hypothesis (one sentence):
- Confirm (an experiment of 1 to 3 lines, and what it printed):
- Fix (the line before, and after; which file?):
- Test (its name; it failed before the fix, and passes after):

## Issue 4: the sphere crashes on [0, 10]

- Reproduce (the command, and the last line it printed):
- Where (the lowest frame: file, line, and the code on that line):
- Hypothesis (one sentence): why is the number you divide by exactly 0?
- Confirm (an experiment of 1 to 3 lines, and what it printed):
- What should the early stop do when the best value is exactly 0, and stays 0?
- Fix (the line before, and after):
- Test (its name; it failed before the fix, and passes after):

## Issue 5: Rastrigin's answer is wrong

- Reproduce (the command, and what it printed):
- Expected (what, and why):
- Hypothesis (one sentence): is the swarm stuck, or is something else wrong?
- Confirm (an experiment of 1 to 3 lines, and what it printed):
- Fix (the line before, and after):
- Test (its name; it failed before the fix, and passes after):

## Three questions

1. Issue 3's bug was in `pso_v3.py` from the start, yet every run and all five of Wednesday's tests
   passed. Why?
2. Issue 4: how can the best value be exactly 0.0? Why does the same run on [-10, 10] never crash?
3. Issue 5: the user guessed a local minimum. What showed that the swarm was not stuck?
