from collections import deque


class Solution:

    @staticmethod
    def get_input():
        with open("input.txt", "r") as f:
            raw = f.readlines()
            n, b = list(map(int, raw[0].split()))
            clients = list(map(int, raw[1].split()))
        return n, b, clients

    @staticmethod
    def solve(n: int, b: int, clients: list[str]) -> int:
        result = 0
        current_customers = 0
        q = deque()
        for i in range(n):

            q.appendleft(clients[i])
            current_customers += clients[i]
            result += current_customers

            this_perf = b
            while this_perf:
                if q and this_perf > q[-1]:
                    this_perf -= q.pop()
                elif q and this_perf <= q[-1]:
                    q[-1] -= this_perf
                    this_perf = 0
                else:
                    this_perf = 0

            current_customers -= this_perf

        return result

    def solve_from_input(self):
        print(self.solve(*self.get_input()))


if __name__ == "__main__":
    solution = Solution()
    solution.solve_from_input()
