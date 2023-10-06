import math

def solve(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b - discriminant**0.5) / (2*a)
    else:
        # Handling complex roots
        real_part = -b / (2*a)
        imag_part = (abs(discriminant)**0.5) / (2*a)
        x1 = complex(real_part, imag_part)
        x2 = complex(real_part, -imag_part)
    print(x1, x2)

# Test the function with the provided equations
solve(1, -6, 9)
solve(1, 2, -8)
solve(8, -6, -35)
solve(1, 0, 1)
