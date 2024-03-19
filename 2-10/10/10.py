
"""
Алгоритм нахождения эйлерова цикла в неориентированном графе заключается в следующем:
1. Проверяем граф на наличие эйлерова цикла. Это возможно только если степени всех 
вершин графа четные.
2. Находим произвольную вершину и запускаем DFS, в каждой вершине отмечая пройденные ребра 
и вершины.
3. Если мы дошли до вершины, из которой мы начали обход, и прошли все ребра, 
то граф содержит эйлеров цикл.
4. Если граф не содержит эйлеров цикл, то берем вершину из стека, у которой еще остались
непройденные ребра, и повторяем шаги 2-3, начиная с этой вершины.
5. В конце обхода, если список ребер, которые мы прошли, содержит все ребра графа, 
то граф содержит эйлеров цикл.
"""


def find_euler_cycle(adj_matrix_):
    # Список, где будем хранить путь
    cycle = []
    # Находим стартовую вершину
    start_vertex = 0
    # Создаем копию матрицы смежности, чтобы не изменять оригинал
    adj_matrix_copy = [row[:] for row in adj_matrix_]
    while True:
        # Получаем список возможных следующих вершин
        next_vertices = find_next_vertices(adj_matrix_copy, start_vertex)
        if not next_vertices:
            # Если список пуст, то мы нашли эйлеров цикл
            break
        # Если следующая вершина только одна, то добавляем её в путь
        if len(next_vertices) == 1:
            cycle.append(next_vertices[0])
        else:
            # Если следующих вершин несколько, то выбираем любую
            # и добавляем её в путь
            cycle.append(next_vertices[0])
        # Удаляем ребро между последней добавленной вершиной и новой вершиной
        if len(cycle) > 1:
            adj_matrix_copy[cycle[-1]][cycle[-2]] = 0
            adj_matrix_copy[cycle[-2]][cycle[-1]] = 0

        # Обновляем start_vertex
        start_vertex = next_vertices[0]

        if all(all(v == 0 for v in row) for row in adj_matrix_copy):
            break
    return cycle


def find_next_vertices(adj_matrix, vertex):
    """Получаем список возможных следующих вершин"""
    next_vertices = []
    for i in range(len(adj_matrix[vertex])):
        if adj_matrix[vertex][i] == 1:
            # Если ребро существует, добавляем вершину в список
            next_vertices.append(i)
    return next_vertices


# Чтение входных данных
with open('/Users/a.sagitovich/programming/BFU/ASD/2-10/10/input.txt') as f:
    n = int(f.readline())
    adj_matrix = [list(map(int, f.readline().split())) for _ in range(n)]

# Находим эйлеров цикл
euler_cycle = find_euler_cycle(adj_matrix)

# Вывод результата
print("Эйлеров цикл в графе состоит из следующих вершин:")
print(' '.join(map(str, [v for v in euler_cycle])))


import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

matrix_g = np.loadtxt('/Users/a.sagitovich/programming/BFU/ASD/2-10/10/input_.txt')
# Создаем граф из матрицы смежности
graph_to_show = nx.from_numpy_array(matrix_g)
# Рисуем граф
nx.draw(graph_to_show, with_labels=True)
plt.show()
