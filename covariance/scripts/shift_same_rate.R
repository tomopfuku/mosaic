require(ape)
require(phytools)
require(geiger)

args = commandArgs(trailingOnly=T)

for (i in 1:100) {
	tr3 = read.tree(paste(paste(toString(args[1]),toString(i),sep=""),".tre",sep="")) #single rate tree
	shift_tree = read.tree(paste(paste(toString(args[2]),toString(i),sep=""),".tre",sep=""))
	corr = as.numeric(args[3])
	mat_size = 25 # this refers to the size of covarying blocks, not the matrices as a whole
	vcv = matrix(corr,mat_size,mat_size)
	diag(vcv)<-1.0
	Q<-matrix(c(-0.00001,0.00001,0.00001,-0.00001),2,2) #This maps regimes to tree, allowing covariance strength to vary across the tree. It is set to keep covariance uniform across tree NOTE: got this from revell's blog. thanks!
	tre<-sim.history(tr3,Q)
	singlerate = sim.corrs(tre,vcv)
	singlerate = cbind(singlerate,sim.corrs(tre,vcv))
	singlerate = data.frame(singlerate)
	tre<-sim.history(shift_tree,Q)
	shift = sim.corrs(tre,vcv)
	shift = cbind(shift,sim.corrs(tre,vcv))
	shift = data.frame(shift)
	all = merge(singlerate,shift,by="row.names")
	row.names(all) = all$Row.names
	all = scale(all[2:ncol(all)])
	flnm = paste(toString(i),".phy",sep="")
	write.table(all,row.names=T,col.names=F,sep="\t",quot=F,file=flnm)
}
