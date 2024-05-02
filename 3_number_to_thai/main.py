"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:
    def __init__(self):
        # number to thai
        self.numbers = {
            0: 'ศูนย์', 1: 'หนึ่ง', 2: 'สอง', 3: 'สาม', 4: 'สี่',
            5: 'ห้า', 6: 'หก', 7: 'เจ็ด', 8: 'แปด', 9: 'เก้า'
        }
        # digit to thai
        self.places = {1: '', 10: 'สิบ', 100: 'ร้อย', 1000: 'พัน', 10000: 'หมื่น', 100000: 'แสน', 1000000: 'ล้าน'}

    def number_to_thai(self, number: int) -> str:
        if number == 0:
            return self.numbers[number]
        
        if not (0 < number < 10_000_000):
            return "number can not less than 0 or greater than 10,000,000"
        
        thai_number = []
        for place in [1000000, 100000, 10000, 1000, 100, 10, 1]:
            digit = number // place
            number %= place
            if digit > 0:
                if digit == 1 and place == 10:
                    thai_number.append(self.places[place])
                elif digit == 2 and place == 10:
                    thai_number.append("ยี่สิบ")
                else:
                    thai_number.append(self.numbers[digit])
                    thai_number.append(self.places[place])
            str1 = ""
            for i in thai_number:
                str1 += i
        return "Convert numbers to Thai: " + str1

def main():
    sol = Solution() 
    number = input("Enter a positive number (0-10,000,000): ")
    number = int(number.replace(",", ""))
    print(sol.number_to_thai(number))
main()

