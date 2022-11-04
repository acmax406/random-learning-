def merge(list):
    x=list[:len(list)//2]
    y=list[len(list)//2:]
    i=0
    j=0
    sorted=[]
    while i<len(x) and j< len(y):
        if x[i]<y[j]:
            sorted.append(x[i])
            i=i+1
        else:
            sorted.append(y[j])
            j=j+1
    
    #left elements in both partisisons

    while i< len(x):
        sorted.append(x[i])
        i=i+1
    while j< len(y):
        sorted.append(y[j])
        j=j+1

    # display
    return sorted


def merge_sort(list):
    if len(list)==1:
        return list[0]
    list[:len(list)//2]
    list[len(list)//2:]

    merge_sort(list[:len(list)//2])
    merge_sort(list[:len(list)//2])

    return merge(list)



list=[34,5,6,89,34,21,68,23,93,33,62]
print(merge_sort(list))