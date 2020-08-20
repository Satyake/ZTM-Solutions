a=[2,5,6,7,8,2]
c={}
for i in range(len(a)):
 if a[i] not in c:
   c[a[i]]=i
 elif a[i] in c:
   print(a[i])
   break
