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

    @staticmethod
    def solve(n, connections):
        connections = sorted(connections, key=lambda x: x[0])
        adj = [[] for _ in range(n)]
        for first, second in connections:
            adj[first - 1].append(second - 1)
            adj[second - 1].append(first - 1)
        f = [0 for _ in range(n)]
        g = [0 for _ in range(n)]
        paths = [None for _ in range(n)]

        pre = deque()
        traversed = [False for _ in range(n)]
        counted = [False for _ in range(n)]
        calculated = 0
        diameter = 0
        pre.append(0)
        diam_path = []
        # вычисляем дерево и компоненты
        while calculated < n:
            V = pre.pop()
            if not traversed[V]:
                pre.append(V)
                traversed[V] = True
                for v in adj[V]:
                    if not traversed[v]:
                        pre.append(v)
            else:
                max_ = 0
                max_index = None
                second = 0
                second_index = None
                for v in adj[V]:
                    if not counted[v]:
                        continue
                    if f[v] + 1 > max_:
                        prev_max = max_
                        max_ = f[v] + 1
                        prev_max_index = max_index
                        max_index = v
                        if prev_max > second:
                            second = prev_max
                            second_index = prev_max_index
                    elif f[v] + 1 > second:
                        second = f[v] + 1
                        second_index = v
                if max_:
                    f[V] += max_
                if max_ and second:
                    g[V] = max_ + second
                counted[V] = True
                if max_index is not None:
                    if paths[max_index] is None:
                        paths[max_index] = [max_index]
                    paths[V] = paths[max_index]
                    paths[V].append(V)
                if f[V] > g[V] and f[V] > diameter: # Приходящая линия выиграла
                    diameter = f[V]
                    diam_path = paths[V]
                elif g[V] >= f[V] and g[V] > diameter: # Поддерево выиграло
                    diameter = g[V]
                    if paths[max_index] is None:
                        paths[max_index] = [max_index]
                    paths[V] = paths[max_index]
                    if paths[second_index] is None:
                        paths[second_index] = [second_index]
                    diam_path = paths[V] + paths[second_index][::-1]
                calculated += 1
        pre.append(diam_path[0])
        calculated = 0
        f = [0 for _ in range(n)]
        g = [0 for _ in range(n)]
        while calculated < n:
            V = pre.pop()
            if traversed[V]:
                pre.append(V)
                traversed[V] = False
                for v in adj[V]:
                    if traversed[v]:
                        pre.append(v)
            else:
                max_ = 0
                second = 0
                for v in adj[V]:
                    if counted[v]:
                        continue
                    if f[v] + 1 > max_:
                        prev_max = max_
                        max_ = f[v] + 1
                        if prev_max > second:
                            second = prev_max
                    elif f[v] + 1 > second:
                        second = f[v] + 1
                if max_:
                    f[V] += max_
                if max_ and second:
                    g[V] = max_ + second
                #print(f"V {V + 1} f[V] {f[V]} g[V] {g[V]} max {max_} second {second}")
                counted[V] = False
                calculated += 1
        result = 0
        diam_set = set(diam_path)
        i = 0
        max_on_up = 0
        for V in diam_path:
            #print(f"V {V + 1}, gv {g[V]}, d {diameter}, i {i}, fV - 1 {f[V] - 1}")
            max_g_on_sub = 0
            max_f_from_sub = 0
            second_f_from_sub = 0
            g_on_path = 0
            f_on_path = 0
            for v in adj[V]:
                if not counted[v]:
                    if v not in diam_set:
                        max_g_on_sub = max(max_g_on_sub, g[v])
                        if f[v] + 1 > max_f_from_sub:
                            prev_max = max_f_from_sub
                            max_f_from_sub = f[v] + 1
                            if prev_max > second_f_from_sub:
                                second_f_from_sub = prev_max
                        elif f[v] > second_f_from_sub:
                            second_f_from_sub = f[v] + 1
                    else:
                        g_on_path = g[v]
                        f_on_path = f[v]
            sub_plus_diam = max(max_g_on_sub, max_f_from_sub - 1) * diameter

            max_on_up = max(max_on_up, i + max_f_from_sub, max_g_on_sub, max_f_from_sub + second_f_from_sub)
            rest_plus_sub = max_on_up * max(g_on_path, f_on_path)
            result = max(result, sub_plus_diam, rest_plus_sub)
            #print(f"V {V + 1}, max on up {max_on_up}, sub and diam {sub_plus_diam}, rest plus sub {rest_plus_sub}")
            #print(f"{max_g_on_sub} {max_f_from_sub} {g_on_path} {f_on_path}")
            i += 1
            counted[V] = True

        return result

    def solve_from_input(self):
        print(self.solve(*self.get_input()))


if __name__ == "__main__":
    solution = Solution()
    solution.solve_from_input()
