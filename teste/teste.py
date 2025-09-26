import pydot

dot_str = """
    digraph nome_do_grafo {
      a -> b -> c;
      b -> d;
    }
"""

# Parse DOT string
graphs = pydot.graph_from_dot_data(dot_str)
graph = graphs[0]

# Extract nodes and edges
edges = [(e.get_source(), e.get_destination()) for e in graph.get_edges()]

print(graph.get_type())
print("Edges:", edges)

# criando lista de nodes
nodes = set()

for (a, b) in edges:
    nodes.add(a)
    nodes.add(b)

for n in nodes:
    graph.add_node(pydot.Node(n))

print("Nodes:", nodes)
