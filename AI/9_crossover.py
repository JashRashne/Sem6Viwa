import random

# Convert integer chromosome to binary (fixed length)
def to_binary(chromosome, bits=5):
    return format(chromosome, f'0{bits}b')


def crossover(population, crossover_rate=0.25):
    pop_size = len(population)
    num_cross = int(pop_size * crossover_rate)

    # Ensure even number (pairing)
    if num_cross % 2 != 0:
        num_cross += 1

    # Select chromosomes randomly for crossover
    selected_indices = random.sample(range(pop_size), num_cross)

    print("\nSelected for Crossover:", selected_indices)

    new_population = population.copy()

    # Perform crossover in pairs
    for i in range(0, num_cross, 2):
        idx1 = selected_indices[i]
        idx2 = selected_indices[i + 1]

        p1 = new_population[idx1]
        p2 = new_population[idx2]

        # Convert to binary
        b1 = to_binary(p1)
        b2 = to_binary(p2)

        # Choose crossover point
        point = random.randint(1, len(b1) - 1)

        # Single-point crossover
        child1 = b1[:point] + b2[point:]
        child2 = b2[:point] + b1[point:]

        print(f"\nParents: {b1} , {b2}")
        print(f"Crossover Point: {point}")
        print(f"Children: {child1} , {child2}")

        # Convert back to integer
        new_population[idx1] = int(child1, 2)
        new_population[idx2] = int(child2, 2)

    return new_population


# Initial population (6 chromosomes)
population = [3, 7, 12, 5, 9, 15]

print("Initial Population:", population)
print("Binary Representation:", [to_binary(x) for x in population])

# Apply crossover
new_population = crossover(population, 0.25)

print("\nNew Population after Crossover:", new_population)
print("Binary Representation:", [to_binary(x) for x in new_population])