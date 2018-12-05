import sys
seq = "ctgttatacaacgcgtcatggcggggtatgcgttttggtcgtcgtacgctcgatcgttaacgtaggtc"
possiveis = []

tamanho = int(sys.argv[1])
max_dist = int(sys.argv[2])

for i in range(len(seq)-tamanho):
	possiveis.append(seq[i:i+tamanho])

def distancia(a, b):
	if len(a) > len(b):
		a, b = b, a
	dist = 0
	for i in range(len(a)):
		if a[i] != b[i]:
			dist += 1
	return dist
conta = {}
for i in range(len(possiveis)):
	for j in range(len(possiveis)):
		if i == j: continue
		if distancia(possiveis[i], possiveis[j]) <= max_dist:
			if possiveis[i] in conta:
				conta[possiveis[i]] += 1
			else:
				conta[possiveis[i]] = 1

print(conta)
