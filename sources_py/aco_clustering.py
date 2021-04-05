from undirected_graph import UndirectedGraph
from cluster import Cluster
from random import randint
from random import uniform

def aco_sol_cluster(graph: UndirectedGraph, cluster_count: int):
    matr = {}
    for node in graph.nodes():
        matr[node] = {}
        for cluster in range(1, cluster_count+1):
            matr[node][cluster] = 100

    for iteration in range(1000):
        print('Iteration ' + str(iteration))

        solution = {}
        for node in graph.nodes():
            total = sum(matr[node].values())
            choise = uniform(0, total-1)
            cluster = 1
            while matr[node][cluster] < choise:
                choise -= matr[node][cluster]
                cluster += 1
            solution[node] = cluster

        clusters = {}
        for c in range(1, cluster_count+1):
            clusters[c] = Cluster(graph, [])

        for node in solution.keys():
            clusters[solution[node]].add(node)

        mod_dens = 0
        for cluster in clusters.values():
            mod_dens += cluster.modularity_density()

        for node in solution.keys():
            cl = solution[node]
            matr[node][cl] += (mod_dens + clusters[cl].modularity_density() / 5) /5
            if matr[node][cl] == 0:
                matr[node][cl] = 0

    cluster_list = []
    for c in range(1, cluster_count+1):
        clust = Cluster(graph, [])
        for node in graph.nodes():
            if max(matr[node].values()) == matr[node][c]:
                clust.add(node)
        cluster_list.append(clust)

    print('      ', end='')
    for node in graph.nodes():
        print(node, '     ', end='')
    print('')
    for c in range(1, cluster_count+1):
        print(c, '  ', end='')
        for node in graph.nodes():
            print("%.2f" % matr[node][c], ' ', end='')
        print('')

    return cluster_list

def aco_graph_cluster(graph: UndirectedGraph):
    edges = {}
    steps = 0
    for node in graph.nodes():
        for neigh in graph.neighbors(node):
            edges[(node, neigh)] = 10
            edges[(neigh, node)] = 10
            steps += 1
    steps = int(0.1 * steps / 100) + 1
    nodes = [node for node in graph.nodes()]

    for iteration in range(1000):
        print('Iteration ' + str(iteration))

        for i in range(len(nodes)):
            ant = nodes[randint(0, len(nodes)-1)]
            # print('Node ' + str(nodes[i]))
            # ant = nodes[i]
            for step in range(steps):
                next_nodes = graph.neighbors(ant)
                if len(next_nodes) == 0:
                    continue
                # print(next_nodes)
                prob = [edges[(ant, n)] for n in next_nodes]
                # print('prob:',prob)
                total = sum(prob)
                prob = [p / total for p in prob]
                direction = uniform(0, 1)
                while direction > prob[0]:
                    direction -= prob[0]
                    next_nodes = next_nodes[1:]
                    prob = prob[1:]
                next_node = next_nodes[0]
                # print('next_node ', next_node)
                edges[(next_node, ant)] += 0.1
                edges[(ant, next_node)] += 0.1
                ant = next_node

    suma = 0
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            if (nodes[i], nodes[j]) in edges:
                print(str(nodes[i]) + ',' + str(nodes[j]) + ' : ' + str(edges[(nodes[i], nodes[j])]))
                suma += edges[(nodes[i], nodes[j])]
    suma = 2 * suma / len(edges)
    print(suma)

    cluster_list = []
    while len(nodes) != 0:
        node = nodes.pop()
        clust = Cluster(graph, [node])
        vecini = []
        for neigh in graph.neighbors(node):
            if (node, neigh) in edges and edges[(node, neigh)] > 0.9 * suma:
                vecini.append(neigh)
                clust.add(neigh)
                if neigh in nodes:
                    nodes.remove(neigh)
                del edges[(node, neigh)]
                del edges[(neigh, node)]
        while len(vecini) != 0:
            n = vecini.pop()
            for neigh in graph.neighbors(n):
                if (n, neigh) in edges and edges[(n, neigh)] > 0.9 * suma and neigh not in clust:
                    vecini.append(neigh)
                    clust.add(neigh)
                    if neigh in nodes:
                        nodes.remove(neigh)
                    del edges[(n, neigh)]
                    del edges[(neigh, n)]
        cluster_list.append(clust)

    return cluster_list
