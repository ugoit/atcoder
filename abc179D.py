#間違いなくタイムアウトするが、とりあえず時間をかければ計算できるところまで実装した。

[N,K]=list(map(int,input().split()))
L=[""]*K
R=[""]*K
for i in range(K):
    [L[i],R[i]]=list(map(int,input().split()))

S=[]
for i in range(K):
    for j in range(L[i],R[i]+1):
        S.append(j)

S.sort()
nowpt=N
cnt=0

def move(nowpt,cnt):  
    for i in range(len(S)):
        if nowpt>S[i]:
            nowpt-=S[i]
            nowpt,cnt=move(nowpt,cnt)
        elif nowpt==S[i]:
            cnt+=1
            nowpt-=S[i]
    return nowpt,cnt


ans=move(N,0)

print(ans[1])



