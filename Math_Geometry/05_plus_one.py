class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        one, i = 1, len(digits) - 1
        while one:
            if i >= 0:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.insert(0, 1)
                one = 0
            i -= 1
        return digits
