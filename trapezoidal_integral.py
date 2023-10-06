from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
import math

# Define
def f(x):
    return math.sin(x)

a = 0
b = 1/(2*math.pi)
N = 100
h = (b-a)/N

# the trapezoidal(台形) rule formula
I = 0.5*h*(f(a) + f(b) + 2*sum(f(a + k*h) for k in range(1, N)))

print(I)
