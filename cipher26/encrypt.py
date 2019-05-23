import string
arr = string.ascii_lowercase + " " + ",.?!(:)" + "\n"
print arr
file = open("inp.txt", "a+")
ffile = open("a.txt",  "w+")
message = file.read()
en = ""
for i in range(len(message) - 1):
	temp = 0
	for j in range(i + 1):
		temp += arr.index(message[j])
	en += arr[temp%35]
print en
ffile.write(en)