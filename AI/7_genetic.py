import random

def fitness(ch):
    a,b,c,d = ch
    return (a + 2*b + 3*c + 4*d) - 30

population = []

for i in range(6):
    ch = list(map(int, input(f"Chromosome {i+1} (4 values): ").split()))
    population.append(ch)

print("Initial:", population)

population.sort(key=fitness, reverse=True)

print("Final:", population)
print("Best:", population[0])
