import pandas as pd
from kmeans import KMeans

CLUSTERS = 3
df=pd.read_csv('../../leukemia_big.csv', sep=',',header=None)
labels = ["ALL", "AML"]
resultados = []
amostras = []
for amostra in range(72):
	resultados.append(df[amostra][0])
	amostras.append([float(_) for _ in df[amostra][1:].tolist()])

means = KMeans(CLUSTERS)
for amostra in amostras:
	#print "amostra adicionada"
	means.add_point(amostra)
means.generate_first()
for i in range(10):
	means.generate()
print means.predictions
