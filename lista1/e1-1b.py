import sys

def complementar(seq):
	nova_seq = ""
	dic = {"A": "T", "C": "G", "G": "C", "T": "A"}
	for i in range(len(seq)):
		nova_seq += dic[seq[i]]
	return nova_seq

def is_palindromo(seq):
	return (seq[::-1] == seq)

with open(sys.argv[1], "r") as f:
	 lines = f.readlines()
lines = "".join(lines[1:]).replace("\n", "")
palindromos = {}
for i in range(len(lines)-10):
	seq = lines[i:i+10]
	if "N" in seq:
		continue
	if (seq[::-1] == complementar(seq)):
		if seq in palindromos:
			palindromos[seq] += 1
		else:
			palindromos[seq] = 1

for seq in palindromos.keys():
	print seq, palindromos[seq]
