import sys

class Clustering:
    def __init__(self):
        self.assign = {}
        self.npoints = 0        
        self.K = 0    
        self.csites = {}

def read_cluster_string(clstring):
    #clusters = {}
    clusters = Clustering()
    curlab = 0
    for char in clstring:
        if char == "(":
            cursite = ""
            clusters.csites[curlab] = {}
        elif char == ",":
            conv = int(cursite)
            clusters.assign[conv] = curlab 
            clusters.csites[curlab][conv] = True
            cursite = ""
        elif char == ")":
            conv = int(cursite)
            clusters.assign[conv] = curlab 
            curlab+=1          
            #clusters.csites[curlab] = {} 
        else:
            cursite+=char
    clusters.npoints = len(clusters.assign)
    clusters.K = curlab
    return clusters
