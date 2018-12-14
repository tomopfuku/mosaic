import sys,os
import cluster_reader
from calc_rand import *
from scipy.special import binom
import numpy as np
import glob

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("usage: "+sys.argv[0]+" <true clustering> <directory with clustering results> <cutoff>")
        sys.exit(0)
    cutoff = float(sys.argv[3])
    trcl = read_cluster(sys.argv[1])
    nclust = str(trcl.K)
    rerun = open(sys.argv[2].replace("/","").replace("out_","")+"_RERUN","w")
    DIR = sys.argv[2] + "/" 
    
    outfl = open(DIR.replace("/","")+".RI","w")
    for rep in range(100):
        if rep == 0:
            continue
        wild = DIR+"*_"+str(rep)+"*_bestClusters"
        cur = glob.glob(wild)       
        best = -1000000000
        bestK = 0
        for fl in cur: 
            curcl = read_cluster(fl)
            curRand = adj_rand_index(trcl,curcl)
            if float(curRand) > best:
                best = curRand
                bestK = curcl.K
        if best < cutoff:
            rerun.write(fl+"\n") 
        else:
            print(nclust+"\t"+str(bestK)+"\t"+str(best))

