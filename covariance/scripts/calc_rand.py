import sys,os
import cluster_reader
from scipy.special import binom
import numpy as np

# this will read in a cluster from the "*_bestClusters" output by greedo
def read_cluster(cluster_file):
    fl = open(cluster_file,"r")
    line = fl.readline()
    spls = line.strip().split()
    string = spls[1]
    clusters = cluster_reader.read_cluster_string(string)
    return clusters

def calc_rand_index(cl1,cl2):
    if cl1.npoints != cl2.npoints:
        print "you are trying to compare clusterings of two datasets of different sizes"
        sys.exit(0)

    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(cl1.npoints):
        for j in range(cl1.npoints):
            if i>=j:
                continue #skip diagonal and redundant half of matrix
            same1 = False
            same2 = False
            if cl1.assign[i] == cl1.assign[j]:
                same1 = True
            if cl2.assign[i] == cl2.assign[j]:
                same2 = True
            if same1 == same2:
                if same1 == True:
                    a+=1
                elif same1 == False:
                    b+=1
            else:
                if same1 == True and same2 == False:
                    c += 1
                if same1 == False and same2 == True:
                    d += 1
    R = float(a+b)/float(a+b+c+d)
    return R


def adj_rand_index(cl1,cl2):
    if cl1.npoints != cl2.npoints:
        print "you are trying to compare clusterings of two datasets of different sizes"
        sys.exit(0)

    xlen = len(cl1.csites)
    ylen = len(cl2.csites)
    mat = np.zeros((xlen,ylen))
    for i in cl1.assign:
        mat[cl1.assign[i]][cl2.assign[i]] += 1.0
    
    rows = 0.0
    for i in range(xlen):
        rows+= binom(sum(mat[i]),2)

    col = 0.0
    for i in range(ylen):
        col+= binom(sum(mat[:,i]),2)

    diag = 0.0 
    for i in range(xlen):
        for j in range(ylen):
            diag+=binom(mat[i][j],2)
    
    nchoose2 = binom(cl1.npoints,2)
    top = (diag-((rows*col)/nchoose2))/(((rows+col)/2.)-((rows*col)/nchoose2))
    return top



if __name__ == "__main__":
    if len(sys.argv) != 4:
        print "usage: "+sys.argv[0]+" <true clustering> <directory with clustering results> <cutoff>"
        sys.exit(0)
    cutoff = float(sys.argv[3])
    trcl = read_cluster(sys.argv[1])
    nclust = str(trcl.K)
    rerun = open(sys.argv[2].replace("/","").replace("out_","")+"_RERUN","w")
    dy = sys.argv[2] + "/" 
    dy_spls = dy.replace("/","").strip().split("_")
    mag = dy_spls[1]
    cov = dy_spls[2]
    for fl in os.listdir(dy):
        if fl.split("_")[-1]== "bestClusters":
            curcl = read_cluster(dy+fl)
            curRand = adj_rand_index(trcl,curcl)
            if curRand < cutoff:
                rerun.write(fl+"\n") 
            else:
                print(nclust+"\t"+str(curcl.K)+"\t"+str(curRand)+"\t"+mag+"\t"+cov)


