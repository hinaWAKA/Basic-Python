import math

def trapezoidal_integral(f, a=0, b=1, n=100):
    # 区間幅を計算
    h = (b - a) / n
    
    # 台形積分の初期値
    integral = 0.5 * (f(a) + f(b))
    
    # 区間内の中間点で関数を評価して積分値に加える
    for i in range(1, n):
        x_i = a + i * h
        integral += f(x_i)
    
    # 最終的な積分値を計算
    integral *= h
    
    return integral

# (1) 
result1 = trapezoidal_integral(math.sin, 0, math.pi / 2, 50)
print("(1):", result1)

# (2) 
def f2(x):
    return 4 / (1 + x**2)

result2 = trapezoidal_integral(f2, 0, 1, 100)
print("(2):", result2)

# (3) 
def f3(x):
    return math.sqrt(math.pi) * math.exp(-x**2)

result3 = trapezoidal_integral(f3, -100, 100, 1000)
print("(3):", result3)
