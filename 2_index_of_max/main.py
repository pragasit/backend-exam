"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 4

[Example 2]
input = []
output = list can not blank
"""


class Solution:
    def find_max_index(self, numbers: list) -> int | str:
        if not numbers:
            return "list can not blank"
        num = numbers[0]
        for i in numbers:
            if num <= i:
                num = i
        return "Index of maximum number in list : " + str(num)

def main():
    sol = Solution()
    input_str = input("Enter a list of number : ")
    list_number = eval(input_str)
    print(sol.find_max_index(list_number))
main()