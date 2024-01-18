"""
Write the Python code of a program that finds the number of hours,
minutes, and seconds in a given number of seconds. The number of
seconds is taken as input from the user.
==========================================================
Sample Input 1:
10000
Sample Output 1:
Hours: 2 Minutes: 46 Seconds: 40
Explanation:
10000 seconds = 10000 // 3600 = 2 hours and 10000 % 3600 = 2800 seconds.
Then again, 2800 // 60 = 46 minutes and 2800 % 60 = 40 seconds.
And hence we have arrived at our answer.
==========================================================
Sample Input 2:
500
Sample Output 2:
Hours: 0 Minutes: 8 Seconds: 20

"""
s = int(input("Second: "))
hr = s//3600
secD = s%3600
min= secD//60
sec = secD%60
print(f'Hours: {hr} Minutes: {min} Second: {sec}')