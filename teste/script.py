import pydot, os, sys
import numpy as np

def h(graph, is_digraph):
    matrix = np.zeros((len(graph.nodes), len(graph.nodes)), dtype=int)

    for (a, b) in graph.edges:
        row_index = graph.nodes.index(a)
        col_index = graph.nodes.index(b)
        matrix[row_index][col_index] = 1

        if (is_digraph):
            matrix[col_index][row_index] = -1

    return matrix

# Constantes
GRAPH = "graph"
DIGRAPH = "digraph"

# Lidando com leitura de arquivos
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

# criando lista de nodes
nodes = set()

for (a, b) in edges:
    nodes.add(a)
    nodes.add(b)

graph.nodes = sorted(nodes)
graph.edges = edges

# Switch case
adjacency_matrix = h(graph, graph.get_type() == DIGRAPH)

print(adjacency_matrix)