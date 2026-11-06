class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        def to_binary(num: int)->str:
            if num == 0: return "0"
            result = ""
            while num > 0:
                bit = num % 2
                result = str(bit) + result
                num = num // 2
            
            return result
        
        def to_decimal(num: str)->int:
            i = 0
            number = 0
            for j in range(len(num) - 1, -1, -1):
                number += int(num[j]) * (2 ** i)
                i += 1
            
            return number
        
        a_num = to_decimal(a)
        b_num = to_decimal(b)

        return to_binary(a_num + b_num)
            
