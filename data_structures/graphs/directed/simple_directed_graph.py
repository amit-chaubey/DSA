class DirectedGraph:
    def __init__(self):
        self.graph = {}
    
    def add_node(self,node):
        if node not in self.graph or node not in self.graph.values():
            self.graph[node] = []

    def add_edge(self,node1,node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)
        else:
            print("Node not found)")

    def remove_node(self,node):
        if node in self.graph:
            del self.graph[node]
            for edges in self.graph.values():
                if node in edges:
                    edges.remove(node)

    def remove_edge(self,node1,node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].remove(node2)

    def print_graph(self):
        for node in self.graph:
            print(f"{node}-->{self.graph[node]}")
            

if __name__=="__main__":
    graph = DirectedGraph()
    graph.add_edge("A","B")
    graph.add_edge("A","C")
    graph.add_edge("B","C")
    graph.add_edge("C","D")
    graph.print_graph()
    graph.remove_node("A")
    graph.print_graph()
    graph.remove_edge("B","C")
    graph.print_graph() 