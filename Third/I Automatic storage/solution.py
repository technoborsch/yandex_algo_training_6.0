from collections import deque


class Solution:

    @staticmethod
    def get_input():
        with open("input.txt", "r") as f:
            raw = f.readlines()
            n = int(raw[0])
            a, b = list(map(int, raw[1].split()))
            rovers = raw[2:]
        return n, a, b, rovers

    def solve(self, n: int, a, b, rovers) -> list[int]:
        result = []
        priorities = [0] * 4
        priorities[a - 1] = 1
        priorities[b - 1] = 1
        rovers = [tuple(map(int, x.split())) for x in rovers]
        rovers = list(zip(range(1, len(rovers) + 1), rovers))
        rovers = sorted(rovers, key=lambda x: (x[1][1], x[1][0]))
        max_time = rovers[-1][1][1]
        times = [None] * max_time
        for rover in rovers:
            time = rover[1][1] - 1
            side = rover[1][0] - 1
            if times[time] is None:
                times[time] = [0] * 4
            times[time][side] = rover[0]
        for i, time in enumerate(times):
            if time is None:
                times[i] = [0] * 4
        cross = [
            deque(),
            deque(),
            deque(),
            deque(),
        ]
        this_time = 0
        while cross[0] or cross[1] or cross[2] or cross[3] or this_time < len(times):
            if this_time < len(times):
                time = times[this_time]
                for side, index in enumerate(time):
                    if index:
                        cross[side].appendleft(index)
            cross_state = [0] * 4
            for i, side in enumerate(cross):
                if side and side[-1]:
                    cross_state[i] = 1
            go_list = [0] * 4
            for side in range(4):
                if self.can_go(priorities, side, cross_state):
                    go_list[side] = 1
            for side, can_go in enumerate(go_list):
                if can_go and cross[side]:
                    result.append((this_time + 1, cross[side].pop()))
            this_time += 1
        result = sorted(result, key=lambda x: x[1])
        result = [x[0] for x in result]
        return result

    def solve_from_input(self):
        result = self.solve(*self.get_input())
        for item in result:
            print(item)

    @staticmethod
    def can_go(priorities, side, cross_state):
        if priorities[side]:
            if not (priorities[side - 1] and cross_state[side - 1]):
                return True
            return False
        else:
            for i, priority in enumerate(priorities):
                if priority and cross_state[i]:
                    return False
            if not (priorities[side - 1] == 0 and cross_state[side - 1]):
                return True


if __name__ == "__main__":
    solution = Solution()
    solution.solve_from_input()
