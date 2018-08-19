import sys

arquivo = sys.argv[1]
matricula = sys.argv[2]

def complementar(seq):
	nova_seq = ""
	for i in range(len(seq)):
		if seq[i] == "A":
			nova_seq += "T"
		elif seq[i] == "C":
			nova_seq += "G"
		elif seq[i] == "T":
			nova_seq += "A"
		elif seq[i] == "G":
			nova_seq += "C"
		else:
			nova_seq += "N"
	return nova_seq

def gerar_matricula(seq):
	nova_seq = ""
	tabela = {"0": "A", "1": "T", "2": "G", "3": "C", "4": "C", "5": "G", "6": "T", "7": "A", "8": "A", "9": "C"}
	for i in range(len(seq)):
		nova_seq += tabela[seq[i]]
	return nova_seq

def mutar(seq):
	sequencias = []
	sequencia = [_ for _ in seq]
	sequencia[4] = "A"
	sequencias.append("".join(sequencia))
	sequencia[4] = "G"
	sequencias.append("".join(sequencia))
	sequencia[4] = "T"
	sequencias.append("".join(sequencia))
	sequencia[4] = "C"
	sequencias.append("".join(sequencia))
	return sequencias

matricula = gerar_matricula(matricula)
sequencias = [complementar(matricula)] + mutar(matricula)

with open("sequence.fasta", "r") as f:
	 lines = f.readlines()
lines = "".join(lines[1:]).replace("\n", "")

print "Sequencias geradas: ", sequencias
counters = {}
for seq in sequencias:
	counters[seq] = 0

for i in range(len(lines)-8):
	seq = lines[i:i+8]
	if seq in counters:
		counters[seq] += 1

for seq in counters.keys():
	print seq, counters[seq]
