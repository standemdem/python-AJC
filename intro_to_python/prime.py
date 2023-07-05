def is_prime(n):
  for i in range(2,int(n/2)):
    if (n%i) == 0:
      return False
  return True

min = int(input("entre un nombre superieur ou égal à 2: "))
max = int(input("entre un nombre plus grand: "))
prime=[]

for i in range(min, max):
  if is_prime(i):
    prime.append(i)
print(prime)