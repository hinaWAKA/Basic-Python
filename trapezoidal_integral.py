from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
import math

# 積分の範囲
a = 0
b = math.pi / 2

# 台形の数
N = 100

# 台形の幅
h = (b-a)/N

# 台形積分法の公式
# 関数 f(x) = sin(x) を直接記述し、a と b での関数の値を計算
I = 0.5*h*(sin(a) + sin(b) + 2*sum(sin(a + k*h) for k in range(1, N)))

print(I)

