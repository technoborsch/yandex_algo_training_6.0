class Solution:

    @staticmethod
    def get_input():
        with open("input.txt", "r") as f:
            raw = f.readlines()
            n = int(raw[0])
            nums = list(map(int, raw[1].split()))
        return n, nums

    @staticmethod
    def solve(n: int, nums: list[int]) -> int:
        result = 0
        p_sums = [0]
        for i, num in enumerate(nums):
            p_sums.append(p_sums[i] + num)

        mult = [0]
        for i, num in enumerate(nums):
            mult.append(num * (p_sums[len(nums)] - p_sums[i + 1]))

        sum_mult = [0]
        for i, num in enumerate(mult):
            sum_mult.append(sum_mult[i] + num)

        for i in range(len(nums) - 1):
            num = nums[i]
            result += num * (sum_mult[len(nums)] - sum_mult[i + 2])
            result = result % 1_000_000_007
        return result

    def solve_from_input(self):
        print(self.solve(*self.get_input()))


if __name__ == "__main__":
    solution = Solution()
    solution.solve_from_input()
