from collections import deque

def bfs(adj_list, start):
    """Executa BFS e retorna ordem de visita."""
    visitados = set()
    fila = deque([start])
    ordem = []

    while fila:
        no = fila.popleft()
        if no not in visitados:
            visitados.add(no)
            ordem.append(no)
            for vizinho in adj_list[no]:
                if vizinho not in visitados:
                    fila.append(vizinho)
    return ordem

def dfs(adj_list, start):
    """Executa DFS recursiva e retorna ordem de visita."""
    visitados = set()
    ordem = []

    def _dfs(no):
        if no in visitados:
            return
        visitados.add(no)
        ordem.append(no)
        for vizinho in adj_list[no]:
            _dfs(vizinho)

    _dfs(start)
    return ordem
