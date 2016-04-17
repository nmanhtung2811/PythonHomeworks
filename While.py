
n1 = int(input("Enter first integer:"))
n2 = int(input("Enter second integer:"))
k = n1%n2
while k <= n1 and k <= n2:
    if n1 % k == 0 and n2 % k == 0:
        print(k)
    break
    print("the greatest common divisor for", n1, "and", n2, "is", k)
print("Done!")


