
# TODO
#bが0になるまでaをbで割り続け、その都度aとbの値を更新。bが0になった時点でのaの値が、元のaとbの最大公約数。
def compute_gcd(a, b):
   
    while b != 0:
        a, b = b, a % b
    return a

# Given pairs of numbers
pairs = [(10, 20), (14, 91), (91, 14)]

gcd_results_without_gcd_func = [compute_gcd(a, b) for a, b in pairs]

print(gcd_results_without_gcd_func)
