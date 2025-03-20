base = 100000
def r(n):
    if n == 1:
        return 100000
    else:
        return r(n-1) + 1000 * (n -1)
sum = 0
for i in range(15):
    print(f"f({i+1}) = {r(i+1)}")
    sum += r(i+1)
    print(f"sum({i+1}) = {sum:.2f}")
    