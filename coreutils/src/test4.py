import subprocess

Pipe1=subprocess.Popen(['ltrace', './tty', '-s'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

traceA=Pipe1.communicate()[1]
print(traceA)

Pipe2=subprocess.Popen(['tail', '-n', '1', '.clang_hash'], stdout=subprocess.PIPE)

hashA=Pipe2.communicate()[0]
print(hashA)

count=0
index=0
error=''
for i in range(10000):
	pipe1=subprocess.Popen(['ltrace', './tty', '-s'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	traceB=pipe1.communicate()[1]
	pipe2=subprocess.Popen(['tail', '-n', '1', '.clang_hash'], stdout=subprocess.PIPE)
	hashB=''
	hashB+=pipe2.communicate()[0]
	index+=1
	print(index)
	if hashA != hashB :
		error+=hashB
		count+=1


print("===========Difference Occurred : {}===========\n".format(count))
print("===========Error Sequence===========")
print(error)
