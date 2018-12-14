require(ape)
require(phytools)
require(geiger)

args = commandArgs(trailingOnly=T)

for (i in 1:100) {
	tr3 = read.tree(paste(paste(toString(args[1]),toString(i),sep=""),".tre",sep="")) #single rate tree
	shift_tree = read.tree(paste(paste(toString(args[2]),toString(i),sep=""),".tre",sep=""))
	singlerate = data.frame(fastBM(tr3,sig2=1.0,n=50))
	shift = data.frame(fastBM(shift_tree,sig2=1.0,n=50))
	all = merge(singlerate,shift,by="row.names")
	row.names(all) = all$Row.names
	all = scale(all[2:ncol(all)])
	flnm = paste(toString(i),".phy",sep="")
	write.table(all,row.names=T,col.names=F,sep="\t",quot=F,file=flnm)
}
