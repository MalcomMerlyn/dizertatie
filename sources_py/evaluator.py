import os


class Evaluator:
    def __init__(self, path_in: str, path_out: str):
        group_edges_file = open(os.path.join(path_in, 'group-edges.csv'), 'r')

        self.__result = {}
        line = group_edges_file.readline()
        while line != '':
            pair = line.strip().split(',')
            node = int(pair[0])
            cluster = int(pair[1])
            self.__result[node] = cluster
            line = group_edges_file.readline()

        group_edges_file.close()
        print(self.__result)

        group_edges_file = open(os.path.join(path_out, 'group-edges.csv'), 'r')

        self.__ground_truth = {}
        line = group_edges_file.readline()
        while line != '':
            pair = line.strip().split(',')
            node = int(pair[0])
            cluster = int(pair[1])
            self.__ground_truth[node] = cluster
            line = group_edges_file.readline()

        group_edges_file.close()
        print(self.__ground_truth)

    def evaluate(self):
        correct_pairs = 0
        all_pairs = len(self.__result.keys())
        all_pairs = all_pairs * (all_pairs - 1)
        for node1 in self.__result.keys():
            for node2 in self.__result.keys():
                same_res = self.__result[node1] == self.__result[node2]
                same_gt = self.__ground_truth[node1] == self.__ground_truth[node2]
                if same_res == same_gt:
                    correct_pairs += 1
        return correct_pairs / all_pairs


DATASET = 'simple_dataset'
OUTSET = DATASET + '_out'

if __name__ == '__main__':
    evaluator = Evaluator(DATASET, OUTSET)
    print('Accuracy ', evaluator.evaluate())
