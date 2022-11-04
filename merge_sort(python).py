def merge_sort(list):
    if len(list)<2:
        return list
    
    mid= int(len(list)/2) # mid= len(list)//2 for slicing the array

    x=merge_sort(list[:mid])
    y=merge_sort(list[mid:])
    result=[]
    while len(x)> 0 or len(y) > 0:
        if len(x) > 0 and len(y) > 0:
            if x[0]> y[0]:
                result.append(x[0])
                x.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
        elif len(y)>0:
            for i in y:
                result.append(i) 
                y.pop(0)
        else:
            for i in x:
                result.append(i)
                x.pop(0)
    return result 