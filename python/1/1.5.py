def one_edit_away(first,second):
    if len(first) == len(second):
        return one_edit_away_replace(first,second)
    elif len(first) + 1 == len(second):
        return one_edit_away_insert(first,second)
    elif len(first) - 1 == len(second):
        return one_edit_away_insert(second,first)
    return False

def one_edit_away_replace(first,second):
    found_difference = False
    for i in range(len(first)):
        if first[i] != second[i]:
            if found_difference:
                return False
            found_difference = True
    return True

def one_edit_away_insert(shorter, longer):
    i_shorter = 0
    i_longer = 0
    while i_longer < len(longer) and i_shorter < len(shorter):
        if shorter[i_shorter] != longer[i_longer]:
            if i_shorter != i_longer:
                return False
            i_longer += 1
        else:
            i_shorter += 1
            i_longer += 1
    return True

def one_edit_away2(first,second):
    if abs(len(first) - len(second)) > 1:
        return False
    shorter, longer = (first,second) if len(first) < len(second) else (second,first)
    i_shorter = 0
    i_longer = 0
    found_difference = False
    while i_longer < len(longer) and i_shorter < len(shorter):
        if shorter[i_shorter] != longer[i_longer]:
            if found_difference:
                return False
            found_difference = True
            if len(shorter) == len(longer):
                i_shorter += 1
        else:
            i_shorter += 1
        i_longer += 1
    return True

print(one_edit_away('hole','hoe'))
print(one_edit_away('hole','hold'))
print(one_edit_away('hole','holed'))
print(one_edit_away('hole','boe'))
print(one_edit_away2('hole','hoe'))
print(one_edit_away2('hole','hold'))
print(one_edit_away2('hole','holed'))
print(one_edit_away2('hole','boe'))