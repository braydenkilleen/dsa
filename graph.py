"""Object-Oriented graph implementation"""


class Node:

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return f'Node({self.val})'


class Edge:

    def __init__(self, source: Node, destination: Node) -> None:
        self.source = source
        self.destination = destination

    def __str__(self) -> None:
        return f'{self.source} --> {self.destination}'


class WeightedEdge(Edge):

    def __init__(self, source, destination, weight=1.0):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __str__(self):
        return f'{self.source} --{self.weight}--> {self.destination}'


class DirectedGraph():

    def __init__(self):
        self.nodes = []
        self.edges = {}

    def add_node(self, node):
        if node in self.ndoes:
            raise ValueError('Node already exists')
        self.nodes.append(node)
        self.edges[node] = []

    def add_edge(self, edge):
        pass
