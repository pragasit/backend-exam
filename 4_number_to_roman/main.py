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
            1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
            6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 
            40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 
            400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
        }
    def number_to_roman(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"
        # num_digit = list(str(number))
        # num_digit = list(map(int, num_digit))
        number_roman = ""
        for i in sorted(self.numbers.keys(), reverse=True):
            count = number // i
            number_roman += self.numbers[i] * count
            number %= i
            # number_roman += self.numbers[i]
        return number_roman
        # for place in [10, 1]:
        #     digit = number // place
        #     number %= place
        #     if digit > 0:
        #         if place == 10 and digit == 1:
        #             number_roman.append(self.places[10])
        #         else:
        #             number_roman.append(self.numbers[digit])
        # str1 = ""
        # for i in number_roman:
        #     str1 += i
        # return str1



def main():
    sol = Solution()
    num = int(input())
    print(sol.number_to_roman(num))
main()