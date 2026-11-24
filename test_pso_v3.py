"""Tests for pso_v3.py. Run from this folder: pytest"""
import numpy as np

from pso_v3 import Particle, pso_get_best, run_pso


def test_booth_finds_minimum():
    x, value, history = run_pso("booth", 2, 20, -10, 10, 100)
    assert np.allclose(x, [1, 3], atol=1e-4)
    assert value < 1e-8


def test_one_iteration():
    """Issue 1: max_iter = 1 raised UnboundLocalError."""
    x, value, history = run_pso("booth", 2, 20, -10, 10, 1)
    assert len(history) == 1


def test_runs_every_iteration():
    """Issue 1: 30 iterations asked for, 29 run."""
    x, value, history = run_pso("booth", 2, 20, -10, 10, 30)
    assert len(history) == 30


def swarm_with(values):
    """Particles whose fitness values are the given numbers."""
    swarm = [Particle(2, 0, 1) for _ in values]
    for p, value in zip(swarm, values):
        p.set_fitness(value)
    return swarm


def test_tie_in_the_middle():
    """Issue 2: a tie for the lowest value gave the particle after it."""
    assert pso_get_best(swarm_with([3.0, 1.0, 1.0, 5.0])) == 2


def test_tie_at_the_end():
    """Issue 2: a tie at the last particle gave an index past the end."""
    assert pso_get_best(swarm_with([3.0, 1.0, 1.0])) == 2
