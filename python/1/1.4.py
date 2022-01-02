def build_char_frequency_table(phrase):
    table = [0] * (ord('z') - ord('a') + 1)
    for c in phrase:
        x = get_char_number(c)
        if x != -1:
            table[x] += 1
    return table


def get_char_number(c):
    a = ord('a')
    z = ord('z')
    val = ord(c.lower())
    return val - a if a <= val <= z else -1


def check_max_one_odd(table):
    found_odd = False
    for i in table:
        if i % 2 == 1:
            if found_odd:
                return False
            found_odd = True
    return True


def is_permutation_of_palindrome(phrase):
    table = build_char_frequency_table(phrase)
    return check_max_one_odd(table)


def is_permutation_of_palindrome2(phrase):
    count_odd = 0
    table = [0] * (ord('z') - ord('a') + 1)
    for c in phrase:
        x = get_char_number(c)
        if x != -1:
            table[x] += 1
            if table[x] % 2 == 1:
                count_odd += 1
            else:
                count_odd -= 1
    return count_odd <= 1


def check_exactly_one_bit_set(bit_vector):
    return bit_vector & (bit_vector - 1) == 0


def toggle(bit_vector, index):
    if index < 0:
        return bit_vector
    mask = 1 << index
    return bit_vector ^ mask


def create_bit_vector(phrase):
    bit_vector = 0
    for c in phrase:
        x = get_char_number(c)
        bit_vector = toggle(bit_vector, x)
    return bit_vector


def is_permutation_of_palindrome3(phrase):
    bit_vector = create_bit_vector(phrase)
    return bit_vector == 0 or check_exactly_one_bit_set(bit_vector)


print(is_permutation_of_palindrome('Tact Coa '))
print(is_permutation_of_palindrome('aa'))
print(is_permutation_of_palindrome('Tact Coa b'))
print(is_permutation_of_palindrome2('Tact Coa '))
print(is_permutation_of_palindrome2('aa'))
print(is_permutation_of_palindrome2('Tact Coa b'))
print(is_permutation_of_palindrome3('Tact Coa '))
print(is_permutation_of_palindrome3('aa'))
print(is_permutation_of_palindrome3('Tact Coa b'))
