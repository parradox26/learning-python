from collections import Counter
input_string = input("Enter a list element separated by comma ")
list  = input_string.replace(" ","").split(",")
fre = Counter(list)
for i in fre.keys():
    print('{} - {}'.format(i,fre[i])) 



"""
Approach: 

I have taken comma-separated inputs as a single string and stored them as a list using split and replace methods in the input string
I have used Counter (Dict subclass for counting repeated elements and store them in a dictionary ) from collections. 
Then I printed the consecutive keys with their repeat count in the dictionary
"""