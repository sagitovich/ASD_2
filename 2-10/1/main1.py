import numpy as np
import networkx as nx
from collections import deque
import matplotlib.pyplot as plt


# Считываем матрицу смежности из файла
matrix = np.loadtxt('matrix1')

# Создаем граф из матрицы смежности
G = nx.from_numpy_array(matrix)


def bfs(graph, root):  # root - стартовая вершина
    visited = [False] * len(graph.nodes())  # для отслеживания посещенных вершин
    queue = deque([root])  # нужно посетить
    visited[root] = True
    steps = {root: 0}  # Словарь для отслеживания количества шагов

    print("Порядок обхода вершин графа в ширину из начальной вершины " + str(root) + ":")

    while queue:
        vertex = queue.popleft()
        print("Вершина " + str(vertex) + ", количество шагов: " + str(steps[vertex]))

        for neighbour in graph[vertex]:
            if not visited[neighbour]:
                queue.append(neighbour)
                visited[neighbour] = True
                steps[neighbour] = steps[vertex] + 1  # Увеличиваем количество шагов на 1


# Находим кратчайшие пути из вершины 0 до всех остальных вершин
bfs(G, 0)

# Рисуем граф
nx.draw(G, with_labels=True)
plt.show()
