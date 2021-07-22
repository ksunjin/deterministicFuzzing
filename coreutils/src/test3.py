import subprocess

Pipe1=subprocess.Popen(['ltrace', './tty', '-s'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

traceA=Pipe1.communicate()[1]
print(traceA)

Pipe2=subprocess.Popen(['tail', '-n', '1', '.clang_hash'], stdout=subprocess.PIPE)

hashA=Pipe2.communicate()[0]
print(hashA)

count=0

error=''
for i in range(1000):
   pipe1=subprocess.Popen(['ltrace', './tty', '-s'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   traceB=pipe1.communicate()[1]
   pipe2=subprocess.Popen(['tail', '-n', '1', '.clang_hash'], stdout=subprocess.PIPE)
   hashB=''
   hashB+=pipe2.communicate()[0]   
   if hashA != hashB :
      if hashB == 'execution hash :e7207c49fe075f3b \n':
         print('error\n')
      else:
         print("-------------<START>-------------\n")
         print(traceB)
         print(hashB)
         print("-------------<END>-------------\n")
      error+=hashB
      count+=1

  


print("===========Difference Occurred : {}===========\n".format(count))
print("===========Error Sequence===========")
print(error)
