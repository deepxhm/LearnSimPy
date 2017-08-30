def g():
	print("step 1")
	x = yield "Hello"
	print("Step 2 x = %d"% x)
	y = 5 + (yield x)
	print("Step 3 y = %d"% y)

f = g()
f.next()
f.send(5)
