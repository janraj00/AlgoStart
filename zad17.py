
eps = 1e-10


def find_phi(a, b):
    div = -1
    while abs(div - b / a) > eps:
        div = b / a
        a, b = b, a + b
    return div


print(find_phi(5, 4))
