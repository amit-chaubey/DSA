class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:
            self.add_node(node2)

        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def remove_node(self, node):
        if node in self.graph:
            del self.graph[node]
            for edges in self.graph.values():
                if node in edges:
                    edges.remove(node)

    def remove_edge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].remove(node2)
            self.graph[node2].remove(node1)
 
    def print_graph(self):
        for node in self.graph:
            print(f"{node}--->{self.graph[node]}")



if __name__=="__main__":
    graph = Graph()
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.print_graph()