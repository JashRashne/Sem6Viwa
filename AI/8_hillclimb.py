import random
import math

# Choose function
def f(x, choice):
    if choice == 1:
        return math.sin(x)
    elif choice == 2:
        return -x**2
    elif choice == 3:
        return -5*x**2 + 3*x + 6


def hill_climbing(choice, start=None, step=0.1, max_iter=1000):
    if start is None:
        x = random.uniform(-10, 10)
    else:
        x = start

    for i in range(max_iter):
        current = f(x, choice)

        # neighbors
        left = f(x - step, choice)
        right = f(x + step, choice)

        # choose best neighbor
        if left > current:
            x = x - step
        elif right > current:
            x = x + step
        else:
            break  # no improvement → stop

    return x, f(x, choice)


# Input
print("Choose function:")
print("1. y = sin(x)")
print("2. y = -x^2")
print("3. y = -5x^2 + 3x + 6")

choice = int(input("Enter choice: "))

x_opt, y_opt = hill_climbing(choice)

print("\nOptimal x:", round(x_opt, 4))
print("Maximum y:", round(y_opt, 4))