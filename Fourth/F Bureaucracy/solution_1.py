import sys

sys.setrecursionlimit(300000)


class Solution:

    @staticmethod
    def get_input():
        with open("input.txt", "r") as f:
            raw = f.readlines()
            n = int(raw[0])
            bosses = list(map(int, raw[1].split()))
        return n, bosses

    @staticmethod
    def solve(n, bosses):
        employees = tuple(TNode() for _ in range(n))
        for i, boss in enumerate(bosses):
            employees[boss - 1].add_child(employees[i + 1])
        employees[0].calc_level_sum()
        employees[0].calc_money()
        return [employee.money for employee in employees]


    def solve_from_input(self):
        print(*self.solve(*self.get_input()))


class TNode:
    __slots__ = "ch", "level_sum", "money"

    def __init__(self):
        self.ch = None
        self.money = 1
        self.level_sum = 1

    def add_child(self, node):
        if not self.ch:
            self.ch = []
        self.ch.append(node)

    def calc_level_sum(self):
        if self.ch:
            for ch in self.ch:
                self.level_sum += ch.calc_level_sum()
        return self.level_sum

    def calc_money(self):
        if self.ch:
            for ch in self.ch:
                self.money += ch.calc_money() + ch.level_sum
        return self.money


if __name__ == "__main__":
    solution = Solution()
    solution.solve_from_input()
