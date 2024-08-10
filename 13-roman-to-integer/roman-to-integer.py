class Solution:
    def romanToInt(self, s: str) -> int:
        self.s = s
        translations = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        integer = 0
        self.s = self.s.replace("IV","IIII").replace("IX","VIIII")
        self.s = self.s.replace("XL","XXXX").replace("XC","LXXXX")
        self.s = self.s.replace("CD","CCCC").replace("CM","DCCCC")
        for i in self.s:
            integer += translations[i]       
        return integer

        # roman_map = {
        #     'I': 1,
        #     'V': 5,
        #     'X': 10,
        #     'L': 50,
        #     'C': 100,
        #     'D': 500,
        #     'M': 1000
        # }
        
        # total = 0
        # prev_value = 0
        
        # for char in reversed(s):
        #     current_value = roman_map[char]
            
        #     # If the current value is less than the previous value, subtract it
        #     if current_value < prev_value:
        #         total -= current_value
        #     else:
        #         total += current_value
            
        #     prev_value = current_value
        
        # return total
        