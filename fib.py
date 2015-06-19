def fib(n, litter):
	if (n==1) or (n==2):
		return 1
	else:
		return fib(n-1, litter) + fib(n-2, litter)*litter

print(fib(32,4))
