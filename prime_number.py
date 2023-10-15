import math

def is_prime(n):
    if n <= 1:
        return False
    m = 2
    while m * m <= n:
        if n % m == 0:
            return False
        m += 1
    return True

#エクストラ問題（3.14や-1などの整数以外の値や負の値が入力された場合エラーをはかせる）
try:
    n = int(input('n: '))
    if n <= 0:
        raise ValueError('自然数を入力してください')
    
    print(is_prime(n))
except ValueError as e:
    print(e)
