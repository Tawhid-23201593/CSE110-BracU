"""
Write the Python code of a program that reads a student’s mark for
a single subject, and prints out the corresponding grade for that mark.
The mark ranges and corresponding grades are shown in the table below.
You need to make sure that the mark is valid. For example, a student cannot
receive -5 or 110 marks. So, the valid marks range from 0 to 100.
Marks       	Grade
90 or above	      A
80-89	          B
70-79	          C
60-69	          D
50-59	          E
Below 50	      F
"""
m = int(input("Marks: "))
if m>=90:
    print("A")
elif 79<m<90:
    print("B")
elif 69<m<80:
    print("C")
elif 59<m<70:
    print("D")
elif 49<m<60:
    print("E")
else:
    print("F")
