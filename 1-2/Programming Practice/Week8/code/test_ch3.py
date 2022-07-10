__author__ = 'alicakmak'
import clusters

blognames, words, data = clusters.readfile('blogdata.txt')
clust=clusters.hcluster(data)
#clusters.printclust(clust,labels=blognames)
clusters.drawdendrogram(clust, labels=blognames, jpeg = 'bclust.jpeg')




















# kclust=clusters.kcluster(data,k=10)
#
# print [blognames[r] for r in kclust[0]]
# print [blognames[r] for r in kclust[1]]



