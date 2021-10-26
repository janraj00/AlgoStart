from zad15 import find_pi
import numpy as np
import matplotlib.pyplot as plt


def cosinus(x):
    res = 1
    sign = -1
    pow_ = 2
    fac = 2
    for _ in range(20):
        res += sign*(x**pow_)/fac
        pow_ += 2
        fac *= pow_*(pow_-1)
        sign *= -1
    return res


xs = np.linspace(-5.3*find_pi(), 5.3*find_pi(), num=4000)
ys = [cosinus(x) for x in xs]
ys_true = np.cos(xs)

plt.plot(xs, ys)
plt.plot(xs, ys_true, "--")
plt.show()

#print(cosinus(find_pi()/2))

