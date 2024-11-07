class Solution:

    @staticmethod
    def get_input():
        with open("input.txt", "r") as f:
            raw = f.readlines()
            n = int(raw[0])
            interest_ranks = list(map(int, raw[1].split()))
            useful_ranks = list(map(int, raw[2].split()))
            mood = list(map(int, raw[3].split()))
        return n, interest_ranks, useful_ranks, mood

    @staticmethod
    def solve(n: int, interest_ranks: list[int], useful_ranks: list[int], mood: list[int]) -> list[int]:
        used_indexes = set()
        result = []
        zipped = list(zip(range(1, n + 1), interest_ranks, useful_ranks))
        interest_counter = 0
        useful_counter = 0
        ranged_by_interest = sorted(zipped, key=lambda x: (x[1], x[2], -x[0]), reverse=True)
        ranged_by_useful = sorted(zipped, key=lambda x: (x[2], x[1], -x[0]), reverse=True)

        for m in mood:
            if not m:
                while (ranged_by_interest[interest_counter][0] in used_indexes
                       and interest_counter < len(ranged_by_interest) - 1):
                    interest_counter += 1
                index = ranged_by_interest[interest_counter][0]
                result.append(index)
                used_indexes.add(index)
                interest_counter += 1
            else:
                while (ranged_by_useful[useful_counter][0] in used_indexes
                    and useful_counter < len(ranged_by_useful) - 1):
                    useful_counter += 1
                index = ranged_by_useful[useful_counter][0]
                result.append(index)
                used_indexes.add(index)
                useful_counter += 1
        return result

    def solve_from_input(self):
        print(*self.solve(*self.get_input()))


if __name__ == "__main__":
    solution = Solution()
    solution.solve_from_input()
