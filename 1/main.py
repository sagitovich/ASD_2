import numpy as np
import matplotlib.pyplot as plt


def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # коллинеарны
    return 1 if val > 0 else 2  # против часовой стрелки или по часовой стрелке


def jarvis(point_list):
    n = len(point_list)
    points_numbers = list(range(n))

    for i in range(1, n):
        if point_list[points_numbers[i]][0] < point_list[points_numbers[0]][0]:
            points_numbers[i], points_numbers[0] = points_numbers[0], points_numbers[i]

    MCH = [points_numbers[0]]  # создаём список с правильным порядком вершин МВО
    del points_numbers[0]
    points_numbers.append(MCH[0])

    while True:
        right = 0
        for i in range(1, len(points_numbers)):  # ищем самую правую точку
            o = orientation(point_list[MCH[-1]], point_list[points_numbers[right]], point_list[points_numbers[i]])
            if o == 2 or (o == 1 and orientation(point_list[MCH[-1]], point_list[points_numbers[i]], point_list[points_numbers[right]]) == 0):
                right = i

        if points_numbers[right] == MCH[0]:
            break
        else:
            MCH.append(points_numbers[right])
            del points_numbers[right]

    return [point_list[i] for i in MCH]


def main():
    num_points = int(input("Введите количество точек: "))
    points = []
    for i in range(num_points):
        x, y = map(float, input(f"Введите координаты точки {i + 1}: ").split())
        points.append([x, y])

    hull = jarvis(points)

    print("\nМинимальная выпуклая оболочка:")
    for i in hull:
        print(i)

    points = np.array(points)
    plt.plot(points[:, 0], points[:, 1], 'o')
    for i in range(len(hull)):
        plt.plot([hull[i][0], hull[(i + 1) % len(hull)][0]], [hull[i][1], hull[(i + 1) % len(hull)][1]], 'k-')
    plt.show()


if __name__ == "__main__":
    main()
