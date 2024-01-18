"""
Write the Python code of a program that reads two numbers
from the user, and prints their sum, product, and difference.
Hint: subtract the second number from the first one
==========================================================
Example 1:
Sample Input:
4
5
Sample Output:
Sum = 9
Product = 20
Difference = -1
==========================================================
Example 2:
Sample Input:
30
2
Sample Output:
Sum = 32
Product = 60
Difference = 28
==========================================================
"""
A = int(input("Give First Number: "))
B = int(input("Give Second Number: "))
print("Sum =", A+B)
print("Product =", A*B)
print("Difference =", A-B)