import pydot, os, sys
import numpy as np

# Constants
GRAPH = "graph"
DIGRAPH = "digraph"

# Functions related to adjacency list and matrix
def get_adjacency_matrix(graph):
    is_digraph = graph.get_type() == DIGRAPH

    matrix = np.zeros((len(graph.nodes), len(graph.nodes)), dtype=int)

    for (a, b) in graph.edges:
        row_index = graph.nodes.index(a)
        col_index = graph.nodes.index(b)
        matrix[row_index][col_index] = 1

        if (is_digraph):
            matrix[col_index][row_index] = -1

    return matrix

def get_adjacency_list(graph):
    is_digraph = graph.get_type() == DIGRAPH

    list = [[graph.nodes[iterator]] for iterator in range(len(graph.nodes))]

    for (a, b) in graph.edges:
        list[graph.nodes.index(a)].append(b)
        if (not is_digraph):
            list[graph.nodes.index(b)].append(a)

    return list

# Handling file input and ARGV
dir = os.path.dirname(__file__)

if (len(sys.argv) >= 2):
    file_name = sys.argv[1]
else:
    file_name = input("Escreva o nome do arquivo, com a extensão: ")

file_path = dir + "\\data\\" + file_name

if (not os.path.exists(file_path)):
    print("O arquivo não existe na pasta 'data'!")
    sys.exit()

file = open(file_path)
dot_str = file.read()
file.close() 

# Parse DOT string
graphs = pydot.graph_from_dot_data(dot_str)
graph = graphs[0]

# Extract nodes and edges
edges = [(e.get_source(), e.get_destination()) for e in graph.get_edges()]

# Building node list
nodes = set()

for (a, b) in edges:
    nodes.add(a)
    nodes.add(b)

graph.nodes = sorted(nodes)
graph.edges = edges

# Setting data to work with BFS and DFS
adjacency_matrix = get_adjacency_matrix(graph)
adjacency_list = get_adjacency_list(graph)

print(adjacency_matrix)
print(adjacency_list)