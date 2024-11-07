from collections import deque


class Solution:

    @staticmethod
    def get_input():
        with open("input.txt", "r") as f:
            raw = f.readlines()
            n = int(raw[0])
            prices = list(map(int, raw[1].split()))
        return n, prices

    @staticmethod
    def solve(n: int, prices: list[int]) -> list[int]:
        result = [-1] * n
        st = deque()
        for i, price in enumerate(prices):
            while st and price < st[-1][1]:
                result[st.pop()[0]] = i
            st.append((i, price))
        return result

    def solve_from_input(self):
        print(*self.solve(*self.get_input()))


if __name__ == "__main__":
    solution = Solution()
    solution.solve_from_input()
