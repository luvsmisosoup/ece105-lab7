"""pso_v3.py: a particle swarm optimizer, version 3.

A Particle class holds one particle's state; the functions below it drive a swarm of particles.
Run it from a terminal:

    python pso_v3.py FUNCTION DIM SIZE XMIN XMAX MAX_ITER
    python pso_v3.py booth 2 20 -10 10 30

FUNCTION is booth, rastrigin or sphere. Each particle starts at a random point of the box
[XMIN, XMAX] in each of DIM coordinates. The seed is fixed (2021), so a run repeats exactly.
"""
import sys

import numpy as np


class Particle:
    """One particle: its position x, velocity v, best position so far (pbest), and the value of the
    function there (fitness)."""

    gidx = -1                   # class attribute: index of the swarm's best particle

    def __init__(self, dim, xmin, xmax):
        self.dim = dim
        self.xmin = xmin
        self.xmax = xmax
        self.x = np.random.uniform(xmin, xmax, dim)
        self.v = np.random.uniform(-abs(xmax - xmin), abs(xmax - xmin), dim)
        self.pbest = self.x.copy()
        self.fitness = np.inf

    def get_x(self):
        return self.x

    def get_fitness(self):
        return self.fitness

    def set_fitness(self, f):
        self.fitness = f

    def set_pbest(self):
        self.pbest = self.x.copy()

    def get_pbest(self):
        """The particle's best position so far."""
        return self.gbest

    def update(self, gbest):
        """One step: keep moving, plus a pull toward pbest and a pull toward gbest's best."""
        w, c1, c2 = 0.6, 1.49, 1.49
        vmax = abs(self.xmax - self.xmin)
        for i in range(self.dim):
            self.v[i] = (w * self.v[i]
                         + c1 * np.random.uniform(0, 1) * (self.pbest[i] - self.x[i])
                         + c2 * np.random.uniform(0, 1) * (gbest.pbest[i] - self.x[i]))
            if abs(self.v[i]) > vmax:
                self.v[i] = np.random.uniform(-vmax, vmax)
            self.x[i] = np.clip(self.x[i] + self.v[i], self.xmin, self.xmax)


def booth(x):
    """Booth's function, 2-D. Minimum 0 at (1, 3)."""
    return (x[0] + 2 * x[1] - 7) ** 2 + (2 * x[0] + x[1] - 5) ** 2


def rastrigin(x):
    """Rastrigin's function, any dimension. Minimum 0 at the origin, and many local minima."""
    n = len(x)
    return 10 * n + sum(x[i] ** 2 - 10 * np.cos(2 * np.pi * x[i]) for i in range(n - 1))


def sphere(x):
    """The sum of squares, any dimension. Minimum 0 at the origin."""
    return sum(xi ** 2 for xi in x)


FUNCTIONS = {"booth": booth, "rastrigin": rastrigin, "sphere": sphere}


def pso_init(function, size, dim, xmin, xmax):
    """A swarm of size particles, each one evaluated."""
    swarm = [Particle(dim, xmin, xmax) for _ in range(size)]
    if function not in FUNCTIONS:
        print("Unknown function")
        return []
    for p in swarm:
        p.set_fitness(FUNCTIONS[function](p.get_x()))
    return swarm


def pso_get_best(swarm):
    """Index of the particle with the lowest fitness; on a tie, the later particle."""
    min_value, g = np.inf, -1
    for idx, p in enumerate(swarm):
        if p.get_fitness() < min_value:
            min_value, g = p.get_fitness(), idx
        elif p.get_fitness() == min_value:
            g = idx
    return g


def pso_update(swarm):
    """Move every particle one step, toward the best particle's best position."""
    gbest = swarm[Particle.gidx]
    for p in swarm:
        p.update(gbest)


def pso_solve(function, swarm, max_iter, patience=20, tol=1e-6):
    """Run up to max_iter iterations. Return the index of the best particle and the list of best
    values, one per iteration. Stop early if, over the last patience iterations, the best value
    improved by less than the fraction tol."""
    f = FUNCTIONS[function]
    history = []
    for i in range(max_iter):
        for p in swarm:
            value = f(p.get_x())
            if value < p.get_fitness():
                p.set_fitness(value)
                p.set_pbest()
        gidx = pso_get_best(swarm)
        Particle.gidx = gidx
        history.append(float(swarm[gidx].get_fitness()))
        if len(history) > patience:
            old = history[-1 - patience]
            if (old - history[-1]) / old < tol:
                break
        pso_update(swarm)
    return gidx, history


def run_pso(function, dim, size, xmin, xmax, max_iter, seed=2021):
    """Run the optimizer. Return the best position found, its value, and the history."""
    np.random.seed(seed)
    swarm = pso_init(function, size, dim, xmin, xmax)
    if not swarm:
        raise RuntimeError("Error creating swarm")
    Particle.gidx = pso_get_best(swarm)
    gidx, history = pso_solve(function, swarm, max_iter)
    best = swarm[gidx]
    return best.pbest, best.get_fitness(), history


if __name__ == "__main__":
    function = sys.argv[1]
    dim, size = int(sys.argv[2]), int(sys.argv[3])
    xmin, xmax = float(sys.argv[4]), float(sys.argv[5])
    max_iter = int(sys.argv[6])
    x, value, history = run_pso(function, dim, size, xmin, xmax, max_iter)
    print(f"{function}: best x = {np.round(x, 4)}, f(x) = {value:.3g}, "
          f"iterations run: {len(history)}")
