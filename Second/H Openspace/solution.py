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
        result = None
        lr_sum = [0]
        for i, num in enumerate(nums):
            lr_sum.append(lr_sum[i] + num)

        for i in range(1, len(nums) + 1):
            lr_sum[i] = lr_sum[i] + lr_sum[i - 1]

        rl_sum = [0]
        for i in range(len(nums) -1, -1, -1):
            num = nums[i]
            rl_sum.append(rl_sum[len(nums) - 1 - i] + num)

        for i in range(1, len(nums) + 1):
            rl_sum[i] = rl_sum[i] + rl_sum[i - 1]

        for i in range(len(nums)):
            moves_left = lr_sum[i] - lr_sum[0]
            moves_right = rl_sum[len(nums) - 1 - i] - rl_sum[0]
            moves = moves_left + moves_right
            if result is None:
                result = moves
            elif moves < result:
                result = moves
        return result

    def solve_from_input(self):
        print(self.solve(*self.get_input()))


if __name__ == "__main__":
    solution = Solution()
    solution.solve_from_input()
