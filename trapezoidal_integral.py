import math

# 台形積分関数
def trapezoidal_integral(f, a=0, b=1, n=100):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s += f(a + i * h)
    return s * h

# (1) 
f1 = math.sin
a1, b1, n1 = 0, math.pi/2, 50
result1 = trapezoidal_integral(f1, a1, b1, n1)

# (2) 
f2 = lambda x: 4 / (1 + x**2)
a2, b2, n2 = 0, 1, 100
result2 = trapezoidal_integral(f2, a2, b2, n2)

# (3) 
f3 = lambda x: math.sqrt(math.pi) * math.exp(-x**2)
a3, b3, n3 = -100, 100, 1000
result3 = trapezoidal_integral(f3, a3, b3, n3)

print(f"(1) Result: {result1}")
print(f"(2) Result: {result2}")
print(f"(3) Result: {result3}")
