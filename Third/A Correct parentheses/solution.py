from collections import deque


class Solution:

    @staticmethod
    def get_input():
        with open("input.txt", "r") as f:
            raw = f.readlines()
            parentheses = raw[0].strip()
        return parentheses

    @staticmethod
    def solve(parentheses) -> str:
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        dq = deque()
        for sym in parentheses:
            if not dq or sym not in pairs:
                dq.append(sym)
            elif sym in pairs and (not dq or dq.pop() != pairs[sym]):
                return "no"
        if dq:
            return "no"
        return "yes"

    def solve_from_input(self):
        print(self.solve(self.get_input()))


if __name__ == "__main__":
    solution = Solution()
    solution.solve_from_input()
