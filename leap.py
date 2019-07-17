Year=eval(input("Enter a year:"))
if(Year%400==0) or ((Year%4==0) and (Year%100!=0)):
  print("yes")
else:
  print("no")
