from undirected_graph import UndirectedGraph


class Cluster:
    def __init__(self, graph: UndirectedGraph, nodes: list):
        self.__graph = graph
        self.__nodes = nodes
        self.__node_set = set(nodes)
        self.__score = 0

    def score_func(self):
        ms = 0
        cs = 0
        for node in self.__nodes:
            for neigh in self.__graph.neighbors(node):
                if neigh in self.__node_set:
                    ms += 1
                else:
                    cs += 1
        if cs == 0 and ms == 0:
            return -1
        return cs / (2 * ms + cs)

    def __contains__(self, node):
        return node in self.__node_set

    def __str__(self):
        return self.__nodes.__str__()

    def __repr__(self):
        return self.__str__()

    def modularity_density(self):
        ms = 0
        cs = 0
        node_cnt = len(self.__nodes)
        if node_cnt == 0:
            return -2

        for node in self.__nodes:
            for neigh in self.__graph.neighbors(node):
                if neigh in self.__node_set:
                    ms += 1
                else:
                    cs += 1
        return (2 * ms - cs) / node_cnt

    def nodes(self):
        return self.__nodes

    def score(self):
        self.__score = self.__score_func()
        return self.__score

    def add(self, element):
        if element not in self.__node_set:
            self.__nodes.append(element)
            self.__node_set = self.__node_set.union(set([element]))

    @staticmethod
    def merge(left, right):
        nodes = right.__nodes + left.__nodes
        return Cluster(left.__graph, nodes)

    @staticmethod
    def neighbour(left, right):
        for node in left.__nodes:
            for neigh in left.__graph.neighbors(node):
                if neigh in right:
                    return True
        return False

    @staticmethod
    def distance(left, right):
        return Cluster.merge(left, right).score()
