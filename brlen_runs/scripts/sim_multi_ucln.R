require(ape)
require(phytools)
require(geiger)
#require(NELSI)
require(plyr)

tr3 = read.tree("./sim.tre")
#tr3 = rescale(tr3, "depth",1.0)
args = commandArgs(trailingOnly=T)
ntraits= as.numeric(args[1])

for (i in 1:100) {
	multitree1 = tr3
        multitree1$edge.length = rlnorm(length(tr3$edge.length),-4,0.5) 	
	mr1 = fastBM(multitree1,sig2=1.0,n=ntraits)
	mr1 = scale(mr1)
	mr1 = data.frame(mr1)
	mr1$rn=row.names(mr1)

	sr = fastBM(tr3,sig2=1.0,n=ntraits)
	sr = scale(sr)
	sr= data.frame(sr)
	sr$rn=row.names(sr)

	multitree2 = tr3 
	multitree2$edge.length = rgamma(length(tr3$edge.length),.5)
	mr2 = fastBM(multitree2,sig2=1.0,n=ntraits)
	mr2 = scale(mr2)
	mr2 = data.frame(mr2)
	mr2$rn=row.names(mr2)
	

	multitree2$edge.length = rexp(length(tr3$edge.length),5)
	mr3 = fastBM(multitree2,sig2=1.0,n=ntraits)
	#mr3=scale(mr3)
	mr3 = data.frame(mr3)
	mr3$rn=row.names(mr3)

	traits=join_all(list(sr,mr1,mr2,mr3),by="rn",type="left")
	row.names(traits) = traits$rn
	traits$rn=NULL
	flnm = paste(toString(i),".phy",sep="")
	write.table(traits,row.names=T,col.names=F,sep="\t",quot=F,file=flnm)

}

