"""
1.Take a String and an integer input from the user and print these.

Sample Input:
hello world
21

Sample Output:
hello world
21

"""

print("hello world")
print(21)

"""
2. Take two integer inputs from the user and print their summation and multiplication..

Sample Input:
10
5

Sample Output:
Summation: 15
Multiplication: 50

"""
a = int(input("A: "))
b = int(input("B: "))
print("Summation:", a+b)
print("multiplication:", a*b)

"""
3. Take one integer input and one float input from the user and print their
 addition and subtraction in the same line separated by a space.

Sample Input:
4
5

Sample Output:
9.0  -1.0

"""
c = int(input("C: "))
d = float(input("D: "))
print(c+d, (c-d))

"""
4. Take two integer numbers from the user. Convert the second number into float. 
Now convert both numbers into string and add them. Print the addition.

Sample Input:
2
3
Sample Output:
23.0

"""
e = int(input("E: "))
f = float(input("F(Must be float: "))
p = str(e)
q = str(f)
print(p+q)