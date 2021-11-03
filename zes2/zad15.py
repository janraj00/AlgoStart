def n_num():
    res = []
    for j in range(10000000):
        if j == sum(int(i)**len(str(j)) for i in str(j)):
            res.append(j)
    return res

print(n_num())
