from Entities import *
from enum import Enum


class State(Enum):
    UNVISITED = 1
    VISITED = 2
    VISITING = 3


def search(graph, start, end):
    if start.data == end.data:
        return True
    q = [start]
    for u in graph.get_nodes():
        u.state = State.UNVISITED
    start.state = State.VISITING
    while len(q) > 0:
        u = q.pop(0)
        if u is not None:
            for v in u.outgoing:
                if v.state == State.UNVISITED:
                    if v.data == end.data:
                        return True
                    v.state = State.VISITING
                    q.append(v)
            u.state = State.VISITED
    return False

nodes = [
    GraphNode('A'),
    GraphNode('B'),
    GraphNode('C'),
    GraphNode('D'),
    GraphNode('E'),
    GraphNode('F'),
    GraphNode('G'),
]
nodes[0].outgoing = [nodes[4]]
nodes[1].outgoing = [nodes[0], nodes[4]]
nodes[2].outgoing = [nodes[0]]
nodes[3].outgoing = [nodes[6]]
nodes[4].outgoing = []
nodes[5].outgoing = [nodes[1], nodes[2], nodes[0]]
nodes[6].outgoing = []
g = Graph(nodes)
print(search(g, nodes[5], nodes[4]))
print(search(g, nodes[5], nodes[6]))
