def solution(n, tops):
    aUsed = [0]*(n)
    aNotused = [0]*(n)
    
    aUsed[0] = 1
    aNotused[0] = 3 if tops[0]==1 else 2
    
    for k in range(1, n):
        if tops[k]==1:
            aUsed[k] = aUsed[k-1] + aNotused[k-1]
            aNotused[k] = aUsed[k-1]*2 + aNotused[k-1]*3 #(a[k-1] + b[k-1]) + (b[k-1]) + (a[k-1] + b[k-1])

        elif tops[k]==0:
            aUsed[k] = aUsed[k-1] + aNotused[k-1]
            aNotused[k] = aUsed[k-1] + aNotused[k-1]*2 #(a[k-1] + b[k-1]) + (b[k-1])
        
        aUsed[k] %= 10007
            
    return (aUsed[-1]+aNotused[-1])%10007
    