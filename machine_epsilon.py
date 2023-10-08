# TODO

epsilon = 1.0

while 1.0 + epsilon > 1.0:
    epsilon /= 2.0

# epsilon は 1 と 1 + 2*epsilon の最小epsilon 
# 求めるマシンイプシロンは 2*epsilon
machine_epsilon = 2.0 * epsilon

print(machine_epsilon)

