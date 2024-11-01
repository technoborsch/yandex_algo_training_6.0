with open("input.txt", "r") as f:
    x1, y1, x2, y2, x, y = list(map(int, f.readlines()))
if x < x1:                   # Слева от плота
    if y > y2:               # Левый верхний угол
        print("NW")
    elif y1 < y < y2:        # Ближе к левой стороне
        print("W")
    elif y < y1:             # Нижний левый угол
        print("SW")
elif x1 < x < x2:            # Выше или ниже плота
    if y > y2:
        print("N")           # Верхняя сторона
    elif y < y1:
        print("S")           # Нижняя сторона
elif x > x2:                 # Справа от плота
    if y > y2:               # Правый верхний угол
        print("NE")
    elif y1 < y < y2:        # Ближе к правой стороне
        print("E")
    elif y < y1:             # Нижний правый угол
        print("SE")
