require(phytools)
require(geiger)

for (i in 1:100) {
	cur = unroot(pbtree(1,0,100))
	cur$edge.length = rep(0.25,length(cur$edge.length))
	cur = rescale(cur,"depth",1.0)
	outfl = paste(toString(i),".tre",sep="")
	write.tree(cur,outfl)
}
