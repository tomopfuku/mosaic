import sys,os


if len(sys.argv)!=4:
    print "usage: "+sys.argv[0]+" <directory> <alpha parameter> <max # clusters>"
    sys.exit(0)

directory = sys.argv[1]+"/"
for fl in os.listdir(directory):
    cmd = "greedo -t sim.ur.tre -m " + directory+fl+" -f 3 -c 0 -split 10 -gen 100 -o "+directory.replace("/","").replace("HEAD_","")+"_"+fl.replace(".phy","")
    cmd += " -a "+sys.argv[2]
    cmd += " -K "+sys.argv[3]
    print cmd
    os.system(cmd)
