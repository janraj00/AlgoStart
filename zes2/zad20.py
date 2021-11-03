digits = '0123456789ABCDEF'
# 0
# 1101


def code(liczba, system):
    if liczba == 0:
        return []
    result = code(liczba // system, system)
    result.append(digits[liczba % system])
    return result


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    for system in range(2, 16+1):
        tab = [0 for _ in range(system)]
        for c in code(a, system):
            # idx = ord(c) - ord    ('A') * int(ord(c) > ord('9')) - ord('0') * int(ord(c) <= ord('9'))
            tab[digits.index(c)] += 1
            # tab[idx] += 1

        is_bad = False
        for c in code(b, system):
            if tab[digits.index(c)] != 0:
                is_bad = True
                break

        if not is_bad:
            print(system)
            break



