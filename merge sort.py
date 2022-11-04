def merge(list,left,right,mid):
    i,j=0,0
    part1=[]
    part2=[]
    part1=list[left:mid]
    part2=list[mid:right+1]
    result=[]
    while i<len(part1) and j< len(part2):
        if part1[i]<=part2[j]:
            result.append(part1[i])
            i=i+1
        else:
            result.append(part2[j])
            j=j+1
# the left elements in the part1 and part2
    while i<len(part1):
        result.append(part1[i])
        i=i+1
    while j<len(part2):
        result.append(part1[j])
        j=j+1
    return result

def merge_sort(list,left,right):
    if left<right:
        return
    
    mid= left+right//2
    
    merge_sort(list,left,mid)
    merge_sort(list,mid,right+1)

    merge(list, left,right,mid)

    return merge

list=[23,45,234,12,34,11,78,34,34]
print(merge_sort(list,0,len(list)-1))