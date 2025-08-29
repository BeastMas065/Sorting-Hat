Gryffindor = 0
Slytherin = 0
Ravenclaw = 0
Hufflepuff = 0

print("Q1. dawn or dusk")
a = int(input("1 for dawn, 2 for dusk : "))
if a == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif a == 2:
  Slytherin += 1
  Hufflepuff += 1
else :
  print("meh")

print("Q2.how do you want to be remembered?")
b = int(input("1 for good, 2 for great, 3 for wise, 4 for bold : "))

if b == 1:
  Hufflepuff += 2
elif b == 2:
  Slytherin += 2
elif b == 3:
  Ravenclaw += 2
elif b == 4:
  Gryffindor += 2
else:
  print("not fair, do it again")

print("Q3. favourite musical instrument?")
c = int(input('1 for violin, 2 for trumpet, 3 for piano, 4 for drum : '))
if c == 2:
  Hufflepuff += 4
elif c == 1:
  Slytherin += 4
elif c == 3:
  Ravenclaw += 4
elif c == 4:
  Gryffindor += 4
else:
  print("not fair, do it again")
  
print("houses:")
print("Gryffindor =", Gryffindor)
print("Ravenclaw =", Ravenclaw)
print("Hufflepuff =", Hufflepuff)
print("Slytherin =", Slytherin)
