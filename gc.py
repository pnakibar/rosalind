import sys

def percentageOfGC(dna):
	qtyOfGC = dna.count('C') + dna.count('G')
	return qtyOfGC*100/len(dna)


f = open(sys.argv[1], 'r')
dnas = {}
dnaName = ""
for l in f.readlines():
	if l[0] == '>':
		dnaName = l[1:].replace("\n", "")
		dnas[dnaName] = ""
	else:
		dnas[dnaName] += l.replace("\n", "")
maior = ("", -1)

for e in dnas:
	pcE = percentageOfGC(dnas[e])
	if pcE > maior[1]:
			maior = (e, pcE)

for e in maior:
	print(e)
