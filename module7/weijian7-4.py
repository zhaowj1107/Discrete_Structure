def rice_cooker_1(white: int, brown: int, in_cups: list):
    print(f"white rice: {white} cups")
    print(f"brown rice: {brown} cups")
    print(f"total rice: {white + brown} cups")
    out_cups = [white * 1/3, brown * 1/3]
    white_after = white * 2/3 + in_cups[0]
    brown_after = brown * 2/3 + in_cups[1]
    print(f"after white rice: {white_after} cups")
    print(f"after brown rice: {brown_after} cups")
    print(f"after total rice: {white_after + brown_after} cups")
    return white_after, brown_after, out_cups

def rice_cooker_2(white: int, brown: int, in_cups: list):
    print(f"white rice: {white} cups")
    print(f"brown rice: {brown} cups")
    print(f"total rice: {white + brown} cups")
    out_cups = [white * 1/3, brown * 1/3]
    white_after = white * 2/3 + in_cups[0]
    brown_after = brown * 2/3 + in_cups[1]
    print(f"after white rice: {white_after} cups")
    print(f"after brown rice: {brown_after} cups")
    print(f"after total rice: {white_after + brown_after} cups")
    return white_after, brown_after, out_cups

if __name__ == "__main__":
    white_r1 = 3
    brown_r1 = 0
    white_r2 = 0
    brown_r2 = 3
    in_cups_r1 = [1/4, 3/4]
    w_r1, b_r1, out_cups_r1 = rice_cooker_1(white_r1, brown_r1, in_cups_r1)
    w_r2, b_r2, out_cups_r2 = rice_cooker_1(white_r2, brown_r2, out_cups_r1)
    # rice_cooker_2(white: int, brown: int, in_cups: list)
    # white_r1 = 3
    # brown_r1 = 0
    # white_r2 = 0
    # brown_r2 = 3
    # for i in range(10):
    # white_after, brown_after, out_cups = rice_cooker_1(white, brown, in_cups)
    # print(f"white rice after: {white_after} cups")
    # print(f"brown rice after: {brown_after} cups")
    # print(f"out rice: {out_cups} cups")
    # white_after, brown_after, out_cups = rice_cooker_2(white, brown, in_cups)
    # print(f"white rice after: {white_after} cups")
    # print(f"brown rice after: {brown_after} cups")
    # print(f"out rice: {out_cups} cups")