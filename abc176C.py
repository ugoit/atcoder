N=int(input())
A=[""]*N
A=list(map(int,input().split()))

maxA=A[0]
cntchair=0
for i in range(N-1):
    if maxA>A[i+1]:
        cntchair+=maxA-A[i+1]
    elif maxA<A[i+1]:
        maxA=A[i+1]

print(cntchair)




