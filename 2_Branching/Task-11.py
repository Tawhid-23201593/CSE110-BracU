"""
Suppose the following expressions are used to calculate
the values of L for different values of S:

Write the Python code of a program that reads a value of
S and then calculates the value of L.
==========================================================
Sample Input 1:
120
Sample Output 1:
2416.2162162162163
Explanation: Since S (user input) given here is 120 >= 100,
so L = 12000 / (4 + (120 * 120)/14900) = 2416.2162162162163
==========================================================
Sample Input 2:
3
Sample Output 2:
1875
Explanation: Since S (user input) given here is 3 < 100,
so L = 3000 - 125 * 3 * 3 = 1875

"""
S = int(input("S :"))
if S < 100:
    print(3000-125*S**2)
else:
    print(12000/((4+(S**2))/14900))