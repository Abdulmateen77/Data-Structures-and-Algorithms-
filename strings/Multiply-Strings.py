# Define a class named Solution, which will contain a method called multiply.
class Solution:
    # The multiply method takes two string arguments, num1 and num2, and returns a string.
    def multiply(self, num1: str, num2: str) -> str:
        # Convert the first input string, num1, to an integer and store it in the variable firstInt.
        firstInt = int(num1[:])

        # Convert the second input string, num2, to an integer and store it in the variable SecondInt.
        SecondInt = int(num2[:])

        # Calculate the product of the two integers, firstInt and SecondInt, and store it in productofStr.
        productofStr = firstInt * SecondInt

        # Convert the product back to a string and return it using an f-string.
        return f"{productofStr}"
