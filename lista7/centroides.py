import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
CLUSTERS = 3
df=pd.read_csv('leukemia_big.csv', sep=',',header=None)
amostras = []
for amostra in range(72):
	amostras.append(df[amostra][1:].tolist())
kmeans = KMeans(n_clusters=CLUSTERS)
kmeans.fit(amostras)
for _ in range(len(kmeans.cluster_centers_)):
    print "Centroide " + str(_)
    for __ in kmeans.cluster_centers_[_]:
        print __
    print ""
