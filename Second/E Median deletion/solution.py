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
        result = []
        nums = sorted(nums)
        left = len(nums) // 2 - 1
        right = len(nums) // 2
        length = len(nums)

        for i in range(len(nums)):
            if length % 2:
                if left > len(nums) - right - 1:
                    result.append(nums[left])
                    left -= 1
                else:
                    result.append(nums[right])
                    right += 1
            else:
                if right >= len(nums) or nums[left] < nums[right]:
                    result.append(nums[left])
                    left -= 1
                else:
                    result.append(nums[right])
                    right += 1
            length -= 1

        return result

    def solve_from_input(self):
        print(*self.solve(*self.get_input()))


if __name__ == "__main__":
    solution = Solution()
    solution.solve_from_input()
