a=[0,1,0,3,12] #test case1
a=[5,0,0,0,9,4]#test case2
for i in a:
  if i==0:
    a.remove(i)
    a.append(i)
print(a)
