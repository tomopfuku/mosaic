import sys,os
import cluster_reader
from calc_rand import *

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "usage: "+sys.argv[0]+" <true clustering> <directory with clustering results>"
        sys.exit(0)

    trcl = read_cluster(sys.argv[1])
    
    fl = sys.argv[2]
    curcl = read_cluster(fl)
    #curRand = calc_rand_index(trcl,curcl)
    curRand = adj_rand_index(trcl,curcl)
    print curRand            
