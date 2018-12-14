import sys,os

if len(sys.argv)!=3:
    print("usage: "+sys.argv[0]+" <trait_directory> <tree_directory>")
    sys.exit(0)

TREEDIR = sys.argv[2]+"/"
TRAITDIR = sys.argv[1]+"/"
for rep in range(1,101):
    fl_ind = str(rep)
    treefl = TREEDIR+fl_ind+".tre"
    traitfl = TRAITDIR+fl_ind+".phy"
    mag = TRAITDIR.strip().split("_")[0]
    cmd = "greedo -a 10 -K 50 -t "+treefl+" -m "+traitfl+" -f 3 -c 0 -split 10 -gen 10 -o out_"+ mag + "/" + fl_ind
    print(cmd)
    os.system(cmd)
