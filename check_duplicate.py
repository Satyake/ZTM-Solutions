import numpy as np 
a=[4,2,3,3]
b=[]

for i in a:
  if i not in b:
    b.append(i)
  

  elif i in b:
    print('True')

