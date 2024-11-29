import math
import sys

sys.setrecursionlimit(1_000_000)


class Solution:

    @staticmethod
    def get_input():
        with (open("input.txt", "r") as f):
            raw = f.readlines()
            n, m, k = list(map(int, raw[0].split()))
            connections = []
            for i in range(1, len(raw)):
                first, second = tuple(map(int, raw[i].split()))
                connections.append((first, second))
        return n, m, k, connections

    @staticmethod
    def solve(n, m, k, connections):
        peck_tree = PeckTree(n)

        for first, second in connections:
            ok = peck_tree.unite(first - 1, second - 1)
            if not ok:
                return 0
        for relations in peck_tree.relations:
            if len(relations) > 2:
                return 0
        lone = 0
        for p in range(n):
            if peck_tree.is_lone(p):
                lone += 1
        friendly = n - lone
        var = 1
        for i in range(n):
            var *= math.factorial(len(peck_tree.conns[i]) - len(peck_tree.relations[i]))
        var *= 2 ** (peck_tree.diff_groups + peck_tree.grouped)
        var *= math.factorial(peck_tree.diff_groups)
        options = friendly + 2
        while lone:
            var *= options
            options += 1
            lone -= 1
        return var % k

    def solve_from_input(self):
        result = self.solve(*self.get_input())
        print(result)


class WeightedQUPathCompression:

    def __init__(self, n):
        self.id_array = [i for i in range(n)]

    def union(self, p: int, q: int) -> None:
        p_root, p_height = self._root(p)
        q_root, q_height = self._root(q)
        if p_root == q_root:
            return
        if p_height < q_height:
            self.id_array[p_root] = q_root
        else:
            self.id_array[q_root] = p_root

    def connected(self, p: int, q: int) -> bool:
        return self._root(p)[0] == self._root(q)[0]

    def _root(self, p: int) -> tuple[int, int]:
        current_element = self.id_array[p]
        counter = 0

        while current_element != self.id_array[current_element]:
            self.id_array[current_element] = self.id_array[self.id_array[current_element]]
            current_element = self.id_array[current_element]
            counter += 1

        return current_element, counter


class PeckTree(WeightedQUPathCompression):

    def __init__(self, n):
        super().__init__(n)
        self.conns = [[] for _ in range(n)]
        self.relations = [[] for _ in range(n)]
        self.part_of_group = [False for _ in range(n)]
        self.diff_groups = 0
        self.grouped = 0

    def unite(self, p: int, q: int):
        if self.connected(p, q):
            return False
        p_lone = self.is_lone(p)
        q_lone = self.is_lone(q)

        if p_lone and q_lone:
            self.diff_groups += 1
        elif not p_lone and not q_lone:
            self.diff_groups -= 1

        p_group = self.is_in_group(p)
        q_group = self.is_in_group(q)
        if p_group and q_group:
            self.grouped -= 1

        new_group = self.connect(p, q, p_group, q_group)
        self.union(p, q)
        if new_group:
            self.mark_as_in_group(p)
            self.grouped += 1

        return True

    def connect(self, p, q, p_group, q_group):
        self.union(p, q)
        if p_group or q_group:
            self.mark_as_in_group(p)
        new_group = False
        for m in [p, q]:
            for relative in self.conns[m]:
                if len(self.conns[relative]) > 1 and relative not in self.relations[m]:
                    self.relations[m].append(relative)
                    self.relations[relative].append(m)
                    if not new_group and not self.is_in_group(relative):
                        new_group = True
        if len(self.conns[p]) > 0 and len(self.conns[q]) > 0:
            self.relations[p].append(q)
            self.relations[q].append(p)
            if not p_group and not q_group and not new_group:
                new_group = True

        self.conns[p].append(q)
        self.conns[q].append(p)

        return new_group

    def is_lone(self, p):
        return len(self.conns[p]) == 0

    def mark_as_in_group(self, p):
        root, _ = self._root(p)
        self.part_of_group[root] = True

    def is_in_group(self, p):
        in_group = self.part_of_group[p]
        if not in_group:
            root, _ = self._root(p)
            in_group = self.part_of_group[root]
            if in_group:
                self.part_of_group[p] = True
        return in_group


if __name__ == "__main__":
    solution = Solution()
    solution.solve_from_input()
