a=[1,2,3,4,5,6,7]
k=3
c=[]

part1=a[len(a)-k:len(a)+1]
part2=a[0:len(a)-k]

joined=part1+part2
print(joined)
