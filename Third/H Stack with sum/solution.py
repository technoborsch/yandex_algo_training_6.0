from collections import deque


class Solution:

    @staticmethod
    def get_input():
        with open("input.txt", "r") as f:
            raw = f.readlines()
            n = int(raw[0])
            operations = raw[1:]
        return n, operations

    @staticmethod
    def solve(n: int, operations: list[str]) -> list[int]:
        result = []
        s = StackSum()
        for operation in operations:
            if operation.startswith("+"):
                s.add(int(operation[1:]))
            elif operation.startswith("-"):
                result.append(s.pop())
            elif operation.startswith("?"):
                result.append(s.n_sum(int(operation[1:])))
        return result

    def solve_from_input(self):
        for item in self.solve(*self.get_input()):
            print(item)


class StackSum:

    def __init__(self):
        self.s = deque()
        self.ps = [0]

    def add(self, num):
        self.s.append(num)
        self.ps.append(self.ps[-1] + num)

    def pop(self):
        self.ps.pop()
        return self.s.pop()

    def n_sum(self, n):
        return self.ps[-1] - self.ps[-n - 1]


if __name__ == "__main__":
    solution = Solution()
    solution.solve_from_input()
