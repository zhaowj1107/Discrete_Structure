# 定义字母列表
letters = ["I", "A", "G", "L", "N"]

# 从一个空排列开始
permutations = [[]]

# 对于列表中的每个字母，依次将它插入到已有排列的所有可能位置
for letter in letters:
    new_permutations = []
    for perm in permutations:
        # 对当前排列中每个可能的位置插入 letter
        for pos in range(len(perm) + 1):
            new_perm = perm[:pos] + [letter] + perm[pos:]
            new_permutations.append(new_perm)
    permutations = new_permutations

# 将每个排列（列表）转换为字符串
words = ["".join(p) for p in permutations]

# 输出结果
print(words)
print("总数:", len(words))