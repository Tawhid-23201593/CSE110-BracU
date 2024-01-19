"""
Write a python program that takes the CGPA and no of credits completed by a student
and prints whether the student is eligible for a waiver and of what percentage.
To be eligible for a waiver, a student must have completed at least 30 credits
and earned a CGPA greater or equal to 3.8. If not, please print "The student is not
eligible for a waiver".

CGPA	         Waiver percentage
3.80 - 3.89	        5 percent
3.90 - 3.94	        50 percent
3.95 - 3.99	        75 percent
4.00	            100 percent
==========================================================
Sample Input 1:
3.93
78
Sample Output 1:
The student is eligible for a waiver of 50 percent.
==========================================================
Sample Input 2:
3.79
24
Sample Output 2:
The student is not eligible for a waiver
==========================================================
"""
c = int(input("Creadit compeated: "))
cgpa =float(input("CGPA: "))
if c > 29:
    if 3.80 <= cgpa <= 3.89:
        print("The student is eligible for a waiver of 25 percent.")
    elif 3.90 <= cgpa <= 3.94:
        print("The student is eligible for a waiver of 50 percent.")
    elif 3.95 <= cgpa <= 3.99:
        print("The student is eligible for a waiver of 75 percent.")
    elif cgpa == 4:
        print("The student is eligible for a waiver of 100 percent.")
else:
    print("The student is not eligible for a waiver.")