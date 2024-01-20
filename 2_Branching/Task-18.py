"""
Fiona has recently started acrylic painting and she is planning to order
a few canvases and paints from an online stationery shop. The price of
each 10 x 10 sized canvas is 120 tk and the price of each 25 ml paint tube
is 75 tk. Depending on the total amount ordered from the shop, she will get
some discounts. The table below shows the discount she will get on her total amount.
================================================== =======
Total Amount (TK)	         Discount (TK)
0 – 299                      No Discount
300 - 499	                 10
500 - 749	                 20
750 - 999	                 50
>= 1000	                     150
Write a python program and take two inputs from the user.
The first input will be the number of canvases and the second
input will be the number of paint tubes ordered. Based on the price
of each item, calculate the total amount that Fiona needs to pay including the discount.
=================================================== =======
Sample Input 1:
5
8
Sample Output 1:
Previous total: 1200
New total after discount: 1050
Explanation: 5 * 120 + 8 * 75 = 1200 Tk was her bill without discount. For 1200 Tk, the
discount amount is 150 Tk. So, her new bill with a discount is (1200 - 150) = 1050 Tk.
==========================================================
Sample Input 2:
0
3
Sample Output 2:
Previous total: 225
New total after discount: 225
Explanation: 0 * 120 + 3 * 75 = 225 Tk was her bill without discount. For 225 Tk, the discount
 amount is 0 Tk. So, her new bill with a discount is (225 - 0) = 225 Tk.

"""
a = int(input("Canvases: "))
b = int(input("Paint tubes: "))
p1 = (a*120 + b*75)
print("Previous total:",p1)
if 299<p1<500:
    print("New total after discount:",p1-10)
elif 499<p1<750:
    print("New total after discount:",p1-20)
elif 749<p1<1000:
    print("New total after discount:",p1-50)
elif p1>=1000:
    print("New total after discount:",p1-150)
else:
    print("No discount")
