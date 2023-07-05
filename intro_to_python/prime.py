def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True

min = int(input("entre un nombre superieur ou égal à 2: "))
max = int(input("entre un nombre plus grand: "))
prime=[]

for i in range(min, max+1):
  if is_prime(i):
    prime.append(i)
print(prime)