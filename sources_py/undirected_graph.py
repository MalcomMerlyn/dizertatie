

class UndirectedGraph:
    def __init__(self):
        self.__graph = {}
        self.__node_count = 0

    def __init__(self, node_count: int, edges: list):
        self.__graph = {}
        self.__node_count = node_count
        for i in range(1, node_count+1):
            self.__graph[i] = []
        for i,j in edges:
            self.__graph[i].append(j)
            #self.__graph[j].append(i)

    def node_count(self):
        """
        Returns the number of nodes (int)
        """
        return self.__node_count

    def nodes(self):
        """
        Returns all the nodes in the graph
        Returns a list of node ids.
        """
        return self.__graph.keys()

    def neighbors(self, node):
        """
        Find all the nodes where there is an edge from the specified node to that node.
        Returns a list of node ids.
        """
        return self.__graph[node]
