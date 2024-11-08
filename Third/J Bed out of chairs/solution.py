from collections import deque


class Solution:

    @staticmethod
    def get_input():
        with open("input.txt", "r") as f:
            raw = f.readlines()
            n, h = list(map(int, raw[0].split()))
            heights = list(map(int, raw[1].split()))
            widths = list(map(int, raw[2].split()))
        return n, h, heights, widths

    @staticmethod
    def solve(n, h, heights, widths) -> int:
        zipped = list(zip(heights, widths))
        zipped = sorted(zipped, key=lambda x: x[0])
        dq = deque()
        this_width = 0
        i = 0
        max_diff = None
        prev_h = None
        for chair_height, chair_width in zipped:
            this_width += chair_width
            dq.append((chair_height, chair_width))
            if this_width >= h:
                if prev_h:
                    if max_diff is None:
                        max_diff = chair_height - prev_h
                    else:
                        max_diff = max(max_diff, chair_height - prev_h)
                chair_out = dq.popleft()
                this_width -= chair_out[1]
            prev_h = chair_height

        return max_diff

    def solve_from_input(self):
        print(self.solve(*self.get_input()))


if __name__ == "__main__":
    solution = Solution()
    solution.solve_from_input()
