N, X = map(int, input().split())
A =  [list(map(int, input().split()))[1:] for _ in range(N)]

nums = [1]

for n in range(N):
  nums = [num*A[n][a] for num in nums for a in range(len(A[n]))]

print(nums.count(X))
