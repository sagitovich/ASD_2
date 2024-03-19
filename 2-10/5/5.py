
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def read_graph(filename):
    matrix = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            matrix.append(list(map(int, line.strip().split())))

    return matrix


"""
Функция dfs является вспомогательной функцией для обхода в глубину, 
который используется на первом и втором этапах алгоритма.
"""


def dfs(graph, visited, start, component):
    visited[start] = True
    for i in range(len(graph)):
        if graph[start][i] == 1 and not visited[i]:
            dfs(graph, visited, i, component)
    component.append(start)


"""
Для поиска сильно связанных компонент ориентированного графа используется функция find_scc, 
которая сначала обходит граф в глубину для составления порядка обхода вершин, 
а затем обходит его еще раз, но уже в порядке убывания времени выхода из вершин,
чтобы найти все сильно связанные компоненты. Для поиска компонент на втором этапе 
используется транспонированный граф.
"""


def find_scc(graph):
    n = len(graph)
    visited = [False] * n
    order = []
    for i in range(n):
        if not visited[i]:
            dfs(graph, visited, i, order)
    transposed_graph = [[graph[j][i] for j in range(n)] for i in range(n)]
    for item in transposed_graph:
        print(item)

    for item in (order):
        print(item)
    visited = [False] * n
    scc_list = []
    for i in reversed(order):
        if not visited[i]:
            scc = []
            dfs(transposed_graph, visited, i, scc)
            scc_list.append(scc)
    return scc_list


input_file = "graph.txt"
graph = read_graph(input_file)
scc = find_scc(graph)

matrix_g = np.loadtxt('graph.txt')
# Создаем граф из матрицы смежности
graph_to_show = nx.from_numpy_array(matrix_g)

print(f"Количество сильных связностей: {len(scc)}")
for i, component in enumerate(scc):
    print(f"Связность {i + 1}: {component}")

# Рисуем граф
nx.draw(graph_to_show, with_labels=True)
plt.show()

