#!/usr/bin/env python3

# list
wordbank= ["indentation", "spaces"] 

tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

wordbank.append(4)
print(wordbank)

num = int(input("Please enter a number 0 and 18: "))
student_name = tlgstudents[num]

print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent." )
