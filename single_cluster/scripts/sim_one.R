require(ape)
require(phytools)
require(geiger)

args = commandArgs(trailingOnly=T)

for (i in 1:100) {
	tr3 = read.tree(paste(paste(toString(args[1]),toString(i),sep=""),".tre",sep="")) #single rate tree
	singlerate = data.frame(fastBM(tr3,sig2=1.0,n=100))
	singlerate = scale(singlerate)
	flnm = paste(toString(i),".phy",sep="")
	write.table(singlerate,row.names=T,col.names=F,sep="\t",quot=F,file=flnm)
}

