class Solution:

    @staticmethod
    def get_input():
        with open("input.txt", "r") as f:
            raw = f.readlines()
        return [row.split() for row in raw]

    @staticmethod
    def solve(command_list):
        root = None
        values_set = set()
        for command in command_list:
            if len(command) == 2:
                command_text = command[0]
                command_value = int(command[1])
                if command_text == "ADD":
                    if root is None:
                        root = BTNode(command_value)
                        print("DONE")
                    else:
                        print(root.add(command_value))
                    values_set.add(command_value)
                elif command_text == "SEARCH":
                    if command_value in values_set:
                        print("YES")
                    else:
                        print("NO")
            else:
                root.print()

    def solve_from_input(self):
        self.solve(self.get_input())


class BTNode:

    def __init__(self, val, depth=0, left=None, right=None):
        self.val = val
        self.depth = depth
        self.left = left
        self.right = right

    def add(self, val, depth=0):
        if self.val == val:
            return "ALREADY"
        elif val > self.val:
            if self.right is None:
                self.right = BTNode(val, depth + 1)
                return "DONE"
            else:
                return self.right.add(val, depth + 1)
        elif val < self.val:
            if self.left is None:
                self.left = BTNode(val, depth + 1)
                return "DONE"
            else:
                return self.left.add(val, depth + 1)

    def print(self):
        if self.left:
            self.left.print()
        print("." * self.depth + str(self.val))
        if self.right:
            self.right.print()


if __name__ == "__main__":
    solution = Solution()
    solution.solve_from_input()
