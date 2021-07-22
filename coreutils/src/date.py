import subprocess

def compare_hash(command):
	popen = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	(hash_value, stderrdata) = popen.communicate()
	
	count = 0

	for i in range(10000):
		popen = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
		(tmp, stderrdata) = popen.communicate()
		if hash_value != tmp:
			count += 1

	print(hash_value)
	print(count)

def main():
	print compare_hash("./date")

if __name__ == "__main__":
	main()
