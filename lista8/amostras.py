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
for test in range(10):
	print "Round " + str(test)
	means = KMeans(CLUSTERS)
	for amostra in amostras:
		means.add_point(amostra)
	means.generate_first()
	for i in range(10):
		means.generate()

	nclusters = {}
	for cluster in range(CLUSTERS):
		nclusters[cluster] = {"ALL": 0, "AML": 0}

	for i in range(72):
		#print resultados[i]
		for cluster in range(CLUSTERS):
			if i in means.predictions[cluster]:
				nclusters[cluster][resultados[i]] += 1

	for i in nclusters:
		print "Cluster "+str(i)+": "
		print "  ALL: " + str(float(nclusters[i]["ALL"])) + " - " + str(round((float(nclusters[i]["ALL"])/47), 2)*100) + "%"
		print "  AML: " + str(float(nclusters[i]["AML"])) + " - " + str(round((float(nclusters[i]["AML"])/25), 2)*100) + "%"
	#means.predictions
	#print len(means.predictions[0])

	#print len(means.predictions[1])
