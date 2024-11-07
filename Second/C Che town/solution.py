class Solution:

    @staticmethod
    def get_input():
        with open("input.txt", "r") as f:
            raw = f.readlines()
            n, r = list(map(int, raw[0].split()))
            distances = list(map(int, raw[1].split()))
        return n, r, distances

    @staticmethod
    def solve(n: int, r, distances: list[int]) -> int:
        result = 0
        right = 1
        for i in range(len(distances)):
            while distances[right] - distances[i] <= r and right < len(distances) - 1:
                right += 1
            if distances[right] - distances[i] > r:
                result += len(distances) - right

        return result


    def solve_from_input(self):
        print(self.solve(*self.get_input()))


if __name__ == "__main__":
    solution = Solution()
    solution.solve_from_input()
