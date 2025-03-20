def hanoi(n, start, end, wingman, count=0):
    if n == 1:
        count += 1
        print("Move disk 1 from", start, "to", end, count)
    else:
        count = hanoi(n-1, start, wingman, end, count)
        print("Move disk", n, "from", start, "to", end, count)
        count += 1
        count = hanoi(n-1, wingman, end, start, count)

    return count

if __name__ == "__main__":
    print(hanoi(4, "A", "C", "B"))