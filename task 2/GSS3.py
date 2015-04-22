
# coding: utf-8

# In[23]:

class query:
    def __init__(self, a):
        self.query = a
    def mod(self, x, y):
        self.query[x - 1] = y
    def prnmax(self, x, y):
        i=x-1
        rez=0
        while i < y:
            rez += int(self.query[i])
            i+=1
        i=x-1
        while i < y:
            j=i
            sum=0
            while j<y:
                sum=sum+int(self.query[j])
                rez=max(sum,rez)
                j+= 1
            i+=1
        print rez
        
N = int(input())
a = query(raw_input().split(' '))
M = int(input())
i=0
while i < M:
    k,x,y = map(int, raw_input().split(' '))
    if k == 0:
        a.mod(x, y)
    if k == 1:
        a.prnmax(x, y)
    i += 1


# In[ ]:



