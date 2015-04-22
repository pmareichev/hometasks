
# coding: utf-8

# In[ ]:

import sys
f = open(sys.argv[1])
class brackets:
	def __init__(self, exp):
		self.exp = exp
	def change(self, i):
		if self.exp[i - 1] == ')':
			self.exp = self.exp[:i - 1] + '(' + self.exp[i-1:]
		else : 
			self.exp = self.exp[:i - 1] + ')' + self.exp[i-1:]
	def check(self):
		i = 0
		n = 0
		while i < len(self.exp):
			if self.exp[i] == '(':
				n += 1
			else :
				n += -1
            i += 1
            if p<0:
                break
        if p == 0:
            print("YES")
        else :
            print("NO")
i = 0
while i < 10:
    f.readline()
    br = brackets(f.readline())
    M = int(f.readline())
    print("Test %d:" % i+1)
    j = 0
    while j < M:
        k = int(f.readline())
        if k == 0:
            br.check()
        else :
            br.change(k)
        j += 1
    i += 1

