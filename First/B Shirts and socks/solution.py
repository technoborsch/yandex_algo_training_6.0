with open("input.txt", "r") as f:
    a, b, c, d = list(map(int, f.readlines()))

to_blue_shirt = b + 1
to_red_shirt = a + 1
to_blue_sock = d + 1
to_red_sock = c + 1

guarantee_shirts = (max(a, b) + 2, (max(a, b) + 1, 1))
guarantee_socks = (max(c, d) + 2, (1, max(c, d) + 1))
take_blue = (to_blue_shirt + to_blue_sock, (to_blue_shirt, to_blue_sock))
take_red = (to_red_shirt + to_red_sock, (to_red_shirt, to_red_sock))

list_ = [guarantee_socks, guarantee_shirts, take_blue, take_red]

if a == 0 or c == 0:
    if a == 0:
        print(1, to_red_sock)
    elif c == 0:
        print(to_red_shirt, 1)
elif b == 0 or d == 0:
    if b == 0:
        print(1, to_blue_sock)
    elif d == 0:
        print(to_blue_shirt, 1)
else:
    min_ = None
    min_i = None
    for i, option in enumerate(list_):
        sum_ = option[0]
        if min_ is None or sum_ < min_:
            min_ = sum_
            min_i = i
    print(*list_[min_i][1])
