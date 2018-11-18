import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
CLUSTERS = 2
df=pd.read_csv('leukemia_big.csv', sep=',',header=None)
#amostras = np.array([df[0][0:]])
labels = ["ALL", "AML"]
resultados = []
amostras = []
for amostra in range(72):
	#print df[amostra][0]
	#amostras.append([0])
	resultados.append(df[amostra][0])
	amostras.append(df[amostra][1:].tolist())
#print len(amostras[1])
kmeans = KMeans(n_clusters=CLUSTERS)
kmeans.fit(amostras)
acertos = 0
for i in range(72):
	amostra = np.array(amostras[i]).reshape(1, -1)
	print amostra[0]
	#data = np.array(amostras[i])
	print "Amostra " + str(i)
	print "Esperado: " + resultados[i]
	print "Obtido: " + kmeans.predict(amostra)
	print ""
print acertos/float(72)
	
