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

        chair_line = deque()
        this_width = 0
        max_diff = deque()
        prev_diff_right = None
        result = None
        for i, (chair_height, chair_width) in enumerate(zipped):
            # Если это не последний элемент, считаем текущую разницу вправо, иначе 0
            this_diff_right = 0
            if i < len(zipped) - 1:
                this_diff_right = zipped[i + 1][0] - chair_height
            # Если это не первый элемент, это предыдущая разница вправо, иначе 0
            this_diff_left = 0
            if i:
                this_diff_left = prev_diff_right
            prev_diff_right = this_diff_right
            # Сносим все более маленькие значения разниц влево и кладем в дек
            while max_diff and this_diff_left > max_diff[-1]:
                max_diff.pop()
            max_diff.append(this_diff_left)
            # Добавляем в кровать стул, считаем получившуюся ширину кровати
            this_width += chair_width
            chair_line.append((chair_height, chair_width, this_diff_right))
            # Если кровать уже по росту, пишем результат и удаляем стул, пока не станет меньше роста
            while this_width >= h:
                # Пишем результат
                if result is None:
                    result = max_diff[0]
                elif max_diff:
                    result = min(result, max_diff[0])
                else:
                    result = 0
                # Убираем стул слева
                chair_out_height, chair_out_width, chair_out_diff = chair_line.popleft()
                this_width -= chair_out_width
                # Если текущая наибольшая разница - это разница вправо удаляемого стула, убираем с деки
                if max_diff and chair_out_diff == max_diff[0]:
                    max_diff.popleft()

        return result

    def solve_from_input(self):
        print(self.solve(*self.get_input()))


if __name__ == "__main__":
    solution = Solution()
    solution.solve_from_input()
