def revert(s):
	if s == 'A':
		return 'T'
	elif s == 'T':
		return 'A'
	elif s == 'C':
		return 'G'
	elif s == 'G':
		return 'C'
	else:
		return ''

dna = open('rosalind_revc.txt', 'r').readline()
complemented  = ''
reversedDNA = dna[::-1]

for e in reversedDNA:
	complemented += revert(e)

print(complemented)
	

