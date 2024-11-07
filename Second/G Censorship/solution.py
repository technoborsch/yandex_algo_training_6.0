class Solution:

    @staticmethod
    def get_input():
        with open("input.txt", "r") as f:
            raw = f.readlines()
            n, crudeness = list(map(int, raw[0].split()))
            string = raw[1]
        return n, crudeness, string

    @staticmethod
    def solve(n: int, crudeness: int, string: str) -> int:
        result = 0
        a_pref = [0]
        b_pref = [0]
        for i, sym in enumerate(string):
            if sym == "a":
                a_pref.append(a_pref[i] + 1)
                b_pref.append(b_pref[i])
            elif sym == "b":
                b_pref.append(b_pref[i] + 1)
                a_pref.append(a_pref[i])
            else:
                b_pref.append(b_pref[i])
                a_pref.append(a_pref[i])

        this_crudeness = 0
        left = right = 0
        while left < len(string) - 1 and right < len(string) - 1:
            if this_crudeness <= crudeness:
                result = max(result, right - left + 1)
                if right < len(string) - 1:
                    right += 1
                if string[right] == "b":
                    this_crudeness += a_pref[right + 1] - a_pref[left]
            else:
                if string[left] == "a":
                    this_crudeness -= b_pref[right + 1] - b_pref[left]
                if left < len(string) - 1:
                    left += 1
        return result

    def solve_from_input(self):
        print(self.solve(*self.get_input()))


if __name__ == "__main__":
    solution = Solution()
    solution.solve_from_input()
