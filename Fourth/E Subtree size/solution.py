import sys

sys.setrecursionlimit(100000)


class Solution:

    @staticmethod
    def get_input():
        with open("input.txt", "r") as f:
            raw = f.readlines()
            n = int(raw[0])
            connections = []
            for i in range(1, len(raw)):
                split_ = raw[i].split()
                first = int(split_[0])
                second = int(split_[1])
                if first < second:
                    connections.append((first, second))
                else:
                    connections.append((second, first))
        return n, connections

    @staticmethod
    def solve(n, connections):
        connections = sorted(connections, key=lambda x: x[0])
        result = []
        root = None
        existing_nodes = [None] * n
        i = 0
        while i < len(connections):
            first_val = connections[i][0]
            second_val = connections[i][1]
            i += 1
            if existing_nodes[first_val - 1] is None:
                first = TNode(first_val)
                if root is None and first_val == 1:
                    root = first
            else:
                first = existing_nodes[first_val - 1]

            if existing_nodes[second_val - 1] is None:
                second = TNode(second_val)
                if root is None and second_val == 1:
                    root = second
            else:
                second = existing_nodes[second_val - 1]

            if existing_nodes[second_val - 1]:
                second.add_child(first)
            elif existing_nodes[first_val - 1]:
                first.add_child(second)
            else:
                if first is root:
                    first.add_child(second)
                elif second is root:
                    second.add_child(first)
                else:
                    connections.append((first_val, second_val))
                    continue

            existing_nodes[first_val - 1] = first
            existing_nodes[second_val - 1] = second
        root.set_subtree()
        for node in existing_nodes:
            result.append(node.sub)

        return result

    def solve_from_input(self):
        print(*self.solve(*self.get_input()))


class TNode:

    def __init__(self, val, parent=None, children: list=None):
        if children is None:
            children = []
        self.p = parent
        self.ch = children
        self.val = val
        self.sub = 1

    def add_child(self, node):
        self.ch.append(node)
        node.p = self

    def set_subtree(self):
        for child in self.ch:
            self.sub += child.set_subtree()
        return self.sub


if __name__ == "__main__":
    solution = Solution()
    solution.solve_from_input()
