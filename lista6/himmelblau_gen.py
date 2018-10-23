from random import randint, random
from operator import add

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
    a = x*x + y - 11
    b = x + y*y - 7
    return a*a + b*b

def fitness(individuo):
	c = custo(individuo[0], individuo[1])
	return abs(c)

def grade(pop):
	soma = 0
	for x in pop:
		soma += fitness(x)
	return soma / float(len(pop))

def evolve(pop, retain=0.2, random_select=0.05, mutate=0.01):
	graded = [ (fitness(x), x) for x in pop]
	graded = [ x[1] for x in sorted(graded)]
	best_offset = int(len(graded)*0.2)
	best = graded[:best_offset]
	# seleciona alguns entre os que nao sao melhores
	for individual in graded[best_offset:]:
		if random() < 0.05:
			best.append(individual)

	# mutate em alguns dos melhores
	for individual in best:
		if mutate > random():
			if randint(0, 10) > 5:
				individual[0] = randint(min(individual), max(individual))
			else:
				individual[1] = randint(min(individual), max(individual))

	# cruzamentos
	desired_length = len(pop) - len(best)
	children = []
	while len(children) < desired_length:
		a, b = randint(0, len(best)-1), randint(0, len(best)-1)
		if a == b: continue
		child = [best[a][0], best[b][1]]
		children.append(child)
	best.extend(children)
	return best

p_count = 100
i_length = 2
i_min = -10
i_max = 10
pop_inicial = populacao(p_count, i_min, i_max)
p = pop_inicial
fitness_history = [grade(p),]
for i in xrange(100):
	p = evolve(p)
	fitness_history.append((grade(p), p))

for datum in fitness_history:
	print datum
