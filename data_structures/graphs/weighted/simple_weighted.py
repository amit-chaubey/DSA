class WeightedGraph:
    def __init__(self):
        self.graph = {}

    def add_node(self,node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self,node1,node2,weight):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2, weight)
            self.graph[node2].append(node1,weight)
        else:
            print("Node not found")

if __name__ == "__main__":
    graph = WeightedGraph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_edge("A","B",10)
    print(graph.graph)
    