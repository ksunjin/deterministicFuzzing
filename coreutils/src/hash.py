# -*- coding: utf-8 -*-
import subprocess
import os

count = 0

for i in range(100000):
	subprocess.Popen(['./pathchk','--portability' ,'tee-test-file.txt' ], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	

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
