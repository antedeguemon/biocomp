import sys

def distance(s):
	seq = "CAGGAGATCTTCGTGGCCAC"
	d = 0
	for i in range(len(s)):
		if d > 1:
			return 2
		if seq[i] != s[i]:
			d += 1
	return d

with open(sys.argv[1], "r") as f:
	 lines = f.readlines()
lines = "".join(lines[1:]).replace("\n", "")
counters = {}

for i in range(len(lines)-20):
	seq = lines[i:i+20]
	if distance(seq) <= 1:
		print "Sequencia", seq, "em", i
