class Solution:

    @staticmethod
    def get_input():
        with open("input.txt", "r") as f:
            raw = f.readlines()
            n, k = list(map(int, raw[0].split()))
            tasks = list(map(int, raw[1].split()))
        return n, k, tasks

    @staticmethod
    def solve(n: int, k, tasks: list[int]) -> int:
        right = 0
        max_different = 1
        tasks = sorted(tasks)
        for i, task in enumerate(tasks):
            while right < len(tasks) and tasks[right] - task <= k:
                right += 1
            max_different = max(max_different, right - i)
        return max_different

    def solve_from_input(self):
        print(self.solve(*self.get_input()))


if __name__ == "__main__":
    solution = Solution()
    solution.solve_from_input()
