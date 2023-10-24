text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""
import re 

# 単語の抽出（記号を無視）
words = re.findall(r'\b\w+\b', text)

# 各単語の文字数をカウントし、それを文字列に変換して連結
pi_string = "".join(map(str, map(len, words)))

# 結果の出力
print(pi_string)
