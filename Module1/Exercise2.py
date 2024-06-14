# Cau hoi tu luan
def exercise1(num_list, k):
    length = len(num_list)
    i = 0
    j = i + k
    while j <= length:
        arr = num_list[i:j]
        print(f"Max: {max(arr)}")
        i += 1
        j += 1


def exercise2(word):
    dict = {}
    for c in word:
        if c not in dict:
            numb = word.count(c)
            dict[c] = numb
            word.replace(c, '')
    sorted_dict = {k: v for k, v in sorted(
        dict.items(), key=lambda item: item[1])}
    print("{ ", end='')
    formatted_items = ', '.join(
        [f"'{k}': {v}" for k, v in sorted_dict.items()])
    print(formatted_items, end='')
    print(" }")


def count_words(file_path):
    a_file = open(file_path, 'r')
    word = a_file.read()
    list_word = word.split()
    dict = {}
    for c in list_word:
        if c not in dict:
            numb = list_word.count(c)
            dict[c] = numb
            list_word.remove(c)
    sorted_dict = {k: v for k, v in sorted(
        dict.items(), key=lambda item: item[1])}
    print("{ ", end='')
    formatted_items = ',\n'.join(
        [f"'{k}': {v}" for k, v in sorted_dict.items()])
    print(formatted_items, end='')
    print(" }")


def exercise4(source, target):
    m = len(source)
    n = len(target)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        dp[i][0] = i

    for j in range(1, n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if source[i - 1] == target[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    return dp[m][n]


if __name__ == "__main__":
    count_words('P1_data.txt')
