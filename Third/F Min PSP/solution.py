from collections import deque


class Solution:

    @staticmethod
    def get_input():
        with open("input.txt", "r") as f:
            raw = f.readlines()
            n = int(raw[0])
            w = raw[1].strip()
            s = raw[2].strip()
        return n, w, s

    @staticmethod
    def solve(n: int, w: str, s: str) -> str:
        closing_pairs = {
            ")": "(",
            "]": "["
        }
        opening_pairs = {
            "(": ")",
            "[": "]"
        }
        result = s
        st = deque()
        for sym in s:
            if not st or sym not in closing_pairs:
                st.append(sym)
            else:
                st.pop()
        while len(result) < n:
            if len(result) == n - len(st):
                result += opening_pairs[st.pop()]
            else:
                for sym in w:
                    if sym in opening_pairs:
                        st.append(sym)
                        result += sym
                        break
                    elif st and st[-1] == closing_pairs[sym]:
                        st.pop()
                        result += sym
                        break
        return result

    def solve_from_input(self):
        print(self.solve(*self.get_input()))


if __name__ == "__main__":
    solution = Solution()
    solution.solve_from_input()
