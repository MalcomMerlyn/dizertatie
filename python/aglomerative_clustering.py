from undirected_graph import UndirectedGraph
from cluster import Cluster


def cluster(graph: UndirectedGraph):
    cluster_list = [Cluster(graph, [x]) for x in graph.nodes()]
    mod = sum([c.modularity_density() for c in cluster_list])
    while len(cluster_list) != 1:
        print('Iteration ' + str(len(cluster_list)))

        min_dist = 100000000
        left = None
        right = None

        for c1 in range(len(cluster_list)):
            for c2 in range(c1+1, len(cluster_list)):
                if Cluster.neighbour(cluster_list[c1], cluster_list[c2]):
                    dist = Cluster.distance(cluster_list[c1], cluster_list[c2])
                    if min_dist > dist:
                        left = cluster_list[c1]
                        right = cluster_list[c2]
                        min_dist = dist

        new_cluster = Cluster.merge(left, right)
        mod_dens = new_cluster.modularity_density() - left.modularity_density() - right.modularity_density()
        if mod_dens < 0:
            break

        cluster_list.remove(left)
        cluster_list.remove(right)
        cluster_list.append(new_cluster)

        mod += mod_dens
        print('Density ' + str(mod))

        print(cluster_list)
    return cluster_list
