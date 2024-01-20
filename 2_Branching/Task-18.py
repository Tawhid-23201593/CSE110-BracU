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
