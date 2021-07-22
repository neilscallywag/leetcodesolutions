def r(x): 
	b = pow(2, 31)-1
	a = pow(-2, 31)
	x = str(abs(x))
	cx = x[::-1]
	y = int(cx)
	y = y * -1 if int(x) < 0 else y
	return y if (y < b and y > a) else 0

print(r(234))

