"""
Чтобы найти количество и состав компонент связности в графе,
используется алгоритм поиска в глубину (Depth-First Search, DFS).

Алгоритм состоит из следующих шагов:
1. Устанавливаем все вершины графа как не посещенные.
2. Запускаем поиск в глубину из каждой вершины, которая еще не была обнаружена.
3. При запуске поиска в глубину создаем новый компонент связности.
4. В процессе поиска в глубину отмечаем каждую посещенную вершину
    как посещенную и добавляем ее в текущий компонент связности.
5. Когда поиск в глубину завершается, текущий компонент связности сохраняется,
    и переходим к следующей еще не посещенной вершине.
6. По окончании обхода графа количество компонент связности соответствует количеству сохраненных компонентов,
    а состав каждой компоненты хранится в соответствующих списках или массивах.
"""
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


# создаем функцию, которая будет открывать файл с матрицей смежности и считывать данные из него:
# Эта функция открывает файл, читает его содержимое и возвращает матрицу смежности в виде двумерного списка.
def readGraph(filename_):
    graph_ = []
    with open(filename_) as file:
        for line in file:
            row = list(map(int, line.strip().split()))
            graph_.append(row)
    return graph_


filename = "graph.txt"
graph = readGraph(filename)


def dfs(graph_, visited, start, component_):  # Далее мы определяем функцию для поиска в глубину:
    visited[start] = True
    component_.append(start)
    for item in range(len(graph_)):
        if graph_[start][item] == 1 and not visited[item]:
            dfs(graph_, visited, item, component_)


def findComponents(graph_):
    visited = [False] * len(graph_)
    components_ = []
    for item in range(len(graph_)):
        if not visited[item]:
            component_ = []
            dfs(graph_, visited, item, component_)
            components_.append(component_)
    return components_


matrix_g = np.loadtxt('graph.txt')
# Создаем граф из матрицы смежности
graph_to_show = nx.from_numpy_array(matrix_g)

components = findComponents(graph)
print(f"Количество связностей: {len(components)}")
for i, component in enumerate(components):
    print(f"Связность {i + 1}: {component}")

# Рисуем граф
nx.draw(graph_to_show, with_labels=True)
plt.show()
