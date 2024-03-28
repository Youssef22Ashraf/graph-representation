from collections import defaultdict #subclass of dict
import networkx as nx # creating and manipulating graph
from matplotlib import pyplot as plt # create static visualization
from typing import List, Tuple
paths = 0
def new_edge(adjacency_list: List[List[int]], u: int, v: int):
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)
    global paths
    paths += 1
def list_to_matrix(adjacency_list: List[List[int]], matrix: List[List[int]]):
    for v in range(len(adjacency_list)):
        print(f"Adjacency list of vertex {v}:")
        print("head", end=" ")
        for x in adjacency_list[v]:
            print(f"-> {x}", end=" ")
            matrix[v][x] = 1
        print()
def print_matrix_graph(matrix: List[List[int]]):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()
class GraphVisualization:
    def __init__(self):
        self.visual = []
    def addEdge(self, t):
        self.visual.append(t) #This method appends a tuple t representing an edge to the visual list.
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()
def convert(a):
    adjList = defaultdict(list)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 1:
                adjList[i].append(j)
    return adjList
nmatrix = [[0, 1, 0, 0, 1], [1, 0, 1, 1, 1],
           [0, 1, 0, 1, 0, ], [0, 1, 1, 0, 0],
           [1, 1, 0, 1, 0], ]
a = nmatrix
AdjList = convert(a)
resultList = [[key, value] for key, value in AdjList.items()]
z = []
for x in resultList:
    for i in range(len(x)):
        if isinstance(x[i], int):
            for item in x[i + 1]:
                z.append([x[i], item])
G = GraphVisualization()
for i in range(len(z)):
    G.addEdge(z[i])
def main():
    V = 5
    matrix = [[0] * V for _ in range(V)]
    adjacency_list = [[] for _ in range(V)]
    new_edge(adjacency_list, 0, 1)
    new_edge(adjacency_list, 0, 4)
    new_edge(adjacency_list, 1, 2)
    new_edge(adjacency_list, 1, 3)
    new_edge(adjacency_list, 1, 4)
    new_edge(adjacency_list, 2, 3)
    new_edge(adjacency_list, 3, 4)
    list_to_matrix(adjacency_list, matrix)
    print_matrix_graph(matrix)
    print(f"Paths: {paths}")
    G.visualize()
if __name__ == "__main__":
    main()