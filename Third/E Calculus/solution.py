from collections import deque


class Solution:

    @staticmethod
    def get_input():
        with open("input.txt", "r") as f:
            string = f.readlines()[0].strip()
        return string

    def solve(self, string: str):
        if self.wrong_parentheses(string) or self.has_whitespaces(string) or self.has_something_else(string):
            return "WRONG"

        signs = "-+*"
        polish = ""
        st = deque()
        to_skip = 0
        for i, sym in enumerate(string):
            if to_skip:
                to_skip -= 1
                continue
            if sym == " ":
                continue
            if sym.isdigit():
                digit_str = ""
                while i < len(string) and string[i].isdigit():
                    digit_str += string[i]
                    i += 1
                polish += digit_str + " "
                to_skip = len(digit_str) - 1
            elif sym in signs:
                if sym in "-+":
                    while st and st[-1] in "*-+":
                        polish += st.pop() + " "
                st.append(sym)
            elif sym == "(":
                st.append(sym)
            elif sym == ")":
                while st and st[-1] != "(":
                    polish += st.pop() + " "
                st.pop()
        while st:
            polish += st.pop() + " "
        return self.calculate_polish(polish)

    @staticmethod
    def wrong_parentheses(string):
        counter = 0
        for sym in string:
            if sym == "(":
                counter += 1
            elif sym == ")":
                counter -= 1
                if counter < 0:
                    return True
        return counter != 0

    @staticmethod
    def has_whitespaces(string):
        sighs = "+-*"
        string = string.strip("()")
        if string[0] in sighs or string[-1] in sighs:
            return True
        previous = ""
        had_digit = False
        had_sign = False
        for sym in string:
            if sym in sighs:
                if had_sign:
                    return True
                else:
                    had_digit = False
                    had_sign = True
            elif had_digit and not previous.isdigit() and sym.isdigit():
                return True
            elif sym.isdigit():
                had_digit = True
                had_sign = False
            previous = sym
        return False

    @staticmethod
    def has_something_else(string):
        for sym in string:
            if not sym.isdigit() and not sym in " ()-+*":
                return True
        return False

    @staticmethod
    def calculate_polish(string):
        st = deque()
        signs = "+-*"
        for sym in string.split():
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
