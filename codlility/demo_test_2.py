# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
  backet = [0]*(len(A)+1)

  for num in A:
    if 0 < num <= len(A):
      backet[num] += 1
  
  for i in range(len(A)):
    if backet[i+1] == 0:
      return i+1
  else:
    if A:
      return i+2

  return 1

print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1, 2, 3]))
print(solution([-1, -3]))
print(solution([0]))
print(solution([3, 6, 4, 2]))
