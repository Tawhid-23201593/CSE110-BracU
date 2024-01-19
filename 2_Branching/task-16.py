"""
Write the Python code of a program that reads an integer, and prints
the integer if it is a multiple of NEITHER 2 NOR 5.
For example, 1, 3, 7, 9, 11, 13, 17, 19, 21, 23, 27, 29, 31, 33, 37, 39 …
==========================================================
hint(1): you may use the modulus (%) operator for checking the divisibility
hint(2): you can consider the number to be an integer
==========================================================
Sample Input 1:
3
Sample Output 1:
3
==========================================================
Sample Input 2:
19
Sample Output 2:
19
==========================================================
Sample Input 3:
5
Sample Output 3:
No
==========================================================
Sample Input 4:
12
Sample Output 4:
No

"""
n = int (input(" Give a number: "))
if n%2==0 or n%5==0:
    print("No")
else:
    print(n)