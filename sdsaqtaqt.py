def msort(list):
    result = []
    if len(list) < 2:
        return list
    mid = int(len(list)/2)
    y = msort(list[:mid])
    z = msort(list[mid:])


    while (len(y) > 0) or (len(z) > 0):
        if len(y) > 0 and len(z) > 0:
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
        elif len(z) > 0:
            for i in z:
                result.append(i)
                z.pop(0)
        else:
            for i in y:
                result.append(i)
                y.pop(0)
    return result


list=[23,46543,22,12,56,0,45,12,34]
print(msort(list))