class Solution:

    @staticmethod
    def get_input():
        with open("input.txt", "r") as f:
            raw = f.readlines()
            n = int(raw[0])
            weights = list(map(int, raw[1].split()))
            m, k = list(map(int, raw[2].split()))
            evidence_numbers = list(map(int, raw[3].split()))
        return n, weights, m, k, evidence_numbers

    @staticmethod
    def solve(n, weights, m, k, evidence_numbers) -> list[int]:
        result = []
        eq_prefixes = [0]
        for i in range(1, len(weights)):
            if weights[i] == weights[i - 1]:
                eq_prefixes.append(eq_prefixes[i - 1] + 1)
            else:
                eq_prefixes.append(eq_prefixes[i - 1])
        steps_map = []
        j = 0
        prev_w = weights[j]
        for i in range(len(eq_prefixes)):
            while j < len(eq_prefixes) and eq_prefixes[j] - eq_prefixes[i] <= k and prev_w <= weights[j]:
                steps_map.append(i + 1)
                prev_w = weights[j]
                j += 1
            if j == i + 1:
                prev_w = weights[min(j, len(weights) - 1)]
        for evidence in evidence_numbers:
            result.append(steps_map[evidence - 1])
        return result

    def solve_from_input(self):
        print(*self.solve(*self.get_input()))


if __name__ == "__main__":
    solution = Solution()
    solution.solve_from_input()
