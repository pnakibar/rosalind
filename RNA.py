f = open("rosalind_rna.txt", 'r')
dna = f.readline()

rna = ''
for i in dna:
	if i == 'T':
		rna+='U'
	else:
		rna+=i

print(rna)
