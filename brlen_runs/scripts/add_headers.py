import os,sys



directory = sys.argv[1]+"/"
for fl in os.listdir(directory):
    cur = open(directory + fl,"r")
    out = open("HEAD_"+directory+fl,"w")
    out.write("20\t150\n")
    for line in cur:
        out.write(line)
    cur.close()
    out.close()

