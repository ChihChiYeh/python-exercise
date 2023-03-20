x = int(input()) # 20

def isPrime(n):
  if n < 2:
  return False
  for i in range(2, int(n**0.5)+1):
  if n % i == 0:
  return False
  return True

def primes(n):
  f = []
  for i in range(2, n):
  if isPrime(i):
    f.append(i)
  return f

f = primes(n)
print(f)
