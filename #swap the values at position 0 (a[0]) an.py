#swap the values at position 0 (a[0]) and x(A[x])
t = a[0]
A[0] = A[x]
A[x] = t

def test(v):
    if v< 10:
        return 2*v
    else:
        return 3*v