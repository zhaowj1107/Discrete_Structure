def func_t(t):
    """
    f(t + 2) = 5 * f(t +1) - 6 * f(t)
    """
    if t == 1:
        return 1
    elif t == 2:
        return 5
    else:
        return 5 * func_t(t - 1) - 6 * func_t(t - 2)

def func_a(t1, t2):
    return t2 - 2 * t1

def func_b(t1, t2):
    return t2 - 3* t1

if __name__ == "__main__":
    for i in range(1, 11):
        print(f"f({i}) = {func_t(i)}")
        t1 = func_t(i)
        t2 = func_t(i + 1)
        # print(f"a{i}: fa({i-1}, {i}) = {func_a(t1, t2)}")
        print(f"b{i}: fb({i-1}, {i}) = {func_b(t1, t2)}")

