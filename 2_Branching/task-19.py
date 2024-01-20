f = int(input("Tamperature in Fahrenheit: "))
c = ((f-32)*0.56)
if c<20:
    print("Winter")
elif 19<c<26:
    print("Autumn")
elif 25<c>30:
    print("Spring")
else:
    print("Summer")