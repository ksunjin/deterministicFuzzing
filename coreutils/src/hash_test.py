# -*- coding: utf-8 -*-
import subprocess
import os

count = 0

for i in range(100000):
	subprocess.Popen(['./uniq', '-i', 'test1.txt' ], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	
popen = subprocess.Popen(['ltrace', './uniq', '-i'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
(stdoutdata, stderrdata) = popen.communicate()
print(stdoutdata.strip(), stderrdata.strip())
popen1 = subprocess.Popen(['strace', './uniq',' -i'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
(stdoutdata1, stderrdata1) = popen1.communicate()
print(stdoutdata1.strip(), stderrdata1.strip())

with open('.clang_hash', 'r') as f:
	firstLine = f.next().rstrip()
	print(firstLine)
	for line in f:
		line = line.strip()
		if line != firstLine:
			print(line)
			count += 1
	if count == 0:
		print("\n 오류 없음")
		
print(count) 
os.remove('.clang_hash')

