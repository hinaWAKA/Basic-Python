import math

coefficients = [
    (1, -6, 9),
    (1, 2, -8),
    (8, -6, -35),
    (1, 0, 1)
]

# ループ
for i, (a, b, c) in enumerate(coefficients, start=1):
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b - discriminant**0.5) / (2*a)
    else:
        real_part = -b / (2*a)
        imag_part = (abs(discriminant)**0.5) / (2*a)
        x1 = complex(real_part, imag_part)
        x2 = complex(real_part, -imag_part)
    

    print(f"Equation #{i}: x1 = {x1}, x2 = {x2}")

