require(ape)
require(phytools)
require(geiger)
require(NELSI)

tr3 = read.tree("./sim.tre")

for (i in 1:100) {
	#uncor <- simulate.uncor.lnorm(tr3, params = list(mean.log = -3.9, sd.log = 0.7))
	#multitree1 = uncor$phylogram
	#multitree1 = rescale(multitree1, "depth",10.0)
	multitree1 = tr3 
	multitree1$edge.length = rgamma(length(tr3$edge.length),.5)
	multirate1 = fastBM(multitree1,sig2=1.0,n=10)
	singlerate = fastBM(tr3,sig2=1.0,n=10)
	multiall = merge(multirate1,singlerate,by="row.names")
	row.names(multiall) = multiall$Row.names
	multiall = scale(multiall[,2:ncol(multiall)])
	flnm = paste(toString(i),".phy",sep="")
	write.table(multiall,row.names=T,col.names=F,sep="\t",quot=F,file=flnm)

}

