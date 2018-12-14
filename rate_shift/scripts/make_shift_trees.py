import sys,os
import random
from mandos import *

if len(sys.argv) != 3:
    print("usage: " +sys.argv[0] + " <original_tree_directory> <rate_shift_magnitude>")
    sys.exit(0)

DIR = sys.argv[1]+"/"
shift_multiplier = float(sys.argv[2])

for fl in os.listdir(DIR):
    tree = tree_utils2.read_tree(DIR+fl)
    shift_cand = []
    for node in tree.iternodes(1):
        if node.isroot:
            continue
        if node.istip == False:
            descend = len(node.leaves())
            if descend >= 10 and descend < 90:
                shift_cand.append(node)
    shiftnode = random.choice(shift_cand) # make random clade shift
    for node in shiftnode.iternodes():
        node.length = node.length * shift_multiplier
    outfl = open(sys.argv[2]+"x_shift_trees/"+fl, "w")
    #print(sys.argv[2]+"x_shift_trees/"+fl)
    outfl.write(tree.get_newick_repr(True)+";\n")
    outfl.close()

