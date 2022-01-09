from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_word = strs[0]
        for word in strs:
          if len(word) < len(shortest_word):
            shortest_word = word          

        for i in range(len(shortest_word)-1, -1, -1):
          for word in strs:
            flag = True
            if not (shortest_word[:i+1] == word[:i+1]):
              flag = False
              break
          if flag:
            return shortest_word[:i+1]

        return ""

if __name__ == "__main__":
    solution = Solution()
    strs = ["a"]
    print(solution.longestCommonPrefix(strs))
