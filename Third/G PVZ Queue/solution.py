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
        for i in range(n):
            current_customers += clients[i]
            result += current_customers

            if b > current_customers:
                current_customers = 0
            else:
                current_customers -= b
        if current_customers:
            result += current_customers
        return result

    def solve_from_input(self):
        print(self.solve(*self.get_input()))


if __name__ == "__main__":
    solution = Solution()
    solution.solve_from_input()
