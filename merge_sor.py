def merge(left,right):
    i=0
    j=0
    result=[]
    while i<len(left) and j < len(right):
        if(right[i]<left[j]):
            result.append(right[i])
            i=i+1
        else:
            result.append(left[j])
            j=j+1
    return result
"""
def merge_sort(list):
    if len(list)==1:
        return list[0] #so if the list contains only one element the that element
    mid= len(list)//2
    left = merge_sort(list[:mid]) #right and left are the two partisons
    right =merge_sort(list[mid:])
    return merge(left,right)
""""

def merge_sort(list):
    
list=[23,45,67,21,22,13,9,34,67]
print(merge_sort(list))
