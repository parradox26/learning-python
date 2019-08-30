q =  int(input())
slist = []
for query in range(q):
    query = list(map(str,input().split()))
    if query[0] == 'E':
        for i in reversed(range(len(slist))):
            if query[1] in slist[i]:
                slist.insert(i+1,query[1:])
                break
        else:
                slist.append(query[1:])
    else:
        print(f"{int(slist[0][0])} {int(slist[0][1])}")
        slist.remove(slist[0])
        