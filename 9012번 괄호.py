N=int(input())
for i in range(N):
    a=input()
    b=list(a)
    sum=0
    for j in b:
        if j=="(":
            sum+=1
        elif j==")":
            sum-=1
        if sum<0:
            print("NO")
            break
    if sum>0:
        print("NO")
    elif sum==0:
        print("YES")
  
