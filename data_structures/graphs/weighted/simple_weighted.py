class WeightedGraph:
    def __init__(self):
        self.graph = {}

    def add_node(self,node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self,node1,node2,weight):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append((node2, weight))
            self.graph[node2].append((node1, weight))
        else:
            print("Node not found")

    def print_graph(self):
        for node,edges in self.graph.items():
            print(f"{node}: {edges}")

    def remove_edge(self, node01,node02):
        if node01 in self.graph and node02 in self.graph:
            self.graph[node01] = [edge for edge in self.graph[node01] if edge[0] != node02]
            self.graph[node02] = [edge for edge in self.graph[node02] if edge[0] != node01]
        else:
            print("Node not found")

    def remove_node(self,node):
        if node in self.graph:
            del self.graph[node]
            for edges in self.graph.values():
                edges[:] = [edge for edge in edges if edge[0] != node]
        else:
            print("Node not found")

        
if __name__ == "__main__":
    graph = WeightedGraph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_edge("A","B",10)
    print(graph.graph)
    