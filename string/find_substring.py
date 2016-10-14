#TASK:In this challenge, the user enters a string and a substring. You have to print the number
#of times that the substring occurs in the given string. String traversal will take place from
#left to right, not from right to left.
#Input Format:The first line of input contains the original string. The next line contains the substring.
#Output Format:Output the integer number indicating the total number of occurrences of the substring in the
#original string.


s,t=[raw_input() for k in range(2)]
#s is our main string and t is the target substring

count=0

for j in range(len(s)):
  if s[j:j+len(t)]==t:
    count=count+1

print count
