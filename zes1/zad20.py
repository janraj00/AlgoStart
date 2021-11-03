
eps = 1e-10


def arm_geo(num1, num2):
    a = (num1*num2) ** (1/2)
    b = (num1+num2) / 2
    while abs(a-b) > eps:
        a, b = (a*b) ** (1/2), (a+b)/2
    return a


print(arm_geo(3, 5))
