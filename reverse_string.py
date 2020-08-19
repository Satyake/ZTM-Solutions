

#Solution1
def reverse_str(string):
  string=(string)
  reversed_string=string[::-1]
  return print( reversed_string )

#Solution 2
def reverse_str1(String):
  d=[]
  for i in range(len(String)-1,-1,-1):
    d.append(String[i])
  
  return print(d)
  
  
  
