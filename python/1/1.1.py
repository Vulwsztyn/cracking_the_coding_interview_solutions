def is_unique_chars(str):
    if len(str) > 128:
        return False
    char_set = [False] * 128
    for char in str:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True
    return True


def is_unique_chars2(str):
    checker = 0
    for char in str:
        val = ord(char)
        if checker & (1 << val):
            return False
        checker |= (1 << val)
    return True


print(is_unique_chars('abcdefg'))
print(is_unique_chars('abcdefgb'))
print(is_unique_chars2('abcdefg'))
print(is_unique_chars2('abcdefgb'))
