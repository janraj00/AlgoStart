a = int(input())
b = int(input())

# 1/6 == 0.1(6)

# if a is divisible by b we don't need a dot after integer-division result
digits_before_dot = f'{a // b}' if a % b == 0 else f'{a // b}.'
a %= b

digits = []
modulo = []

while a > 0:
    a *= 10
    digits.append(a // b)

    if a not in modulo:
        modulo.append(a)
    else:
        break

    a %= b

if a == 0:
    digits_after_dot = "".join(map(str, digits))
else:
    repeating_from = modulo.index(a)
    digits_before_period = "".join(map(str, digits[:repeating_from]))
    period = "".join(map(str, digits[repeating_from:-1]))
    digits_after_dot = f'{digits_before_period}({period})'

print(f'{digits_before_dot}{digits_after_dot}')
