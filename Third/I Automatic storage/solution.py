from collections import deque
with open("input.txt", "r") as f:
    raw = f.readlines()
    n = int(raw[0])
    a, b = list(map(int, raw[1].split()))
    rovers = sorted([(i, *tuple(map(int, row.split()))) for i, row in enumerate(raw[2:])], key=lambda x: (x[2], x[1]))
result = []
priorities = [1 if side == a - 1 or side == b - 1 else 0 for side in range(4)]
times = [[None] * 4 for _ in range(rovers[-1][2])]
for rover in rovers:
    times[rover[2] - 1][rover[1] - 1] = rover[0]
cross = [deque() for _ in range(4)]
this_time = 0
add_rover = lambda i, r: cross[i].appendleft(r)
can_go = lambda pr, s, cr: not ((pr[s] and pr[s - 1] and cr[s - 1])
                                or (not pr[s] and (cr[s - 1] or any([i[0] and i[1] for i in zip(pr, cr)]))))
move = lambda side: result.append((this_time + 1, cross[side].pop()))
while cross[0] or cross[1] or cross[2] or cross[3] or this_time < len(times):
    if this_time < len(times):
        [add_rover(i, rover) for i, rover in enumerate(times[this_time]) if rover is not None]
    cross_state = [1 if cross[i] else 0 for i in range(4)]
    go_list = [1 if can_go(priorities, side, cross_state) and cross_state[side] else 0 for side in range(4)]
    [move(side) for side, possible in enumerate(go_list) if possible and cross[side]]
    this_time += 1
[print(x[0]) for x in sorted(result, key=lambda x: x[1])]
