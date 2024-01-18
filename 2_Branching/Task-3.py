"""
Write the Python code of a program that reads two numbers from the user. The program should then print "First is greater" if the first number is greater, "Second is greater" if the second number is greater, and "The numbers are equal" otherwise.
==========================================================
Sample Input 1:
7
3
Sample Output 1:
First is greater
==========================================================
Sample Input 2:
-33
-3
Sample Output 2:
Second is greater
==========================================================
Sample Input 3:
11
11
Sample Output 3:
The numbers are equal

"""
x = int(input("First Number: "))
y = int(input('Second Number: '))
if x>y:
    print('First is greater')
elif x<y:
    print("Second is greater")
elif x==y:
    print("The numbers are equal")
else:
    print("Invalid Input!")