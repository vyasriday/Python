CurrTime = input("Enter current time in Hours")
Hours = input("Enter number of hours after which you want to ring alarm")


OffTime = (int(CurrTime) + int(Hours))%24


print(OffTime)
