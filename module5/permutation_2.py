def generate_permutations(elements):
    # 递归生成全排列
    if len(elements) == 1:
        return [elements]

    permutations = []
    for i in range(len(elements)):
        # 固定当前元素，然后递归排列剩下的元素
        rest = elements[:i] + elements[i+1:]
        for p in generate_permutations(rest):
            permutations.append([elements[i]] + p)

    return permutations

# 将每个排列转换为字符串形式
letters = ['a', 'b', 'c', 'd', 'e']
all_permutations = generate_permutations(letters)

# 打印 120 个单词
words = [''.join(p) for p in all_permutations]
for word in words:
    print(word)

print(f"Total words: {len(words)}")
