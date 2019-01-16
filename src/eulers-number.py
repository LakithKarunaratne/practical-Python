x = 1
n_ = 1
end = 100

def func(n):
	n = float((1 + (1 / n)) ** n)
	return n

while x < end:
	n_ = func(n_)
	print (n_)
	x += 1 
print (n_)
