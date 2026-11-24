"""report.py: the five best particles of a run, for our group's weekly report.
Written by a teammate, on top of pso_v3.py. Run it: python report.py"""
import numpy as np

from pso_v3 import Particle, pso_get_best, pso_init, pso_solve


def by_fitness(p):
    return p.get_fitness()


np.random.seed(2021)
swarm = pso_init("booth", 20, 2, -10, 10)
Particle.gidx = pso_get_best(swarm)
gidx, history = pso_solve("booth", swarm, 50)
print(f"booth: 20 particles, {len(history)} iterations. The five best:")
for rank, p in enumerate(sorted(swarm, key=by_fitness)[:5], start=1):
    print(f"{rank}. f = {p.get_fitness():.3g} at {np.round(p.get_pbest(), 4)}")
