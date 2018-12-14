require(ape)
require(phytools)
require(geiger)

tr3 = read.tree("./sim.tre")

for (i in 1:100) {
	singlerate = data.frame(fastBM(tr3,sig2=1.0,n=100))
	singlerate = scale(singlerate)
	flnm = paste(toString(i),".phy",sep="")
	write.table(singlerate,row.names=T,col.names=F,sep="\t",quot=F,file=flnm)

}

