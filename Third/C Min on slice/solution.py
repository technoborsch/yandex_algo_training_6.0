from collections import deque


class Solution:

    @staticmethod
    def get_input():
        with open("input.txt", "r") as f:
            raw = f.readlines()
            n, k = list(map(int, raw[0].split()))
            nums = list(map(int, raw[1].split()))
        return n, k, nums

    @staticmethod
    def solve(n: int, k, nums: list[int]) -> list[int]:
        result = []
        dq = deque()
        for i in range(len(nums)):
            while dq and dq[-1] > nums[i]:
                dq.pop()
            dq.append(nums[i])
            if i >= k - 1:
                result.append(dq[0])
                if nums[i - k + 1] == dq[0]:
                    dq.popleft()

        return result

    def solve_from_input(self):
        result = self.solve(*self.get_input())
        for num in result:
            print(num)


if __name__ == "__main__":
    solution = Solution()
    solution.solve_from_input()
