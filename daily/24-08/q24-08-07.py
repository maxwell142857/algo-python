class Solution:
    def numberToWords(self, num: int) -> str:
        val2char = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
        100: "Hundred",
        1000: "Thousand",
        1000000: "Million",
        1000000000: "Billion"
        }

        def threeDigits(val):
            if val == 0:
                return ''
            if val >= 100:
                ans.append(val2char[val//100])
                ans.append(val2char[100])
            twoDigits(val%100)

        def twoDigits(val):
            if val == 0:
                return 
            if val >= 20:
                ans.append(val2char[val-val%10])
                if val%10 != 0:
                    ans.append(val2char[val%10])
            else:
                ans.append(val2char[val])
        
        ans = []
        values = [10**9,10**6,10**3]
        for i in range(3):
            if num>=values[i]:
                threeDigits(num//values[i])
                ans.append(val2char[values[i]])
                num %= values[i]
        threeDigits(num)
        if not ans:
            return val2char[0]
        else:
            return ' '.join(ans)