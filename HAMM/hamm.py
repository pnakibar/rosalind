import sys

f = open(sys.argv[1], 'r')

s1 = f.readline().replace("\n", "")
s2 = f.readline().replace("\n", "")

distance = 0

for i in range(len(s1)):
    if s1[i] != s2[i]:
        distance+=1

print(distance)
