import os


class DatasetParser:
    def __init__(self, path: str):
        self.path = path
        nodes_file = open(os.path.join(self.path, 'nodes.csv'), 'r')
        edges_file = open(os.path.join(self.path, 'edges.csv'), 'r')
        groups_file = open(os.path.join(self.path, 'groups.csv'), 'r')

        line = nodes_file.readline()
        while line != '':
            self.__nodes_count = int(line.strip())
            line = nodes_file.readline()

        self.__edges_list = []
        line = edges_file.readline()
        while line != '':
            node1, node2 = line.strip().split(',')
            self.__edges_list.append((int(node1), int(node2)))
            self.__edges_list.append((int(node2), int(node1)))
            line = edges_file.readline()

        self.__cluster_count = 0
        line = groups_file.readline()
        while line != '':
            group = int(line.strip())
            if self.__cluster_count < group:
                self.__cluster_count = group
            line = groups_file.readline()

        nodes_file.close()
        edges_file.close()
        groups_file.close()

    def nodes_count(self):
        return self.__nodes_count

    def edges_list(self):
        return self.__edges_list

    def cluster_count(self):
        return self.__cluster_count

def write_output(path: str, groups: str):
    groups_file = open(os.path.join(path, 'groups.csv'), 'w+')
    group_edges_file = open(os.path.join(path, 'group-edges.csv'), 'w+')

    for group in range(0, len(groups)):
        groups_file.write(str(group+1) + '\n')
        for element in groups[group].nodes():
            group_edges_file.write(str(element) + ',' + str(group+1) + '\n')

    groups_file.close()
    group_edges_file.close()
