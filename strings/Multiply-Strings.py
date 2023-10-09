class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        firstInt = int(num1[:])
        SecondInt = int(num2[:])
        
        productofStr = firstInt * SecondInt

        return f"{productofStr}"
