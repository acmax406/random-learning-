#finding the peaks in 1D arry

import numpy
def find_peaks(A):
    L=len(A)
    if A[0]>A[1]:
        print(A[0])
    if A[len(A)-1]>= A[len(A)-2]:
        print(A[len(A)-1])
    for i in range(len(A-2)):
        if A[i+1]>= A[i+2] and A[i+1]>= A[i]:
            print(A[i+1])

    
A=[100,100,56,100,100,100]
find_peaks(A)

