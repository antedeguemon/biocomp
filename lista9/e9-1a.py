import pandas as pd
from kmeans import KMeans
from random import randint

CLUSTERS = 2
df=pd.read_csv('../../leukemia_big.csv', sep=',',header=None)
labels = ["ALL", "AML"]
for coisa in range(100):
	resultados = []
	amostras = []
	for amostra in range(72):
		resultados.append(df[amostra][0])
		dados = [float(_) for _ in df[amostra][1:].tolist()]
		amostras.append(dados)

	usos = []
	for _ in range(7129):
		usos.append(bool(randint(0,1)))
	tamanho = sum([int(_) for _ in usos])
	if tamanho < 3572:
		for i in range(7129):
			tamanho = sum([int(_) for _ in usos]) 
			if tamanho <= 3572:
				usos[randint(0,7129)] = True
			else:
				break
	with open("usos.txt", "a") as f:
		f.write(",".join([str(int(_)) for _ in usos])+"\n")
	
	for j in range(len(amostras)):
		amostra = amostras[j]
		for i in range(len(usos)-1):
			if not usos[i]:
				amostras[j][i] = False
		tmp = [a for a in amostras[j] if a is not False]
		amostras[j] = tmp
	print len(amostras[0])
	for test in range(1):
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
			with open("usos.txt", "a") as f:
				a = "Cluster "+str(i)+": "
				b = "  ALL: " + str(float(nclusters[i]["ALL"])) + " - " + str(round((float(nclusters[i]["ALL"])/47), 2)*100) + "%"
				c = "  AML: " + str(float(nclusters[i]["AML"])) + " - " + str(round((float(nclusters[i]["AML"])/25), 2)*100) + "%"
				f.write(a+"\n"+b+"\n"+c+"\n\n")
				print a
				print b
				print c
				
		#means.predictions
		#print len(means.predictions[0])
	
		#print len(means.predictions[1])
