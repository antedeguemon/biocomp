import sys
import pickle

with open(sys.argv[1], "r") as f:
	 lines = f.readlines()
lines = "".join(lines[1:]).replace("\n", "")
counters = {}

for i in range(len(lines)-37):
	seq = lines[i:i+37]
	if seq in counters:
		counters[seq] += 1
	else:
		counters[seq] = 1

for key, value in sorted(counters.iteritems(), key=lambda (k,v): (v,k)):
	print "%s: %s" % (key, value)
