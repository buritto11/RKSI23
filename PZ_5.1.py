#Составить функцию, которая напечатает сорок любых символов.
import random
def rand1():
  y = 0
  s1 = ''
  s= 'qwery'
  while y<40:
    t = random.randint(0,4)
    print(s[t])
    s1 = s1 + s[t]
    y = y + 1
  return s1
print(rand1())
