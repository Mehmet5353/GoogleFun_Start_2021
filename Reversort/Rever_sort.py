N=int(input())
for j in range(N):
    Num=int(input())
    a=list(map(int,input().split()))
    cost=0
    for i in range(len(a)-1):
        MIN=i+1
        Index=a.index(MIN)
        a=a[0:i]+a[i:Index+1][::-1]+a[Index+1:len(a)]
        cost+=Index-i+1
    print("Case #"+str(j+1)+": "+str(cost))
    
    
#3
#4
#4 2 1 3
#2
#1 2
#7
#7 6 5 4 3 2 1

