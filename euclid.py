import math
# 問3. ユークリッドの互除法
a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

def euc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

gcd = euc(a, b)
print(f"{a} と {b} の最大公約数は {gcd} です。")

# 問4. 互いに素
def are_coprime(a, b):
    gcd = euc(a, b)
    return gcd == 1

if are_coprime(a, b):
    print(f"{a} と {b} は互いに素です。")
else:
    print(f"{a} と {b} は互いに素ではありません。")


#エクストラ問題
import random
def coprime_prob(num_samples):
    count_coprime = 0

    for _ in range(num_samples):
        a = random.randint(1, 10000)  # 1から10000までのランダムな整数
        b = random.randint(1, 10000)  # 1から10000までのランダムな整数

        if are_coprime(a, b):
            count_coprime += 1

    prob = count_coprime / num_samples
    return prob

num_samples = 100000  # サンプル数を設定
print(f"エクストラ問題の答え： {coprime_prob(num_samples)}")

