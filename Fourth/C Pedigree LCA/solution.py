import sys

sys.setrecursionlimit(100000)


class Solution:

    @staticmethod
    def get_input():
        with open("input.txt", "r") as f:
            raw = f.readlines()
            n = int(raw[0])
            relations = [raw[i].split() for i in range(1, n)]
            queries = [raw[i].split() for i in range(n, len(raw))]
        return n, relations, queries

    def solve(self, n, relations, queries):
        existing_nodes = {}
        for child_name, parent_name in relations:
            if parent_name not in existing_nodes:
                parent = TNode(parent_name)
                existing_nodes[parent_name] = parent
            else:
                parent = existing_nodes[parent_name]
            if child_name not in existing_nodes:
                child = TNode(child_name)
                existing_nodes[child_name] = child
            else:
                child = existing_nodes[child_name]
            parent.add_child(child)
        result = []
        for first, second in queries:
            result.append(self.get_lca(existing_nodes[first], existing_nodes[second]))
        return result

    def get_lca(self, first, second):
        first_ancestry = self.get_ancestors(first)
        second_ancestry = self.get_ancestors(second)
        previous = None
        for i in range(len(first_ancestry)):
            one = first_ancestry[len(first_ancestry) - i - 1]
            two = second_ancestry[len(second_ancestry) - i - 1]
            if one and two and one == two:
                previous = one
            else:
                return previous

    @staticmethod
    def get_ancestors(node):
        result = [None]
        this_node = node
        while this_node:
            result.append(this_node.val)
            this_node = this_node.p
        return result

    def solve_from_input(self):
        for item in self.solve(*self.get_input()):
            print(item)


class TNode:

    def __init__(self, val, parent=None, children: list=None):
        if children is None:
            children = []
        self.p = parent
        self.ch = children
        self.val = val
        self.t_child = None

    def add_child(self, node):
        self.ch.append(node)
        node.p = self

    def set_tot_child_count(self):
        if self.t_child is None:
            self.t_child = 0
            for child in self.ch:
                self.t_child += child.set_tot_child_count()
        return self.t_child + 1


if __name__ == "__main__":
    solution = Solution()
    solution.solve_from_input()
