def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    s1s1 = s1 + s1
    return s2 in s1s1


print(is_rotation('waterbottle', 'erbottlewat'))
print(is_rotation('waterbottle', 'erbottlewaa'))
