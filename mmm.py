
def merge(list,left,right,mid):
    sorted=[]
    part1=list[right:mid]
    print(part1)
    part2=list[mid:left+1]
    print(part2)
    i,j=0,0
    while i<len(part1) and j<len(part2):
        if part1[i]<=part2[j]:
            sorted.append(part1[i])
            i=i+1
        else:
            sorted.append(part2[j])# list=[23,45,234,12,34,11,78]
            j=j+1   
    print(sorted)
    if i<len(part1):
        while i < len(part1):
            sorted.append(part1[i])
            i=i+1
    print(sorted)
    if j<len(part2):
        while j< len(part2):
            sorted.append(part2[j])
            j=j+1
    return sorted


        


def merge_sort(list,left,right):
    if left >=right:
        return

    mid=(right+left)//2
    merge_sort(list[right:mid],right,mid)
    merge_sort(list[mid:left+1],mid,mid+1)
    
    return merge(list,left,right,mid)

list=[20,45,2,3,90,7,100]
right=0
left=len(list)-1
print(merge_sort(list,left, right))

