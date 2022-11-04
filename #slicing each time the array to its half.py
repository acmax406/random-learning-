#slicing each time the array to its half to find the element
def binary_search(sequence,item):
    begin_index=0
    end_index= len(sequence)-1

    while(begin_index<= end_index):
        midpoint= (begin_index + end_index)//2
        midpoint_value= sequence[midpoint]
        if midpoint_value==item:
            return midpoint
        elif item < midpoint_value:
            end_index= midpoint-1
        else:
            begin_index= midpoint+1
    return None 

sequence=[23,45,62,34,532,56,35,67]
print(sequence.sort())
print(binary_search(sequence,62))