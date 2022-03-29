#Q8. Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.
num = int(input("enter number"))
if num%2 == 0 and num%3 == 0:
    print ("Divisible by 3 and 2")
else:
    print ("not divisible by 2 and 3")