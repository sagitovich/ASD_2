import numpy as np
import networkx as nx
from collections import deque
import matplotlib.pyplot as plt

# Считываем матрицу смежности из файла
matrix = np.loadtxt('matrix')

# Создаем граф из матрицы смежности
G = nx.from_numpy_array(matrix)


def bfs(graph):
    visited = [False] * len(graph.nodes())  # для отслеживания посещенных вершин
    all_components = []  # список для хранения компонент связности

    for root in range(len(graph.nodes())):  # обходим все вершины графа
        if not visited[root]:  # если вершина еще не посещена
            component = []  # создаем новую компоненту связности
            queue = deque([root])  # добавляем вершину в очередь
            visited[root] = True

            while queue:
                vertex = queue.popleft()
                component.append(vertex)  # добавляем вершину в компоненту связности

                for neighbour in graph[vertex]:
                    if not visited[neighbour]:
                        queue.append(neighbour)
                        visited[neighbour] = True

            all_components.append(component)  # добавляем компоненту связности в список

    return all_components  # возвращаем список компонент связности


# Находим компоненты связности графа
components = bfs(G)

# Выводим количество и состав компонент связности
print("Количество компонент связности:", len(components))
for i, comp in enumerate(components, 1):
    print("Компонента связности", i, ":", comp)

# Рисуем граф
nx.draw(G, with_labels=True)
plt.show()


# Компонента связности - это подмножество вершин графа, в котором каждую пару вершин соединяет путь,
# и которое не связано с остальными вершинами графа.
