class TNode:

    def __init__(self, cost):
        self.conn = []
        self.cost = cost
        self.tagged = True

    def add_child(self, node):
        self.conn.append(node)
        node.conn.append(self)

    def have_near_tagged(self):
        if self.tagged:
            return True
        for ch in self.conn:
            if ch.tagged:
                return True
        return False

    def all_connections_are_valid(self):
        if not self.tagged:
            for ch in self.conn:
                if not ch.tagged:
                    return False
        return True

    def calculate_obligatory(self):
        obligatory_cost = 0
        for ch in self.conn:
            if len(ch.conn) == 1:
                obligatory_cost += ch.cost
        return obligatory_cost

    def switch_off_lone_conns(self):
        less = 0
        for ch in self.conn:
            if len(ch.conn) == 1:
                less += ch.cost
                ch.tagged = False
        return less

    def ok_to_switch_off(self):
        for ch in self.conn:
            if not ch.tagged:
                return False
        return True

class Solution:

    @staticmethod
    def get_input():
        with open("input.txt", "r") as f:
            raw = f.readlines()
            n = int(raw[0])
            connections = []
            for i in range(1, len(raw) - 1):
                split_ = raw[i].split()
                if split_:
                    first = int(split_[0])
                    second = int(split_[1])
                    if first < second:
                        connections.append((first, second))
                    else:
                        connections.append((second, first))
            costs = list(map(int, raw[-1].split()))
        return n, connections, costs

    def solve(self, n, connections, costs):
        if not connections:
            return [costs[0], 1, [1]]
        connections = sorted(connections, key=lambda x: x[0])

        existing_nodes = self.build_tree(n, connections, costs)

        total_cost = 0
        for cost in costs:
            total_cost += cost

        for node in existing_nodes:
            obligatory = node.calculate_obligatory()
            if obligatory >= node.cost:
                less = node.switch_off_lone_conns()
                total_cost -= less
        profits = []
        for i, node in enumerate(existing_nodes):
            if node.tagged:
                profits.append((i, node.cost))
        profits = sorted(profits, key=lambda x: -x[1])

        for i, _ in profits:
            node = existing_nodes[i]
            if node.ok_to_switch_off():
                node.tagged = False
                total_cost -= node.cost
        nodes_to_tag = [i + 1 for i, node in enumerate(existing_nodes) if node.tagged]

        return total_cost, len(nodes_to_tag), nodes_to_tag


    def solve_from_input(self):
        result = self.solve(*self.get_input())
        print(result[0], result[1])
        print(*result[2])

    @staticmethod
    def build_tree(n: int, connections: list, costs: list) -> list[TNode]:
        root = None
        i = 0
        existing_nodes = [None] * n
        while i < len(connections):
            first_val = connections[i][0]
            second_val = connections[i][1]
            i += 1
            if existing_nodes[first_val - 1] is None:
                first = TNode(costs[first_val - 1])
                if root is None and first_val == 1:
                    root = first
            else:
                first = existing_nodes[first_val - 1]

            if existing_nodes[second_val - 1] is None:
                second = TNode(costs[second_val - 1])
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
        return existing_nodes


if __name__ == "__main__":
    solution = Solution()
    solution.solve_from_input()
