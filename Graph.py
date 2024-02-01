import json

class Node:
    def __init__(self, id, name=None, color=None, label=None, title=None, shape=None, image=None, size=None, cost=None):
        self.id = id
        self.name = name
        self.color = color
        self.label = label
        self.title = title
        self.shape = shape
        self.image = image
        self.size = size
        self.cost = cost

    def to_dic(self):
        return {
            "id": self.id,
            "name": self.name,
            "color": self.color,
            "label": self.label,
            "title": self.title,
            "shape": self.shape,
            "image": self.image,
            "size": self.size,
            "cost": self.cost
        }


class Edge:
    def __init__(self, from_node, to_node, color=None, id=None):
        self.from_node = from_node
        self.to_node = to_node
        self.color = color
        self.id = id

    def to_dic(self):
        return {
            "from": self.from_node.id,
            "to": self.to_node.id,
            "color": self.color,
            "id": self.id
        }
class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, edge):
        self.edges.append(edge)

    def get_node(self, id):
        for node in self.nodes:
            if node.id == id:
                return node

    def to_dic(self):
        res = dict()
        res["nodes"] = [i.to_dic() for i in self.nodes]
        res["edges"] = [i.to_dic() for i in self.edges]
        return res


# Example Usage:
if __name__ == "__main__":

    graph = Graph()
    node1 = Node(id="a")
    node2 = Node(id="b")
    graph.add_node(node1)
    graph.add_node(node2)


    edge1 = Edge(node1,node2)
    graph.add_edge(edge1)


    # Print nodes and edges
    print(graph.to_dic())