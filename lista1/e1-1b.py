import sys

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

def is_palindromo(seq):
	return (seq[::-1] == seq)

with open(sys.argv[1], "r") as f:
	 lines = f.readlines()
lines = "".join(lines[1:]).replace("\n", "")
palindromos = {}
for i in range(len(lines)-9):
	seq = lines[i:i+9]
	if is_palindromo(complementar(seq)):
		if seq in palindromos:
			palindromos[seq] += 1
		else:
			palindromos[seq] = 1

for seq in palindromos.keys():
	print seq, palindromos[seq]
