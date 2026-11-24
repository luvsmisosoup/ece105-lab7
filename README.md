# Lab 7: debugging, with an AI tool

`pso_v3.py` is Wednesday's particle swarm optimizer (Lecture 15), with Wednesday's two fixes in it:
issues 1 and 2 are closed. Three more bug reports came in. Each one is below, as its writer sent it.
The writers' guesses about the cause may be wrong.

- `pso_v3.py`: the optimizer. `python pso_v3.py booth 2 20 -10 10 30` runs it.
- `test_pso_v3.py`: Wednesday's five tests. In this folder, run `pytest`: 5 passed. Add your tests here.
- `report.py`: a teammate's script, on top of `pso_v3.py`.
- `answers.md`: for each issue, what you ran, what you think, and how you checked it.
- `ai_log.md`: for each issue, what you asked the AI tool, and what it said.
- `.gitignore`: what Git should not track.

## Issue 3, from a teammate: report.py crashes

> I wrote `report.py` to list the five best particles for our weekly report. `python report.py`
> prints one line, then crashes with an `AttributeError`. `pso_v3.py` has worked for weeks, so the
> mistake must be in my script. Can you help?

## Issue 4, from a user: the sphere crashes on [0, 10]

> I only care about x >= 0, so I ran `python pso_v3.py sphere 2 20 0 10 100`. It crashes with a
> `ZeroDivisionError`. The same command on [-10, 10] works. Is 0 not allowed as a bound?

## Issue 5, from a user: Rastrigin's answer is wrong

> Rastrigin's function has its minimum, 0, at the origin (its docstring says so).
> `python pso_v3.py rastrigin 2 20 -5.12 5.12 100` says f(x) = 10 at x = [0, 1.6587]. I think the swarm
> gets stuck in a local minimum. More particles?

## The method (Lecture 15)

Reproduce. Read the traceback from the bottom up, or, with no traceback, say what you expected and what
you got. Ask the AI tool for a hypothesis. **Confirm it with a small experiment before you change any
code.** Then write a test that fails, make the smallest fix, and see the test pass.
