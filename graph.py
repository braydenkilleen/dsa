class Node:

    def __init__(self, val):
        self.val

    def __str__(self):
        return f'Node({self.val})'


class Edge:

    def __init__(self, source: Node, destination: Node):
        self.source = source
        self.destination = destination

    def __str__(self):
        return f'{self.source} --> {self.destination}'


class WeightedEdge(Edge):

    def __init__(self, source, destination, weight=1.0):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __str__(self):
        return f'{self.source} --{self.weight}--> {self.destination}'
