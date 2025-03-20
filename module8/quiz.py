def func(n, m):
    y1 = 10*(n**2) + 20*n + 30
    y2 = m(n)
    print(y1, y2)
    print(y1 <= y2)

def m1(n):
    return 60 *(n**2)

def m2(n):
    return 30 *(n**2)

def m3(n):
    return 11 *(n**2)

def m4(n):
    return 10.1 *(n**2)

def m5(n):
    return 10 *(n**2)

func(1, m1)
func(1, m2)
func(100, m3)
func(1000, m4)
func(1000, m5)