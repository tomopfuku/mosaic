import sys,os

DIR = sys.argv[1]
for i in os.listdir(DIR):
    spls = i.strip().split("_")
    if spls[0] == "8x":
        outnm = "_".join(spls[3:])
        outfl = open(DIR+outnm,"w")
        for line in open(DIR+i):
            outfl.write(line.strip()+"\n")
