"""
Write a Python program that reads two integers M and N respectively
and finds the value of M^N (or MN) and prints the value exactly as shown in
the examples below. Your code should work correctly for any other sample inputs.

Sample Input:
2
3
Sample Output:
2^3: 8

"""
M = int(input("M: "))
N = int(input("N: "))
print(M, "^", N, ": ", M**N, sep="")
