#TODO
# 与えられた数字のペア
pairs = [(10, 20), (14, 91), (91, 14)]

# 各ペアに対してGCDを計算するための結果リストを初期化
gcd_results = []

# ペアリスト内の各ペアに対してループを実行
for a, b in pairs:
    # bが0でない間、ループを実行（ユークリッドの互除法）
    while b != 0:
        a, b = b, a % b
    # ループが終了したら、gcd_resultsリストに結果（GCD）を追加
    gcd_results.append(a)

print(gcd_results)

