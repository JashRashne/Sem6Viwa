import random

# Step 1: Input chromosomes (decimal)
population = []
for i in range(6):
    num = int(input(f"Enter chromosome {i+1} (decimal): "))
    binary = format(num, '04b')   # convert to 4-bit binary
    population.append(binary)

print("\nInitial Population:", population)

# Step 2: Mutation
mutation_rate = 0.10

for i in range(6):
    if random.random() < mutation_rate:
        bit_pos = random.randint(0, 3)

        print(f"\nMutation in {population[i]} at position {bit_pos}")

        # flip bit
        bit = '1' if population[i][bit_pos] == '0' else '0'
        population[i] = population[i][:bit_pos] + bit + population[i][bit_pos+1:]

# Step 3: Output
print("\nFinal Population after Mutation:", population)
