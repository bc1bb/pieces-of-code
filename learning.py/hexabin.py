# I made this in ~30 minutes on my NumWorks calculator
# Features :
#  - Convert from base 10 to base 2 and base 16 in a nice looking output

def y(x):
  i=0

  while i<x:
    i=i+1
    print(i, bin(i), hex(i))

print("Enter a value for x")

try:
  y(int(input()))
except:
  print("You have entered an incorrect value")
