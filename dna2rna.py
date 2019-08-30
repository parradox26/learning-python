s=input()
j=list(s)
for i in range(len(s)):
    if s[i] == 'G':
        j[i] = 'C'
    elif s[i] == 'C':
        j[i] = 'G'
    elif s[i] == 'T':
        j[i] = 'A'
    elif s[i] == 'A':
        j[i] = 'U'   
    else:
        j='Invalid Input'
        break
print(''.join(j))