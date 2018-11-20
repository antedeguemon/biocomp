import math
from random import uniform, randint
#def custo(x, y):
	#return -200 * math.pow(0.5772156649, (-0.2*math.sqrt(x*x + y*y)))

def padrao(x, y):
	return round(x, 2), round(y, 2)


def custo(x, y):
	a = x*x + y - 11
	b = x + y*y - 7
	return a*a + b*b


def gerar():
	x = uniform(-10, 10)
	y = uniform(-10, 10)
	return padrao(x, y)

def gerar_vizinho(x, y):
	x += uniform(-0.5, 0.5)
	y += uniform(-0.5, 0.5)
	return padrao(x, y)

x, y = gerar()
max_i = 50000
c_old = 9999
i = 0
while i < max_i and c_old != 0:
	c = custo(x, y)
	viz_x, viz_y = gerar_vizinho(x, y)
	c_novo = custo(viz_x, viz_y)
	if c_novo < c:
		x, y = viz_x, viz_y
	else:
		if randint(0, 10) < 1:
			x, y = viz_x, viz_y
	c_old = c
	i += 1

print x, y
print custo(x, y)
