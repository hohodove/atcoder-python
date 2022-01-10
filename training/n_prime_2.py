
# cd ~/develop/python-test/traing
# python3 n_prime_2.py 5

import sys

primes = []

def is_prime(num: int) -> bool:
  for p in primes:
    if (num % p) == 0:
      return False
  
  primes.append(num)
  return True


def main(argv):
  index = int(argv[0])

  if index < 1:
    print("invalid arg error")
    return

  count = 0
  num = 1

  while count != index:
    num += 1
    if is_prime(num):
        count += 1
    # print(num, count)

  print(num)
  return

if __name__ == "__main__":
  main(sys.argv[1:])
