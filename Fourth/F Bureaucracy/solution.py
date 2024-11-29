import os
import sys

import psutil

sys.setrecursionlimit(100000)


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
        root = TNode(1)
        for i, boss in enumerate(bosses):
            root.insert_child(boss, i + 2)
        result = [None for _ in range(n)]
        #root.calc_level_sum()
        #root.calc_money(result)
        process = psutil.Process(os.getpid())
        mem = process.memory_info()[0] / float(2 ** 20)
        print(f"Execution took {mem} MB")
        return result


    def solve_from_input(self):
        print(*self.solve(*self.get_input()))


class TNode:
    __slots__ = "ch", "money", "level_sum", "val", "level"

    def __init__(self, val, level = 0):
        self.val = val
        self.ch = []
        self.money = 1
        self.level_sum = 1
        self.level = level

    def insert_child(self, parent_val, val):
        if self.val != parent_val:
            for ch in self.ch:
                ch.insert_child(parent_val, val)
        else:
            self.ch.append(TNode(val))

    def calc_level_sum(self):
        for ch in self.ch:
            self.level_sum += ch.calc_level_sum()
        return self.level_sum

    def calc_money(self, result):
        if self.ch:
            for ch in self.ch:
                self.money += ch.calc_money(result) + ch.level_sum
        result[self.val - 1] = self.money
        return self.money


if __name__ == "__main__":
    solution = Solution()
    solution.solve_from_input()
