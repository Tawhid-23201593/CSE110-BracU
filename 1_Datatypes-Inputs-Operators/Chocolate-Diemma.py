"""
Write a python program that takes an integer from the user which represents the number of chocolates that he/she has.
He/She decided to distribute the chocolates equally among 3 friends, keeping the remaining chocolates for him/herself.
Find out the number of chocolates each friend will receive and the number of chocolates that will be remaining.
Sample Input:
50
Sample Output:
Each friend will receive 16 chocolates
The number of remaining chocolates is 2

"""
A = int(input("Number of chocolates: "))
print("Each friend will receive",((A-(A%3))//3),"chocolates")
print("The number of remaining chocolates is",(A%3))