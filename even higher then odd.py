def arrange(arr , n):
    arr.sort()
    result = [0]*n
    start = 0
    end = n - 1
    for i in range(n):
        if (i+1) % 2 != 0 :
            result[i] = arr[start]
            start+= 1
        else:
            result[i] = arr[end]
            end-= 1
    for i in result:
        print("{}  ".format(i))


list =input("Enter  list integers separated by comma ").split (",")
li = []
for i in list:
	li.append(int(i))
N = len(li)
arrange(li,N)



"""
1. Approach:

    * sort the list of numbers 
    * arrange highest number to lowest even position and increase the position.
    * arrange lowest number to odd lowest position and increase the position.
    * repeat this till all elements of the list are rearranged.

2. Time complexity = O(n)

3. space complexity = O(n)

4. the given test could not be verified since 
   I couldn't find any logic satisfying the test case however my solution completely satisfies the problem stated.

   """
   