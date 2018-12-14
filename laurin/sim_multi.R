require(ape)
require(phytools)
require(geiger)

tr3 = read.tree("./sim.tre")

for (i in 1:100) {
	random_node = sample.int(length(tr3$edge.length),1)
	multitree1=rescale(tr3,"lrate",rate=c(8.0,.5),node=random_node)
	random_node = sample.int(length(tr3$edge.length),1)
	multitree2=rescale(tr3,"lrate",rate=c(8.0,.5),node=random_node)
	multirate1 = fastBM(multitree1,sig2=1.0,n=50)
	multirate2 = fastBM(multitree2,sig2=1.0,n=50)
	multiall = merge(multirate1,multirate2,by="row.names")
	row.names(multiall) = multiall$Row.names
	singlerate = fastBM(tr3,sig2=1.0,n=50)
	traits = merge(multiall[2:ncol(multiall)],singlerate,by="row.names")
	flnm = paste(toString(i),".phy",sep="")
	write.table(traits,row.names=F,col.names=F,sep="\t",quot=F,file=flnm)
}

