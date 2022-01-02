def replaceSpaces(str):
    true_length = len(str)
    space_count = 0
    for i in str:
        if i == ' ':
            space_count += 1
    index = space_count * 2 + true_length
    res = [None]*index
    for i in range(true_length - 1, -1, -1):
        if str[i] == ' ':
            res[index - 1] = '0'
            res[index - 2] = '2'
            res[index - 3] = '%'
            index -= 3
        else:
            res[index - 1] = str[i]
            index -= 1
    return ''.join(res)

s = 'test test'
print(replaceSpaces(s))
