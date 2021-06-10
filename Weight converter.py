weight = int(input("weight: "))
unit = input("lbs or kgs:choose L or K ")
if unit.upper() == "L":
    conversion_1 = weight / 2.2
    print(f'You are {conversion_1} kgs')
else:
    conversion_2 = weight * 2.2
    print(f'You are {conversion_2} lbs')