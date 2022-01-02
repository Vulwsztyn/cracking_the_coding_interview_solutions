def permutations(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)


def permutations2(s, t):
    if len(s) != len(t):
        return False
    letters = [0] * 128
    for c in s:
        letters[ord(c)] += 1
    for c in t:
        letters[ord(c)] -= 1
    for l in letters:
        if l > 0:
            return False
    return True


print(permutations('abc', 'cba'))
print(permutations('abc', 'cbc'))
print(permutations2('abc', 'cba'))
print(permutations2('abc', 'cbc'))
