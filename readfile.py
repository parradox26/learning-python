xfile = open('F:\PYTHON\pythoncode\dummy.txt')
count = 0
c = 0
for line in xfile:    #reading a file per line 
    for word in line.split():
        if word in 'one':
            c+=1
        print(word)
    count+=1
    print(f'{count}: {line}  {c}')
    
