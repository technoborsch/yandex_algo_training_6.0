class Solution:

    @staticmethod
    def get_input():
        with open("input.txt", "r") as f:
            raw = f.readlines()
            n = int(raw[0])
            nums = list(map(int, raw[1].split()))
        return n, nums

    @staticmethod
    def solve(n: int, nums: list[int]) -> list[int]:
        result = [0]
        for i, num in enumerate(nums):
            result.append(result[i] + num)
        return result[1:]

    def solve_from_input(self):
        print(*self.solve(*self.get_input()))


if __name__ == "__main__":
    solution = Solution()
    solution.solve_from_input()
