num1, num2 = 61, 10
import math

# TODO
#num1 は素数であると仮定する
is_prime_num1 = True

#1以下の数は素数ではない
#2からnum1の平方根までの各数iに対して、num1をiで割った余りが0であるか
#余りが0である場合、num1はiで割り切れるので素数ではない
if num1 <= 1:
    is_prime_num1 = False
else:
    for i in range(2, math.isqrt(num1) + 1):
        if num1 % i == 0:
            is_prime_num1 = False
            break

#num2も同様
is_prime_num2 = True
if num2 <= 1:
    is_prime_num2 = False
else:
    for i in range(2, math.isqrt(num2) + 1):
        if num2 % i == 0:
            is_prime_num2 = False
            break

print(is_prime_num1, is_prime_num2)