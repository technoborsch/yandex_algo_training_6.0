class Solution:

    @staticmethod
    def get_input():
        with open("input.txt", "r") as f:
            raw = f.readlines()
            n = int(raw[0])
            relations = [raw[i].split() for i in range(1, len(raw))]
        return n, relations

    @staticmethod
    def solve(n, relations):
        root = None
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
        for node in existing_nodes.values():
            if node.p is None:
                root = node
                break
        root.set_depth()
        return sorted([" ".join((name, str(node.depth))) for name, node in existing_nodes.items()])


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
        self.depth = None

    def add_child(self, node):
        self.ch.append(node)
        node.p = self

    def set_depth(self, level=0):
        self.depth = level
        for child in self.ch:
            child.set_depth(level + 1)


if __name__ == "__main__":
    solution = Solution()
    solution.solve_from_input()
