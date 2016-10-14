'''Task:You are given a string .
Your task is to find out if the string contains: alphanumeric characters, alphabetical
characters, digits, lowercase and uppercase characters.

Input Format: A single line containing a string .

Output Format:
In the first line, print True if has any alphanumeric characters. Otherwise, print False.
In the second line, print True if has any alphabetical characters. Otherwise, print False.
In the third line, print True if has any digits. Otherwise, print False.
In the fourth line, print True if has any lowercase characters. Otherwise, print False.
In the fifth line, print True if has any uppercase characters. Otherwise, print False.
'''

s=raw_input()
alpha="False"; alnum="False"; digit="False"; low="False"; upp="False"

for i in range(len(s)):
    if s[i].isalpha():
        alpha="True"
    if s[i].isalnum():
        alnum="True"
    if s[i].isdigit():
        digit="True"
    if s[i].islower():
        low="True"
    if s[i].isupper():
        upp="True"

print alpha
print alnum
print digit
print low
print upp
