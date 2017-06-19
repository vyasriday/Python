StartDay = input("Enter the No of day You want ot go on")
Stay = input("Enter for how many nights you wish to stay")

ReturnDay = (int(StartDay) + int(Stay))%6

print(ReturnDay-1)
