"""
Алгоритм Прима работает по следующему принципу:
1. Выбирается произвольная стартовая вершина.
2. Создается список доступных ребер, которые не входят в дерево, и сортируется по возрастанию весов.
3. Из списка доступных ребер выбирается ребро с наименьшим весом и добавляется в дерево.
4. Добавляются все вершины, соединенные выбранным ребром, в список посещенных.
5. Обновляется список доступных ребер, исключая те, которые соединены с вершинами, уже находящимися в дереве.
6. Выполняются шаги 3-5, пока не будут рассмотрены все вершины графа.
"""

# чтение матрицы смежности из файла
with open('/Users/a.sagitovich/programming/BFU/ASD/2-10/6/graph.txt', "r") as f:
    n = int(f.readline().strip())  # число вершин
    matrix = [[int(j) for j in f.readline().strip().split()] for i in range(n)]

# инициализация списка ребер дерева
edges = []
# инициализация списка посещенных вершин
visited = [0]
# инициализация списка доступных ребер
available_edges = [(i, j, matrix[i][j]) for i in range(n) for j in range(i) if matrix[i][j] != 0 and 
                   (i in visited) != (j in visited)]

# проход по всем вершинам графа
for i in range(n-1):
    # поиск ребра с наименьшим весом среди доступных ребер
    e = min(available_edges, key=lambda x: x[2])
    # добавление ребра к дереву
    edges.append(e)
    # добавление новой вершины в список посещенных
    new_vertex = e[0] if e[1] in visited else e[1]
    visited.append(new_vertex)
    # обновление списка доступных ребер
    available_edges = [(i, j, matrix[i][j]) for i in range(n) for j in range(i) if matrix[i][j] != 0 and 
                       ((i in visited) != (j in visited)) and ((i, j) not in edges) and ((j, i) not in edges)]

# вывод результирующего списка ребер
print("Минимальное остовное дерево состоит из следующих ребер:")
for e in edges:
    print("Ребро между вершинами {} и {}, вес ребра: {}".format(e[0], e[1], e[2]))

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

matrix_g = np.loadtxt('/Users/a.sagitovich/programming/BFU/ASD/2-10/7/graph_.txt')
# Создаем граф из матрицы смежности
graph_to_show = nx.from_numpy_array(matrix_g)
# Рисуем граф
nx.draw(graph_to_show, with_labels=True)
plt.show()