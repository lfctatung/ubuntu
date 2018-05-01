def sum(*args):
	print("Input : " + str(args))
	i = 0
	first = args[i]
	traceP(first)
	for a in args[1:]:
		i += 1; first += a
		traceP(first, i)

def traceP(tp, i = 0):
	print("Sum[%d] = %s" % (i, str(tp)))

sum(1, 2, 3, 4, 5, 6, 7, 8, 9)
sum('Are ', 'you ', 'happy in ', 'your ', '50', ' birthday?')
