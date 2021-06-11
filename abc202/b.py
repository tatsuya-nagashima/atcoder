s = input()

ans=[]
for i in range(len(s)):
    if s[i] == '6':
        ans.insert(0,'9')
    elif s[i] == '9':
        ans.insert(0,'6')
    else:
        ans.insert(0,s[i])

print (''.join(ans))



