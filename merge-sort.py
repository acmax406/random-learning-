def merge(list):
    mid=int(len(list)/2)
    part1=list[0:mid]
    part2=list[mid: int(len(list))]
    i=0
    j=0
    result=[]
    while len(part1)>0 and len(part2)>0:
        if part1[i]>part2[j]:
            result.append(part2[j])
            j=j+1
        else:
            result.append(part1[i])
            i=i+1
    return result
def merge_sort(list):
    left=len(list)-1
    mid= left+right
    merge_sort(list[:mid])
    merge_sort(list[mid:])

    return merge(list)


list=[23,54,12,45,2,45,23,56]
print(merge_sort(list))

