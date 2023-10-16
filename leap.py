#leap or not
year=int(input("Enter the year:"))
if year%4==0:
  if year%100==0:
    if year%400==0:
      print("leap year")
    else:
      print("not leap")
  else:
    print("leap year")
