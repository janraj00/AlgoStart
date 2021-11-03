def prime_test(n):
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 1
    while 6 * i - 1 <= n ** 0.5:
        if n % (6 * i - 1) == 0:
            return False
        if n % (6 * i + 1) == 0:
            return False

        i += 1

    return True
