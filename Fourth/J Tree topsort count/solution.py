import math
import sys
from collections import deque


class Solution:
    @staticmethod
    def get_input():
        with open("input.txt", "r") as f:
            raw = f.readlines()
            n = int(raw[0])
            connections = []
            for i in range(1, len(raw)):
                split_ = raw[i].split()
                first = int(split_[0])
                second = int(split_[1])
                connections.append((first, second))
        return n, connections

    def solve(self, n, connections):
        connections = sorted(connections, key=lambda x: x[0])
        adj = [([], []) for _ in range(n)]
        for first, second in connections:
            adj[first - 1][1].append(second - 1)  # По индексу 1 исходящие
            adj[second - 1][0].append(first - 1)  # По индексу 0 входящие
        root_nodes = [i for i, node in enumerate(adj) if not node[0]]  # Делаем список из вершин
        dp = [1 for _ in range(n)]
        sz = [1 for _ in range(n)]
        nszf = [1 for _ in range(n)]
        result = 0

        pre = deque(root_nodes)
        traversed = [False for _ in range(n)]
        counted = [False for _ in range(n)]
        calculated = 0
        while calculated < n:
            V = pre.pop()
            if not traversed[V]:
                pre.append(V)
                traversed[V] = True
                for v in adj[V][1]:
                    if not traversed[v]:
                        pre.append(v)
            else:
                ndp = 1
                nsz = 1
                for v in adj[V][1]:
                    if not counted[v]:
                        continue
                    sz[V] += sz[v]
                    ndp *= dp[v]
                    nsz *= math.factorial(sz[v])
                dp[V] = math.factorial(sz[V] - 1) * ndp // nsz
                if len(adj[V][0]) == 0:
                    print("here")
                    result += dp[V]
                calculated += 1
                counted[V] = True
                pre.appendleft(V)
        print(dp)
        print(sz)
        return result

    def solve_from_input(self):
        print(self.solve(*self.get_input()))


if __name__ == "__main__":
    solution = Solution()
    solution.solve_from_input()
