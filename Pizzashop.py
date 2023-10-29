
print("Welcome to your favourite Pizza shop.")
print("\n\n")
print("Thank you for choosing Python Pizza delivery!\n")
size=input("Enter the size(s/m/l):")
size=size.lower()
bill=0
if size=='s':
  bill+=15
elif size=='m':
  bill+=20
elif size=='l':
  bill+=25
else:
  print("Enter correct size")
pep=input("you want pepperoni?(y/n):")
pep=pep.lower()
if pep=='y':
  bill+=3
elif pep=='n':
  bill+=0
else:
  print("Enter correct choice")
ex=input("you want extra cheese?(y/n):")
ex.lower()
if ex=='y':
  bill+=1
  print(f"Total bill is {bill}")
else:
  print(f"Total bill is {bill}")
