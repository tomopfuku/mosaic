require(mclust)
correct_clust=c(rep(1,50),rep(2,50))
num_cat=2
#correct_clust=c(rep(1,50),rep(2,50),rep(3,50))
#correct_clust=c(rep(1,50),rep(2,50),rep(3,50),rep(4,50))
ari=c()
recon_cat=c()
for (cur in list.files(dir)) {
    tab=read.table(paste(dir,cur,sep="/"),skip=1,row.names=1)
    fit=densityMclust(t(tab))
    ari=c(ari,adjustedRandIndex(fit$classification,correct_clust))
    recon_cat=c(recon_cat,fit$G)
}
num_cat=rep(num_cat,100)
#mag=rep("64x",fit$n)
#cov=rep("0.1",fit$n)
#res=data.frame(num_cat,recon_cat,ari,mag,cov)
res=data.frame(num_cat,recon_cat,ari)
