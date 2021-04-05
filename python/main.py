from undirected_graph import UndirectedGraph
from evaluator import Evaluator
from dataset_handler import *
import aglomerative_clustering
import aco_clustering

DATASET = 'simple_dataset'
OUTSET = DATASET + '_out'

if __name__ == '__main__':
    dataset = DatasetParser(DATASET)
    graph = UndirectedGraph(dataset.nodes_count(), dataset.edges_list())
    clusters = aco_clustering.aco_sol_cluster(graph, dataset.cluster_count())
    # clusters = aglomerative_clustering.cluster(graph)
    print(clusters)
    write_output(OUTSET, clusters)
    evaluator = Evaluator(DATASET, OUTSET)
    print('Accuracy ', evaluator.evaluate())
