from collections import deque

def get_input():
    with open("input.txt", "r") as f:
        raw = f.readlines()
        n = int(raw[0])
        connections = []
        for i in range(1, len(raw) - 1):
            split_ = raw[i].split()
            if split_:
                first = int(split_[0])
                second = int(split_[1])
                connections.append((first, second))
        costs = list(map(int, raw[-1].split()))
    return n, connections, costs

def solve(n, connections, costs):

    if not connections:
        return costs[0], 1, [1]
    else:
        adj = [[] for _ in range(n)]
        for first, second in connections:
            adj[first - 1].append(second - 1)
            adj[second - 1].append(first - 1)
        dp1 = [0 for _ in range(n)]
        dp2 = [0 for _ in range(n)]

        sum1 = 0
        sum2 = 0

        pre = deque()
        traversed = [False for _ in range(n)]
        counted = [False for _ in range(n)]
        calculated = 0
        pre.append(0)
        while calculated < n:
            V = pre.pop()
            if not traversed[V]:
                pre.append(V)
                traversed[V] = True
                for v in adj[V]:
                    if not traversed[v]:
                        pre.append(v)
            else:
                sum1 = 0
                sum2 = 0
                for v in adj[V]:
                    if not counted[v]:
                        continue
                    sum1 += min(dp1[v], dp2[v])
                    sum2 += dp1[v]
                dp1[V] = costs[V] + sum1
                dp2[V] = sum2
                calculated += 1
                counted[V] = True
                pre.appendleft(V)
        switched_on = set()

        if dp1[0] < dp2[0]:
            traversed[0] = False
            switched_on.add(1)
        while pre:
            V = pre.popleft()
            this_tagged = not traversed[V]
            if not this_tagged:
                for v in adj[V]:
                    traversed[v] = False
                    switched_on.add(v + 1)
            else:
                for v in adj[V]:
                    if dp1[v] < dp2[v]:
                        traversed[v] = False
                        switched_on.add(v + 1)
                    else:
                        traversed[v] = True

        return min(dp1[0], dp2[0]), len(switched_on), switched_on

if __name__ == "__main__":
    result = solve(*get_input())
    print(result[0], result[1])
    print(*result[2])
