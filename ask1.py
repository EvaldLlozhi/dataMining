import sys
from random import randint

N = 1000
K = int(sys.argv[1])

lines = []

for i in range (0,K):
	line = raw_input()
	lines.append(line)

for i in range (10, N):
	try:
		line = raw_input()
		p = randint(0,i)
		if p < K:
			lines[p] = line
	except:
		print("EOF")
		break

for l in lines:
	print l
