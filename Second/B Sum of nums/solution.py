class Solution:

    @staticmethod
    def get_input():
        with open("input.txt", "r") as f:
            raw = f.readlines()
            n, lucky = list(map(int, raw[0].split()))
            nums = list(map(int, raw[1].split()))
        return n, lucky, nums

    @staticmethod
    def solve(n: int, lucky, nums: list[int]) -> int:
        result = 0
        left = right = 0
        this_sum = 0
        while left < len(nums) or right < len(nums):
            if this_sum < lucky:
                if right == len(nums):
                    break
                elif right < len(nums):
                    this_sum += nums[right]
                    right += 1
            elif this_sum > lucky:
                if left < len(nums):
                    this_sum -= nums[left]
                    left += 1
            else:
                result += 1
                this_sum -= nums[left]
                if left < len(nums):
                    left += 1

        return result


    def solve_from_input(self):
        print(self.solve(*self.get_input()))


if __name__ == "__main__":
    solution = Solution()
    solution.solve_from_input()
