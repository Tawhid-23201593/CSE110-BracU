"""
Write the Python code of a program that reads the radius of a circle
and prints its circumference and area.
==========================================================
Example 1:
Sample Input:
4
Sample Output:
Area is 50.26548245743669
Circumference is 25.132741228718345
==========================================================
Example 2:
Sample Input:
3.5
Sample Output:
Area is 38.48451000647496
Circumference is 21.991148575128552
=======================================================
"""
radius = float(input("Radius: "))
print("Area is", 3.1416*(radius**2))
print("Circumference is", 2*3.1426*radius)