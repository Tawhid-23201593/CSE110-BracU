"""
Write a Python program that reads 3 integers A, B, and C respectively,
and then reads a floating-point number D. After reading, the program should
print the result (as int) using the given formula below.
Formula: AC + (2*B) * (A//2) - D/3

Sample Input:
2
6
8
1.3
Sample Output:
267

"""
A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
D = float(input("D: "))
print(int(A**C+(2*B)*(A//2)-D/3))









