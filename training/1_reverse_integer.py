# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.

def solution(num: int) -> int:
  string = str(num)
  if num >= 0:
    return int(string[::-1])
  else:
    return int("-" + string[:0:-1])

print(solution(-123))
print(solution(123))
