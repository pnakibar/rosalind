import re
import sys

#loading codon table
codonTableFile = open('codon_table.txt', 'r')
codonTable = {}

for e in codonTableFile.readlines():
    treatedLine = re.split("(\w\w\w) (\w+)", e)
    i = 0
    for i in range(len(treatedLine)):
        if len(treatedLine[i]) == 3:
            codonTable[treatedLine[i]] = treatedLine[i+1]
   
#now the program starts
rna = open(sys.argv[1], 'r')
rna = rna.readline().replace("\n", "")
amino = ""
for i in range((len(rna)/3)):
    codon = rna[i*3:(3+i*3)]
    tempAmino = codonTable[codon]
    if tempAmino != 'Stop':
        amino += tempAmino


print(amino)

