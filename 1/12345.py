from matplotlib import pyplot as plt


def rotate(point_A, point_B, point_C):
    return (point_B[0] - point_A[0]) * (point_C[1] - point_B[1]) - (point_B[1] - point_A[1]) * (point_C[0] - point_B[0])


def minimal_convex_hull(point_list):
    n = len(point_list)
    points_numbers = list(range(n))

    for i in range(1, n):  # если points_numbers[i]-ая
        if point_list[points_numbers[i]][0] < point_list[points_numbers[0]][0]:
            # меняем местами НОМЕРА этих точек
            points_numbers[i], points_numbers[0] = points_numbers[0], points_numbers[i]
    # теперь самая первая точка - самая левая (с наименьшей x-координатой)

    MCH = [points_numbers[0]]  # создаём список с правильным порядком вершин МВО
    del points_numbers[0]
    points_numbers.append(MCH[0])  # переносим стартовую вершину в конец

    # бесконечный цикл, на каждой итерации которого ищем самую правую точку
    # из points_numbers отн-но последней вершины в H
    while True:
        right = 0
        for i in range(1, len(points_numbers)):  # ищем самую правую точку
            if rotate(point_list[MCH[-1]], point_list[points_numbers[right]], point_list[points_numbers[i]]) <= 0:
                right = i

        if points_numbers[right] == MCH[0]:  # если она совпала со стартовой, то прерываем цикл
            break  # оболочка построена
        else:
            MCH.append(points_numbers[right])  # переносим эту вершину в МВО
            del points_numbers[right]

    return [point_list[i] for i in MCH]


def draw_points_and_hull(points, hull):
    # Разделение координат x и y
    x = [point[0] for point in points]
    y = [point[1] for point in points]

    # Рисование точек
    plt.scatter(x, y, color='blue')

    # Рисование минимальной выпуклой оболочки
    hull.append(hull[0])  # добавляем первую точку в конец, чтобы замкнуть оболочку
    hull_x = [point[0] for point in hull]
    hull_y = [point[1] for point in hull]
    plt.plot(hull_x, hull_y, 'r')

    # Показать график
    plt.show()


n = int(input('Количество точек - '))
list_of_points = []
print('Задайте точки:')
for i in range(n):
    list_of_points.append(list(map(int, input(f'{i + 1}) ').split())))

print(list_of_points)
hull = minimal_convex_hull(list_of_points)
print('МВО заданных точек составляют:', hull)

draw_points_and_hull(list_of_points, hull)
