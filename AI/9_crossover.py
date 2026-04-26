import random

# Step 1: Input chromosomes (decimal)
population = []
for i in range(6):
    num = int(input(f"Enter chromosome {i+1} (decimal): "))
    binary = format(num, '04b')   # convert to 4-bit binary
    population.append(binary)

print("\nInitial Population:", population)

# Step 2: Crossover
crossover_rate = 0.25
pairs = [(0,1), (2,3), (4,5)]

for i, j in pairs:
    if random.random() < crossover_rate:
        point = random.randint(1, 3)  # crossover point

        print(f"\nCrossover between {population[i]} and {population[j]} at point {point}")

        p1 = population[i][:point] + population[j][point:]
        p2 = population[j][:point] + population[i][point:]

        population[i], population[j] = p1, p2

# Step 3: Output
print("\nFinal Population after Crossover:", population)
