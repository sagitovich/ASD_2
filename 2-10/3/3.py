"""
Поиск в ширину
1. Создать очередь вершин и поместить в нее начальную вершину.
2. Пометить начальную вершину как посещенную.
3. Пока очередь не пуста, извлечь из очереди вершину и записать ее в список обхода.
4. Добавить в очередь все непосещенные соседние вершины.
5. Пометить все добавленные вершины как посещенные.
6. Повторять шаги 3-5, пока очередь не станет пустой.
7. Вернуть список вершин обхода.
"""
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from collections import deque


def read_graph(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    matrix_ = []
    for line in lines:
        row = [int(x) for x in line.strip().split()]
        matrix_.append(row)
    return matrix_


def bfs(graph_, visited, queue, component_):
    while queue:
        vertex = queue.popleft()
        for neighbor, edge_exists in enumerate(graph_[vertex]):
            if edge_exists and not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                component_.append(neighbor)


def find_connected_components(graph_):
    visited = [False] * len(graph_)
    components_ = []
    for vertex in range(len(graph_)):
        if not visited[vertex]:
            visited[vertex] = True
            queue = deque([vertex])
            component_ = [vertex]
            bfs(graph_, visited, queue, component_)
            components_.append(component_)
    return components_


matrix_g = np.loadtxt('graph.txt')
# Создаем граф из матрицы смежности
graph = nx.from_numpy_array(matrix_g)

matrix = read_graph('graph.txt')
components = find_connected_components(matrix)

print(f"Numbers of components: {len(components)}")
for i, component in enumerate(components):
    print(f"Component {i + 1}: {component}")

# Рисуем граф
nx.draw(graph, with_labels=True)
plt.show()
