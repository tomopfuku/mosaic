import os,sys

if len(sys.argv) != 4:
    print "usage: " +sys.argv[0]+ " <folder with matrices> <out directory <ntraits>"
    sys.exit(0)

INDIR = sys.argv[1]+"/"
DIR = sys.argv[2]+"/"
ntrait = str(sys.argv[3])
for fl in os.listdir(INDIR):
    spls = fl.strip().split(".")
    if spls[-1] != "phy":
        continue
    cur = open(fl,"r")
    out = open(DIR+fl,"w")
    out.write("100\t"+ntrait+"\n")
    for line in cur:
        out.write(line)
    cur.close()
    out.close()

