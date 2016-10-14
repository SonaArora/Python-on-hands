#Task: Read a given string, change the character at a given index and then print the modified string.
#Input Format: The first line contains a string S,The next line contains an integer , denoting the index location
# and a character separated by a space.
#Output Format: Using any of the methods explained above, replace the character at index
#with character .


S=raw_input()
l=raw_input().split()
S=S[:int(l[0])]+l[1]+S[int(l[0])+1:]
print S

#alter:
'''p=list(S)
p[int(l[0])]=l[1]
print str(p)
'''
