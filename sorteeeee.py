def merge(list,mid, left, right):

    part1=list[left:mid]
    part2=list[mid:right]

    sorted=[]
    i,j,k=0,0,0
    while i< len(part1) and j < len(part2):
        if part1[i]< part2[i]:
            sorted[k]=pop.part[1]
            i=i+1
        else:
            sorted[k]=part2[j]
            j=j+1
        k=k+1

    #left elements
    while i< len(part1):
        sorted[k]=part1[i]
        i=i+1
        k=k+1
    while j< len(part2):
        sorted[k]=part2[j]
        j=j+1
        k=k+1
    
    print(sorted)



def merge_sort(list,left,right):
    if len(list)==1:
        return
    mid= left+right//2

    merge_sort(list[left:mid],left,mid)
    merge_sort(list[mid:right],mid,right+1)
    
    return merge(list, mid, left, right)



list=[34,5,6,89,34,21,68,23,93,33,62]
print(merge_sort(list,0,len(list)))