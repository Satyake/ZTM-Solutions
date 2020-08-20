a=[-2,1,-3,4,-1,2,1,-5,4]
current_count=a[0]
global_count=a[0]
for i in range(len(a)-1):
  current_count=max(current_count,current_count+a[i])
print(current_count)
