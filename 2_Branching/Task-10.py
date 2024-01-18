"""
Write a Python program to compute and display a person’s weekly salary as determined
by the following conditions:
●	If the hours worked is less than or equal to 40,
then the person receives Tk 200 per hour.
●	If the hours worked is greater than 40, then the person
receives Tk 8000 plus Tk 300 for each hour worked over 40 hours.
The program should request the hours worked as an input from
the user and display the salary as output. You need to make
ure that user input is valid. For example, a person cannot
work for -5 hours or more than 168 hours in a week. So, the
valid hours range is 0 to 168. For invalid hours, print outputs
as given in the samples below.
==========================================================
Sample Input 1:
100
Sample Output 1:
26000
Explanation: Since, the number of hours worked is 100 > 40, therefore salary = 8000 + (100 - 40) * 300 = 26000.
==========================================================
Sample Input 2:
30
Sample Output 2:
6000
Explanation: Since, the number of hours worked is 30 < 40, therefore salary = 30 * 200 = 6000.
==========================================================
Sample Input 3:
-30
Sample Output 3:
Hour cannot be negative
==========================================================
Sample Input 4:
170
Sample Output 4:
Impossible to work more than 168 hours weekly

"""
t = int(input("Working time: "))
if t<0:
    print("Time cannot be negative")
elif t>169:
    print("Impossible to work more than 168 hours weekly")
elif t<=40:
    print(t*200)
else:
    print(8000+(t-40)*300)