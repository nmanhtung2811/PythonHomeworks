'''print("Hello Ta Thu Hang")
name = "Tung"
age = 34
print("My name is %s. I am %d" % (name, age))

primeNum = [1, 2, 3, 5, 7, 11, 13, 15, 17, 19]
i = 1
for prime in primeNum:
    print("%2d  %2d" % (i, prime))
    i +=1'''
'''for i in range(1, 10):
    print(i, '  ', end='')
for j in range(1,10):
    print(j,'|')'''
'''i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print(i, " is prime")
   i = i + 1
print("Good bye!")'''

numbers = [1, 2, 5, 6, 8, 9, 10, 15]
i = 1
for num in numbers:
    print('%2d la %2d' % (i, num))
    i +=1


