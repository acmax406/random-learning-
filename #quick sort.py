#quick sort
import random
def partition(L):
    pivot = L[0]
    lesser =[]
    greater=[]
    for i in range(1, len(L),1):
        if L[i]<pivot:
            lesser.append(L[i])
        else:
            greater.append(L[i])

    #for i in range ( len(lesser)):
    #    L[i]=lesser[i]
    #L[len(lesser)]=pivot
    #for i in range(len(greater)):
    #   L[len(i+lesser)]=
    L[0:len(L)-1]=lesser +[pivot]+greater
    print(lesser)
def main():
    n=16
    x=[100+i for i in range(n)]
    random.shuffle(x)
   
    #sorting the list
    partition(x)
    print(x)
main()
