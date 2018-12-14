import sys

if len(sys.argv) != 3:
    print "usage: "+sys.argv[1]+" <number of sites> <number of partitions>"
    sys.exit(0)

nsites = int(sys.argv[1])
npart = int(sys.argv[2])


period = nsites/npart
curpart =0 
clstring = ""
for i in range(nsites):
    if curpart == 0:
        clstring+="("
    curpart+=1
    if curpart == period:
        clstring+=str(i)
        clstring += ")"
        curpart = 0
    else:
        clstring+=str(i)+","        

print clstring