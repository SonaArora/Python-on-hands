s=raw_input()
name=['Kevin','Stuart']
count_c=0;count_v=0
#sonali
for i in range(len(s)):
    if s[i] in ['A','E','I','O','U']:
            for j in range(len(s[i:])):
                if len(s)-j > i:
                    #print s[i:len(s)-j]
                    count_c += 1
    else:
            for j in range(len(s[i:])):
                if len(s)-j > i:
                    #print s[i:len(s)-j]
                    count_v += 1

if count_c < count_v :
    print name[1],count_v
else :
    print name[0],count_c
