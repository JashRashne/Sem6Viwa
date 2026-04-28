import random

def f(x):
    return -5*x*x + 3*x + 6

x = int(input("Enter initial x: "))

for _ in range(100):
    nx = x + random.choice([-1,1])
    if f(nx) > f(x):
        x = nx

print("Best x:", x, "Value:", f(x))
