#x
def merge_sort(list,left,right):
    if right>=left:
        return
    mid=right+left//2
    x=list[right:mid]
    merge_sort(x,right,mid)
    y=list[mid:left+1]
    merge_sort(y,mid,left)

    return x
    

list=[20,45,2,3,90,7,100]
left=len(list)-1
right=0
print(merge_sort(list,left,right))
    