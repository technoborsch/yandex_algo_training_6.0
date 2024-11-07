from collections import deque


class Solution:

    @staticmethod
    def get_input():
        with open("input.txt", "r") as f:
            raw = f.readlines()
            syms = raw[0].split()
        return syms

    @staticmethod
    def solve(syms: list[str]) -> int:
        st = deque()
        signs = "+-*"
        for sym in syms:
            if len(sym) == 1 and sym in signs:
                second = st.pop()
                first = st.pop()
                if sym == "+":
                    st.append(first + second)
                elif sym == "-":
                    st.append(first - second)
                elif sym == "*":
                    st.append(first * second)
            else:
                st.append(int(sym))
        return st[0]

    def solve_from_input(self):
        print(self.solve(self.get_input()))


if __name__ == "__main__":
    solution = Solution()
    solution.solve_from_input()
