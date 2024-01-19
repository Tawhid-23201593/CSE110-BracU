d = int(input("Distance in meter: "))
t = int(input("Time in second: "))
kmH = ((d/1000)/(t/3600))
if kmH<60:
    print("Too slow. Needs more changes.")
elif 59<kmH<91:
    print("Velocity is okay. The car is ready!")
else:
    print("Too fast. Only a few changes should suffice.")
