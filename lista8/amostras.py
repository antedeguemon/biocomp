import pandas as pd
from kmeans import KMeans

CLUSTERS = 2
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
print means.predictions
means.generate()
print means.predictions
means.generate()
print means.predictions
#print len(amostras[0])
#print len(amostras[1])
"""kmeans.fit(amostras)
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
"""
