#task:
#Input Format:The first line contains the first name, and the second line contains the last name.
#Output Format: Print the output as mentioned above.

a=raw_input()
b=raw_input()
print "Hello " + a + " " + b + "! You just delved into python."


#task: You are given a string . Your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
#Input Format: single line containing a string .
#Output Formate: Print the modified string
print raw_input().swapcase()


#task: You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
#Input Format :  The first line contains a string consisting of space separated words.
#Output Format :  Print the formatted string.
print "-".join(raw_input().split())
