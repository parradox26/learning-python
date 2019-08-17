fname = input("enter the file name: ")
finput = open(fname)
name_input = finput.read() #open file as a single string
names = name_input.split()
store = dict()
maxm = [-1,'none']
for name in names: 
    store[name] = store.get(name,0) + 1  #get method in dict to check availablity of a key
    if store[name] > maxm[0]:
        maxm[1] = name
        maxm[0] = store[name]
print(f'{maxm[1]} in {store}')

        
    



