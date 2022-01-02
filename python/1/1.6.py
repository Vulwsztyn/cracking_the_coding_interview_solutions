def compress(phrase):
    consecutive_count = 0
    current = phrase[0]
    res_array=[]
    for c in phrase:
        if c == current:
            consecutive_count += 1
        else:
            res_array.append(current+str(consecutive_count))
            consecutive_count = 1
            current = c
    res_array.append(current + str(consecutive_count))
    res = ''.join(res_array)
    return res if len(res) < len(phrase) else phrase

print(compress('aabcccccaaa'))
print(compress('abbcc'))