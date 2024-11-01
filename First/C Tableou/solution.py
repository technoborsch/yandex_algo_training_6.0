def find_letters(m):
    main_square, has_wrongs = find_squares(m, "#", (0, len(m) - 1, 0, len(m) - 1), True)
    if not main_square or len(main_square) > 1 or has_wrongs:
        return "X"  # Не найден основной прямоугольник
    else:
        # print(main_square[0], has_wrongs)
        main_square = main_square[0]
        inner_squares, has_wrong = find_squares(m, ".", main_square, False)
        # print(inner_squares, has_wrong)
        if has_wrong:
            return "X"
        elif len(inner_squares) == 0:  # Точно I
            return "I"
        elif len(inner_squares) == 1:  # Может быть O, L, C
            figure = inner_squares[0]
            if (touches_up(figure, main_square)
                    and touches_right(figure, main_square)
                    and not touches_left(figure, main_square)
                    and not touches_down(figure, main_square)):
                return "L"
            elif (not touches_up(figure, main_square)
                  and not touches_down(figure, main_square)
                  and not touches_left(figure, main_square)
                  and not touches_right(figure, main_square)):
                return "O"
            elif (touches_right(figure, main_square)
                  and not touches_down(figure, main_square)
                  and not touches_left(figure, main_square)
                  and not touches_up(figure, main_square)):
                return "C"
            else:
                return "X"
        elif len(inner_squares) == 2:  # Может быть H и P
            first_square = inner_squares[0]
            second_square = inner_squares[1]
            if (touches_up(first_square, main_square)
                    and not touches_down(first_square, main_square)
                    and not touches_left(first_square, main_square)
                    and not touches_right(first_square, main_square)
                    and touches_down(second_square, main_square)
                    and not touches_up(second_square, main_square)
                    and not touches_left(second_square, main_square)
                    and not touches_right(second_square, main_square)
                    and first_square[0] == second_square[0]
                    and first_square[1] == second_square[1]
                    and first_square[3] < second_square[2]):
                return "H"
            elif (not touches_up(first_square, main_square)
                    and not touches_down(first_square, main_square)
                    and not touches_left(first_square, main_square)
                    and not touches_right(first_square, main_square)
                    and touches_down(second_square, main_square)
                    and not touches_up(second_square, main_square)
                    and not touches_left(second_square, main_square)
                    and touches_right(second_square, main_square)
                    and first_square[0] == second_square[0]
                    and first_square[3] < second_square[2]):
                return "P"
            else:
                return "X"
        else:
            return "X"


def touches_up(figure, area):
    return figure[2] == area[2]


def touches_down(figure, area):
    return figure[3] == area[3]


def touches_left(figure, area):
    return figure[0] == area[0]


def touches_right(figure, area):
    return figure[1] == area[1]


def find_squares(m: list[str], sym_to_search, search_area, allow_inner):
    square_list = []
    figure = []
    figure_start_row = None
    has_wrongs = False

    for i in range(search_area[2], search_area[3] + 1):
        row = m[i]
        left = None
        right = None
        for j in range(search_area[0], search_area[1] + 1):
            if row[j] == sym_to_search:
                if figure_start_row is None:
                    figure_start_row = i
                left = j
                break
        for k in range(search_area[1], search_area[0] - 1, -1):
            if row[k] == sym_to_search:
                right = k
                break
        if right is not None and left is not None:
            figure.append((left, right))
        if right is None and figure_start_row is not None:
            validated_figure = validate_figure(m, figure, figure_start_row, sym_to_search, allow_inner)
            if validated_figure:
                square_list.append(validated_figure)
            else:
                has_wrongs = True
            figure = []
            figure_start_row = None
        elif i == search_area[3] and figure:
            validated_figure = validate_figure(m, figure, figure_start_row, sym_to_search, allow_inner)
            if validated_figure:
                square_list.append(validated_figure)
            else:
                has_wrongs = True
            figure = []
            figure_start_row = None

    return square_list, has_wrongs


def validate_figure(m, figure, start_row, sym_to_search, allow_inner):
    left = None
    right = None
    for i in range(len(figure)):
        m_i = i + start_row
        row_left, row_right = figure[i]
        if left is None:
            left = row_left
        elif row_left != left:
            if not allow_inner:
                return
            else:
                if row_left < left:
                    left = row_left
        if right is None:
            right = row_right
        elif row_right != right:
            if not allow_inner:
                return
            else:
                if row_right > right:
                    right = row_right
        if not allow_inner:
            for j in range(left, right + 1):
                if m[m_i][j] != sym_to_search:
                    return
    return left, right, start_row, start_row + len(figure) - 1


if __name__ == "__main__":
    #from test_cases import cases
    #for case in cases:
    #    result = case[0]
    #    input_ = case[1]
    #    this_result = find_letters(input_)
    #    if this_result != result:
    #        print(f"Неверное решение, Keйс {result}, выдано {this_result}", )
    #        for string in input_:
    #            print(string)
    with open("input.txt", "r") as f:
        raw = f.readlines()
    matrix = raw[1:]
    print(find_letters(matrix))
