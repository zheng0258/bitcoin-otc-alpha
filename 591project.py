import igraph as ig

bitcoin_alpha = ig.Graph.Read_Ncol('soc-sign-bitcoinalpha.csv', directed = False) 
bitcoin_otc = ig.Graph.Read_Ncol('soc-sign-bitcoinotc.csv', directed = False) 



#Louvain Algorithm
alpha_clusters = bitcoin_alpha.community_multilevel()
otc_clusters = bitcoin_otc.community_multilevel()

alpha_modularity = bitcoin_alpha.modularity(alpha_clusters)
otc_modularity = bitcoin_otc.modularity(otc_clusters)

print("Louvain: alpha - modularity score", alpha_modularity)
print("Louvain: otc - modularity score", otc_modularity)


#Label Propagation Algorithm
alpha_clusters = bitcoin_alpha.community_label_propagation()
otc_clusters = bitcoin_otc.community_label_propagation()

alpha_modularity = bitcoin_alpha.modularity(alpha_clusters)
otc_modularity = bitcoin_otc.modularity(otc_clusters)
print("Label Propagation: alpha - modularity score", alpha_modularity)
print("Label Propagation: otc - modularity score", otc_modularity)

#Leiden Algorithm
alpha_clusters = bitcoin_alpha.community_leiden()
otc_clusters = bitcoin_otc.community_leiden()

alpha_modularity = bitcoin_alpha.modularity(alpha_clusters)
otc_modularity = bitcoin_otc.modularity(otc_clusters)

print("Leiden: alpha - modularity score", alpha_modularity)
print("Leiden: otc - modularity score", otc_modularity)

#Infomap Algorithm
alpha_clusters = bitcoin_alpha.community_infomap()
otc_clusters = bitcoin_otc.community_infomap()

alpha_modularity = bitcoin_alpha.modularity(alpha_clusters)
otc_modularity = bitcoin_otc.modularity(otc_clusters)

print("Infomap: alpha - modularity score", alpha_modularity)
print("Infomap: otc - modularity score", otc_modularity)




