"""
Код реализует алгоритм Дейкстры для нахождения кратчайших путей взвешенного графа с помощью матрицы смежности. 
Сначала считывается матрица смежности графа из файла "graph.txt". Затем запускается функция dijkstra, принимающая 
на вход матрицу смежности и индекс стартовой вершины. Функция реализует алгоритм Дейкстры на основе массива dist,
который содержит расстояния от стартовой вершины до всех остальных вершин. Изначально все элементы dist установлены 
на бесконечность, кроме элемента с индексом start, который равен 0. Массив visited содержит информацию о том, 
была ли уже посещена каждая вершина. В каждой итерации алгоритма находится вершина с наименьшим расстоянием в dist, 
которая еще не была посещена. Затем невоспроизводимость этой вершины помечается в массиве visited и расстояния до 
ее соседей обновляются, если новое расстояние оказывается меньше текущего. Далее функция возвращает массив dist 
с найденными расстояниями.
"""


def dijkstra(graph, start):
    n = len(graph)
    dist = [float("inf")] * n
    dist[start] = 0
    visited = [False] * n

    for i in range(n):
        min_dist = float("inf")
        min_index = -1
        for j in range(n):
            if not visited[j] and dist[j] < min_dist:
                min_dist = dist[j]
                min_index = j

        if min_index == -1:
            break

        visited[min_index] = True
        for k in range(n):
            if graph[min_index][k] != 0 and dist[k] > dist[min_index] + graph[min_index][k]:
                dist[k] = dist[min_index] + graph[min_index][k]
    return dist


with open("/Users/a.sagitovich/programming/BFU/ASD/2-10/6/graph.txt", "r") as f:
    # Считываем матрицу смежности из файла
    graph = []
    for line in f:
        row = list(map(int, line.strip().split()))
        graph.append(row)

    start = 0
    result = dijkstra(graph, start)
    
    # выводим результат
    print("Кратчайшие расстояния от вершины {} до остальных вершин:".format(start))
    for i, d in enumerate(result):
        print("До вершины {}: {}".format(i, d))


import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

matrix_g = np.loadtxt('/Users/a.sagitovich/programming/BFU/ASD/2-10/8/graph_.txt')
# Создаем граф из матрицы смежности
graph_to_show = nx.from_numpy_array(matrix_g)
# Рисуем граф
nx.draw(graph_to_show, with_labels=True)
plt.show()