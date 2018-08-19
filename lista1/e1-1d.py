with open("sequence.fasta", "r") as f:
	 lines = f.readlines()
lines = "".join(lines[1:]).replace("\n", "")
counters = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
unknown = []
for letter in lines:
	if letter in counters:
		counters[letter] += 1
	else:
		unknown.append(letter)
print "Contadores:", counters
if len(unknown) > 0:
	print "Sim, caracteres diferentes encontrados:", list(set(unknown))
else:
	print "Nao foram encontrados caracteres diferentes"
