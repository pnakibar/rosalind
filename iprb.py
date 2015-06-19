class Population:
	def __init__(self, k, m, n):
		self.k = float(k)
		self.m = float(m)
		self.n = float(n)
		self.total = lambda: self.k+self.m+self.n

	def dominantProbability(self):
		#probMandK = (self.m/self.total()) * (self.k)/(self.total() -1) * probability('m','k')
		#probNandK = (self.n/self.total()) * (self.k)/(self.total() -1) * probability('n', 'k')
		#probNandM = (self.n/self.total()) * (self.m)/(self.total() -1) * probability('n', 'm')
		
		probKandK = (self.k/self.total()) * (self.k-1)/(self.total() -1) * probability('k','k')
		probKandM = (self.k/self.total()) * (self.m)/(self.total() -1) * probability('k', 'm') * 2
		probKandN = (self.k/self.total()) * (self.n)/(self.total() -1) * probability('k', 'n') * 2

		probMandM = (self.m/self.total()) * (self.m-1)/(self.total() -1) * probability('m','m')
		probMandN = (self.m/self.total()) * (self.n)/(self.total() -1) * probability('m', 'n') * 2
		
		probNandN = 0 #just do it

		print(probKandK+probKandM+
			probKandN+
probMandM+
				probMandN+
				probNandN)

def probability(s1, s2):
	if (s1 == 'k') or (s2 == 'k'): 
		print("k inda house")
		return 1.0
	elif (s1 == 'm') and (s2 == 'm'):
		print("both are m!") 
		return 3.0/4.0
	elif (s1 == 'n') and (s2 == 'n'): 
		print("both are n!")
		return 0
	#s1 or s2 can't be equals to 'k' anymore
	elif s1 != s2: 
		print("yeah!")
		return 1.0/2.0
	else: return None








popu = Population(24, 30, 15)
popu.dominantProbability()



