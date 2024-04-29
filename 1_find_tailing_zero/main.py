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
        ans = 0
        if number < 0:
            return "number can not be negative"
        else:
            n = number   ## 7
            num = number
            for i in range(number): ## count 7 
                # print("font",n)
                num = num-1
                if num > 0:

                    # print("n",n)
                    # print("num",num)
                    n = n*num
                    # print("Back",n)
                else:
                    ans = n
        count = 0
        while ans % 10 == 0:
            count += 1 
            ans //= 10
        return count

#Start
def main():
    sol = Solution()
    num = int(input())
    print(sol.find_tailing_zeroes("",num))
main()