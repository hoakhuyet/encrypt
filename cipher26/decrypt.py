import string
file = open("a.txt", "a+")
m = file.read()
print m
p = m[0]
for i in range(1, len(m)):
	t = 0
	for j in p:
		t += r.index(j)
	p += r[(- t + r.index(m[i])) % 35]
print p
