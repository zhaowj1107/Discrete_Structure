#Question 1
def Hanoi(n, Start, Process, End):
    if n==1: print("Move disk", n, "from", Start, "to", End)
    else:
        Hanoi(n-1, Start, End, Process)
        print("Move disk", n, "from", Start, "to", End)
        Hanoi(n-1, Process, Start, End)


def Factorial(n):
	if n==1: return 1
	else: return Factorial(n-1)*n
   
print(Factorial(5))

#Question 2
def Factorial_parity(n):
    if n == 0:
        return 1
    elif n ==1:
        return 1
    else:
        return Factorial_parity(n-2)*n

#Question 3
def lyric(n):
    if n == 0:
        print("No more bottles of beer on the wall, no more bottles of beer. \nGo to the store and buy some more, 99 bottles of beer on the wall.\n")
    elif n == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, No More bottles of beer on the wall.\n")
        return lyric(n-1)
    else:
        total = n
        left = n - 1
        print(total,"bottles of beer on the wall,",total,"bottles of beer.\nTake one down and pass it around,",left,"bottles of beer on the wall.\n")
        return lyric(n-1)

lyric(99)
