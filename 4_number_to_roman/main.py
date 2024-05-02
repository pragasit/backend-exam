"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def __init__(self):
        self.numbers = {
            1: 'I', 4: 'IV', 5: 'V',9: 'IX', 
            10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 
            100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 
            1000: 'M'
        }
    def number_to_roman(self, number: int) -> str:
        if number < 0:
            return "Number can not less than 0"
        number_roman = ""
        for i in sorted(self.numbers.keys(), reverse=True):
            count = number // i
            number_roman += self.numbers[i] * count
            number %= i
        return "Roman number: " + number_roman



def main():
    sol = Solution()
    num = int(input())
    print(sol.number_to_roman(num))
main()