
# coding: utf-8

# In[5]:

while (1):
    l = int(input())
    if (l == 0):
        break
    string = str(raw_input())
    newStr = str()
    ns = str()
    i = 0
    for i in range(len(string) / l):
        if i % 2:
            newStr += string[(i + 1) * l - 1:i * l - 1:-1]
        else:
            newStr += string[i * l:(i + 1) * l:1]
    j = 0
    for j in range(l/1):
        i = 0
        for i in range((len(newStr) / l)/1):
            ns += newStr[i * l +j]
    print(ns)


# In[ ]:




# In[ ]:



