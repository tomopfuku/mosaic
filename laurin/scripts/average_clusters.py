import sys,os
import cluster_reader
import numpy as np
from math import exp
import igraph

# this will read in a cluster from the "*_bestClusters" output by greedo
def read_cluster(line):
    spls = line.strip().split()
    string = spls[1]
    clusters = cluster_reader.read_cluster_string(string)
    aic = float(spls[0])
    clusters.AIC = aic
    return clusters

def calc_weighted_occurrence_matrix(weights):
    for cl in weights:
        nsites = cl.npoints
        break

    mat = np.zeros((nsites,nsites))

    for i in range(nsites):
        for j in range(nsites):
            if i == j:
                mat[i][j] += 1.0
            else:
                for cur1 in weights:
                    if cur1.assign[i] == cur1.assign[j]:
                        mat[i][j] += weights[cur1]
    return mat

def calc_AIC_weights(cl,bestAIC):
    denom=0.
    clweights = {}
    for cur in cl:
        if cur.AIC == bestAIC:
            rellike = 1.
        else:
            rellike = exp(-.5*(bestAIC-cur.AIC))

        clweights[cur] = rellike
        denom+=rellike

    for i in clweights:
        clweights[i] = clweights[i]/denom

    return clweights

def generate_graph(adjMat,cutoff):
    #graph = nx.convert_matrix.from_numpy_matrix(adjMat)
    #nx_agraph.write_dot(graph,"/home/tomo/Dropbox/projects/laurin/best.dot")
    graph = igraph.Graph.Weighted_Adjacency(adjMat.tolist(),mode="lower",loops=False)
    row,col = adjMat.shape
    labs = []
    for i in range(row):
        labs.append(str(i))
    #print labs
    #print graph

    newwgt = []
    for i in graph.es["weight"]:
        if i < cutoff:
            newwgt.append(0.)
        else:
            newwgt.append(i)
    graph.es["weight"] = newwgt
    #print graph.es["weight"]
    graph.vs["name"] = labs
    graph.write_ncol("bestnet.ncol")
    visual_style = {}
    visual_style["edge_width"] = graph.es["weight"]
    visual_style["vertex_label"] = graph.vs["name"]
    layout = "lgl"
    igraph.drawing.plot(graph,"best"+layout+".svg",layout="fr", **visual_style)
    print "wrote the graph of clusterings to the file bestnet.ncol"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "usage: "+sys.argv[0]+" <file with all clusterings and their *IC scores> <weight cutoff for breaking edges>"
        sys.exit(0)

    clfl = open(sys.argv[1],"r")
    cl = []
    bestAIC = 1000000.
    for line in clfl:
        cur = read_cluster(line)
        cl.append(cur)
        if cur.AIC < bestAIC:
            bestAIC = cur.AIC
    
    weights = calc_AIC_weights(cl,bestAIC)

    mat = calc_weighted_occurrence_matrix(weights)
    generate_graph(mat,float(sys.argv[2]))
