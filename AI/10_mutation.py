import random

# Convert to binary (fixed length)
def to_binary(num, bits=5):
    return format(num, f'0{bits}b')


def mutate(population, mutation_rate=0.1, bits=5):
    pop_size = len(population)

    # Convert to binary
    binary_pop = [list(to_binary(x, bits)) for x in population]

    total_bits = pop_size * bits
    num_mutations = int(total_bits * mutation_rate)

    print("Total bits:", total_bits)
    print("Number of mutations:", num_mutations)

    for _ in range(num_mutations):
        # Pick random chromosome and bit position
        i = random.randint(0, pop_size - 1)
        j = random.randint(0, bits - 1)

        # Flip bit
        old = binary_pop[i][j]
        binary_pop[i][j] = '1' if binary_pop[i][j] == '0' else '0'

        print(f"Mutated chromosome {i}, bit {j}: {old} → {binary_pop[i][j]}")

    # Convert back to integers
    new_population = [int("".join(bits), 2) for bits in binary_pop]

    return binary_pop, new_population


# Initial population
population = [3, 7, 12, 5, 9, 15]

print("Initial Population:", population)
print("Binary:", [to_binary(x) for x in population])

# Apply mutation
binary_after, new_population = mutate(population, 0.1)

print("\nAfter Mutation (Binary):", ["".join(b) for b in binary_after])
print("New Population:", new_population)