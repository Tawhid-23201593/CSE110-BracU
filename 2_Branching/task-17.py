"""
Write the Python code of a program that reads an integer, and prints the integer
if it is NOT a multiple of 2 OR NOT a multiple of 5.
For example, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22\
hint(1): you may use the modulus (%) operator for checking the divisibility
hint(2): you can consider the number to be an integer
==========================================================
Sample Input 1:
3
Sample Output 1:
3
==========================================================
Sample Input 2:
15
Sample Output 2:
15
==========================================================
Sample Input 3:
20
Sample Output 3:
No
==========================================================
Sample Input 4:
14
Sample Output 4:
14

"""
n = int(input("Give a number: "))
if n%2==0 or n%==0:
    print(n)
else:
    print("No")