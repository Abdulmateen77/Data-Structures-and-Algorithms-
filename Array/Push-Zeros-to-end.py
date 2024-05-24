// Function to check if a searchElement exists in the given array
function includes(array, searchElement) {
  // Loop through each element in the array
  for (let element of array) {
    // Check if the current element is equal to the searchElement
    if (element === searchElement) {
      // If found, return true
      return true;
    }
  }
  // If the loop completes without finding the element, return false
  return false;
}

//Test cases

// Test case 1: Search for an existing number in an array
const numbers = [1, 2, 3];
console.log(includes(numbers, 1)); // Expected output: true (1 exists in the array)
console.log(includes(numbers, 4)); // Expected output: false (4 does not exist in the array)

// Test case 2: Search in an empty array
const emptyArray = [];
console.log(includes(emptyArray, 1)); // Expected output: false (Empty array contains no elements)
console.log(includes(emptyArray, undefined)); // Expected output: false (Empty array contains no elements)

// Test case 3: Search for an existing string in an array
const strings = ["apple", "banana", "cherry"];
console.log(includes(strings, "banana")); // Expected output: true ("banana" exists in the array)
console.log(includes(strings, "grape")); // Expected output: false ("grape" does not exist in the array)

// Test case 4: Search for various data types in an array
const mixedTypes = [1, "apple", true, null, 42];
console.log(includes(mixedTypes, null)); // Expected output: true (null exists in the array)
console.log(includes(mixedTypes, "apple")); // Expected output: true ("apple" exists in the array)
console.log(includes(mixedTypes, false)); // Expected output: true (false exists in the array)
console.log(includes(mixedTypes, 42)); // Expected output: true (42 exists in the array)
console.log(includes(mixedTypes, "orange")); // Expected output: false ("orange" does not exist in the array)
