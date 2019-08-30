t=int(input())
for testcase in range(t):
    n, k=map(int, input().split())
    h=list(map(int, input().split()))
    c=0
    if h[0]>k:
    	if h[0]%k==0:
    		c=c+h[0]//k-1
    	else:
    		c=c+h[0]//k
    for j in range(1, n):
        if h[j]-h[j-1]<=k:
            continue
        elif (h[j]-h[j-1])%k==0:
            c=c+(h[j]-h[j-1])//k-1
        else:
            c=c+(h[j]-h[j-1])//k
    print(c)