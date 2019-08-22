try:
    fname = input('provide a file name: ')
    if len(fname) < 1 :
        print("name can not be empty..!")
    else:
        xfile = open(fname)
except FileNotFoundError:
    print(f'File not found : {fname}')
    exit()
keyword = input('Enter the keyword you want to search: ')
count = 0
c = 0
for line in xfile:     #reading a file per line 
    line = line.rstrip()    #removes whitespaces from right hand side
    for word in line.split():
        if word in keyword:
            c+=1
    count+=1
    print(f'{keyword} is occured {c} times in total of {count} line(s)')
xfile.close()
    
