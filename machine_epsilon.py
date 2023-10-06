# TODO
#sys.float_info.epsilon という、浮動小数点数のマシンイプシロンを取得するための機能が sys モジュールに用意。
import sys
machine_epsilon = sys.float_info.epsilon

print(machine_epsilon)
