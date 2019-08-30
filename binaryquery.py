n, q = map(int,input().split())
nlist=list(map(int,input().split()))
for query in range(q):
    query=input()
    if query[0] == '1':
        print(nlist)
        t,x = map(int,query.split())
        if nlist[x-1] == 1:
            nlist[x-1] = 0
        else:
            nlist[x-1] = 1
        print(nlist)
    else:
        t,l,r = map(int,query.split())
        if nlist[r-1] == 1:
            print('ODD')
        else:
            print('EVEN')




''' question :  given an array with only numbers 0 and 1. There are two types of queries -

0 L R : Check whether the number formed from the array elements L to R is even or odd and print EVEN or ODD respectively. Number formation is the binary number from the bits status in the array L to R

1 X : Flip the Xth bit in the array 

Indexing is 1 based

Input
First line contains a number N and Q as input. Next line contains N space separated 0 or 1. Next Q lines contain description of each query 

Output
Output for only query type 0 L R whether the number in range L to R is "EVEN" or "ODD" (without quotes).

SAMPLE INPUT 
5 2
1 0 1 1 0
1 2
0 1 4

SAMPLE OUTPUT 
ODD

'''