import networkx as nx

class GraphTraversal:
    """
    This class has purpose of search in breadth first manner.
    """
    def __init__(self, G):
        """
        If G is graph object, it's read directly, or if it's a text file
        it converts it into a graph object.
        :param G: Can be a graph object or a text file.
        :return:
        """
        if isinstance(G, nx.Graph):
            self.G = G
        else:
            self.G = self._make_graph_from_text(G)


    def Breadth_first_traversal(self):
        pass

    def Depth_first_traversal(self):
        pass

    @staticmethod
    def _make_graph_from_text(textFile):
        file = open(textFile)
        nodes = eval(file.readline())
        edges = eval(file.readline())
        file.close()
        G = nx.Graph()
        G.add_nodes_from(nodes)
        G.add_edges_from(edges)
        return G.number_of_edges()

if __name__ == "__main__":
    ob = GraphTraversal('sampleGraph.txt')





