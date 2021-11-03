
a_curr, b_curr = 0, 2
a_next = 1

while int(input()) == a_curr:
    print(b_curr)
    a_curr, a_next, b_curr = a_next, a_next - b_curr * a_curr, b_curr + 2 * a_next


