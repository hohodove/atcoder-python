class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")":"(",
                    "]":"[",
                    "}":"{"}
        strings = []

        for ope in s:
          # print(strings)
          if (ope == "(") or (ope == "[") or (ope == "{"):
            strings.append(ope)
          if (ope == ")") or (ope == "]") or (ope == "}"):
            if strings == []:
              return False
            if strings.pop() != brackets[ope]:
              return False

        if len(strings) != 0:
          return False

        return True

if __name__ == "__main__":
  solution = Solution()
  inputs = "()[]{}"
  print(solution.isValid(inputs))