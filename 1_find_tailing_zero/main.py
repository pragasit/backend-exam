"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:
    
    def find_tailing_zeroes(self, number: int) -> int | str:
        answer = 0
        if number < 0:
            return "Number can not be negative"
        elif number == 0:
            return "Number of last adjacent 0 number : 0"
        else:
            main_number = number
            num = number
            for i in range(number):
                num = num - 1
                if num > 0:
                    main_number = main_number * num
                else:
                    answer = main_number
        count = 0
        while answer % 10 == 0:
            count += 1 
            answer //= 10
        return "Number of last adjacent 0 number : " + str(count)

#Start
def main():
    sol = Solution()
    number = int(input("Enter the factotial number : "))
    print(sol.find_tailing_zeroes(number))
main()