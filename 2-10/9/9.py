"""
Алгоритм Беллмана-Форда используется для нахождения кратчайшего пути взвешенного графа с отрицательными весами ребер.
Он также может использоваться в графах без отрицательных ребер.
Алгоритм состоит из следующих шагов:
1. На входе алгоритма имеем граф G, множество вершин V и множество ребер E, а также вершину A.
2. Инициализируем все вершины значениями бесконечность, кроме вершины A
,которой присваиваем значение 0.
3. Повторяем следующее действие V - 1 раз, где V - количество вершин в графе:
a. Итерируемся по всем ребрам графа E.
b. Для каждого ребра выполняем релаксацию, т.е. проверяем, можем ли мы 
улучшить длину пути до конечной вершины ребра ,используя текущую вершину и длину ребра. 
c. Если длина пути до конечной вершины улучшается, то обновляем ее значение. 
4. Выполняем проверку на наличие отрицательных циклов в графе. Для этого повторяем итерацию релаксации для каждого
ребра. Если значение какой-либо вершины продолжает уменьшаться после V-1 итерации, 
то в графе есть отрицательный цикл. 
В другом случае, кратчайший путь до каждой вершины найден.
5. Окончательный результат представляет собой значение кратчайшего пути до каждой вершины из вершины A.
"""

input_file = '/Users/a.sagitovich/programming/BFU/ASD/2-10/6/graph.txt'


def bellman_ford(graph, start_vertex):
    # инициализация списков
    distances = [float('inf')] * len(graph)
    predecessors = [None] * len(graph)

    distances[start_vertex] = 0  # расстояние до стартовой вершины равно 0

    # проходимся по всем ребрам графа
    for _ in range(len(graph)-1):
        for u in range(len(graph)):
            for v in range(len(graph)):
                if graph[u][v] != 0 and distances[u] + graph[u][v] < distances[v]:
                    distances[v] = distances[u] + graph[u][v]
                    predecessors[v] = u

    return distances, predecessors


# считываем граф из файла
with open(input_file, 'r') as f:
    graph = []
    for line in f:
        graph.append(list(map(int, line.strip().split())))

# запускаем алгоритм Беллмана-Форда
start_vertex = 0
distances, predecessors = bellman_ford(graph, start_vertex)


# выводим результат
print("Кратчайшие расстояния от вершины {} до остальных вершин:".format(start_vertex))
for i in range(len(distances)):
    print("До вершины {}: {}".format(i, distances[i]))


import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

matrix_g = np.loadtxt('/Users/a.sagitovich/programming/BFU/ASD/2-10/9/input_.txt')
# Создаем граф из матрицы смежности
graph_to_show = nx.from_numpy_array(matrix_g)
# Рисуем граф
nx.draw(graph_to_show, with_labels=True)
plt.show()