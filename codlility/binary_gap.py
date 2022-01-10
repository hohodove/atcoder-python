# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
  # write your code in Python 3.6
  strings = bin(N)[2:]

  ones = []
  for i, s in enumerate(strings):
    if s == '1':
      ones.append(i)

  max_gap = 0
  for i in range(len(ones)-1):
    if (ones[i+1] - ones[i])-1 > max_gap:
      max_gap = ones[i+1] - ones[i] - 1

  return max_gap

print(solution(9))
print(solution(1041))
print(solution(32))
