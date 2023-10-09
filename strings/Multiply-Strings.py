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


# Test Case 1: Multiply two single-digit numbers
result1 = solution.multiply("2", "3")
print(result1)  # Expected output: "6"

# Test Case 2: Multiply a single-digit number with a multi-digit number
result2 = solution.multiply("9", "123")
print(result2)  # Expected output: "1107"

# Test Case 3: Multiply two multi-digit numbers
result3 = solution.multiply("456", "789")
print(result3)  # Expected output: "359784"
