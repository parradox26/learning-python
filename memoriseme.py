from collections import Counter
n=int(input())
nlist=list(map(int, input().split()))
q=int(input())
fre = Counter(nlist)
print(fre)
for query in range(q):
    bi=int(input())
    if fre[bi]==0:
        print('NOT PRESENT')
    else:
        print(fre[bi])
        
