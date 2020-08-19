def two_sum(target,array):
    h={}
    for i in range(len(a)):
        if array[i] not in h:
            h[target-array[i]]=i
        elif array[i] in h :
            print( h[array[i]],i)
