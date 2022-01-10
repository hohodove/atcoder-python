
# cd ~/develop/python-test/training
# python3 n_prime.py 5

import sys

def main(argv):
  index = int(argv[0])

  count = 1
  num = 2

  while count != index:
    num += 1
    # print(num, count)
    for i in range(2,num):
      if (num % i) == 0:
        break
    else:
      count += 1

  print(num)
  return

if __name__ == "__main__":
  main(sys.argv[1:])
