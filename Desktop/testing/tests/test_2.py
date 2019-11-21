def product(n):
  total = 1
  for i in n:
    total += i
  return total
cool = str(input("Enter a number to find something cool: "))
print (product(cool))
