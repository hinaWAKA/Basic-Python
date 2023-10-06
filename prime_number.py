# TODO
import math
# 自然数nが素数であるかを判定するには、2からn^1/2までの範囲でnを割り切れる（割り算の余りが0である）数が存在しないことを確認。
# この範囲を選ぶ理由は、もしnが素数でない自然数であるならば、その約数は少なくとも1つはn^1/2以下であるため。

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

# Check the given numbers
num1, num2 = 61, 10
is_prime_num1, is_prime_num2 = is_prime(num1), is_prime(num2)

print(is_prime_num1, is_prime_num2)