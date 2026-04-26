import random

# Fitness function
def fitness(ind):
    a, b, c, d = ind
    value = (a + 2*b + 3*c + 4*d)
    return 1 / (1 + abs(value - 30))


# Generate chromosome
def create_individual():
    return [random.randint(0, 10) for _ in range(4)]


# Initial population (6 chromosomes)
population = [create_individual() for _ in range(6)]

print("Initial Population:")
for ind in population:
    print(ind)

# One iteration (selection + crossover + mutation)
new_population = []

for i in range(0, 6, 2):
    p1 = population[i]
    p2 = population[i+1]

    # Crossover
    point = random.randint(1, 3)
    child1 = p1[:point] + p2[point:]
    child2 = p2[:point] + p1[point:]

    # Mutation
    for child in [child1, child2]:
        if random.random() < 0.1:
            idx = random.randint(0, 3)
            child[idx] = random.randint(0, 10)

    new_population.extend([child1, child2])

# Final population
print("\nFinal Population:")
for ind in new_population:
    print(ind)

# Best chromosome
best = max(new_population, key=fitness)

print("\nBest Chromosome:", best)
a, b, c, d = best
print("Value =", a + 2*b + 3*c + 4*d)