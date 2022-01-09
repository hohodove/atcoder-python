class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        s = s[::-1]

        num = 0
        mae = ""
        for i in s:
          if i == "I" and (mae == "V" or mae == "X"):
            num -= 1
            mae = i
            continue
          elif i == "X" and (mae == "L" or mae == "C"):
            num -= 10
            mae = i
            continue
          elif i == "C" and (mae == "D" or mae == "M"):
            num -= 100
            mae = i
            continue
          num += dic[i]
          mae = i

        return num

if __name__ == '__main__':
    solution = Solution()
    print(solution.romanToInt("MCMXCIV"))
