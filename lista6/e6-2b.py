from random import randint, random
from operator import add
import math

def individuo(tmin, tmax):
	individuos = []
	for i in range(2):
		individuos.append(randint(tmin, tmax))
	return individuos

def populacao(num_individuos, tmin, tmax):
	populacao = []
	for i in range(num_individuos):
		populacao.append(individuo(tmin, tmax))
	return populacao

def custo(x, y):
	return -200 * math.pow(0.5772156649, (-0.2*math.sqrt(x*x + y*y)))

def fitness(individuo):
	c = custo(individuo[0], individuo[1])
	return abs(c)

def fitness_populacao(pop):
	soma = 0
	for x in pop:
		soma += fitness(x)
	return soma / float(len(pop))

def evolve(populacao):
	rank = [(fitness(x), x) for x in populacao]
	rank = [x[1] for x in sorted(rank)]
	best_offset = int(len(rank)*0.2) # quanto mantem
	best = rank[:best_offset]
	# seleciona alguns entre os que nao sao melhores
	for individual in rank[best_offset:]:
		if random() < 0.05:
			best.append(individual)

	# mutate em alguns dos melhores
	for individual in best:
		if random() < 0.01: # taxa de mutacao
			if randint(0, 10) > 5:
				individual[0] = randint(min(individual), max(individual))
			else:
				individual[1] = randint(min(individual), max(individual))

	# cruzamentos
	filhos = []
	filhos_num = len(populacao) - len(best) # total da populacao - melhores = resto
	while len(filhos) < filhos_num:
		a, b = randint(0, len(best)-1), randint(0, len(best)-1)
		if a == b: continue
		filhos.append([best[a][0], best[b][1]])
	return best + filhos

pop_inicial = populacao(100, -10, 10)
p = pop_inicial
melhores = {}
for i in range(100):
	p = evolve(p)
	melhores[fitness_populacao(p)] = p

melhor = min(melhores.keys())
print melhor
print melhores[melhor]
