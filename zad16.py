
def find_start():
    max_steps = 0
    max_num = -1
    for i in range(2, 10000 +1):
        start = i
        counter = 0
        while start != 1:
            start = (start % 2) * (3 * start + 1) +(1 - start % 2) * start / 2
            counter += 1
        if counter > max_steps:
            max_steps = counter
            max_num = i
    return max_num


print(find_start())
