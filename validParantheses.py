def sol1(arr):


	cnt = 0
	for i in arr:
		if i == ')':
			cnt -=1
		elif i == '(':
			cnt+=1
		if i == '}':
			cnt -=1
		elif i == '{':
			cnt+=1
		if i == ']':
			cnt -=1
		elif i == '[':
			cnt+=1
		elif cnt < 0:
			return False
		
	if cnt > 0:
		return False
	return True

print(sol1("({})"))