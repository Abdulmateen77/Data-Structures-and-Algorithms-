#Import necessary modules
import heapq, os


#Define a BinaryTreeNode class for the Huffman tree nodes
class BinaryTreeNode:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq
    
    def __eq__(self, other):
        return self.freq == other.freq

# Define the Huffman Coding class
class huffmanCoding:
    def __init__(self, path):
        self.path = path
        self.__heap = []  # Priority queue for Huffman tree nodes
        self.__code = {}  # Dictionary to store Huffman codes
        self.__reverseCode = {}  # Dictionary to map codes to characters
    
    # Helper function to create a frequency dictionary from input text
    def _make_frequency_dict(self, text):
        freq_dict = {}
        for char in text:
            if char not in freq_dict:
                freq_dict[char] = 0
            freq_dict[char] += 1
        return freq_dict
    
    # Build a heap (priority queue) from the frequency dictionary
    def __buildHeap(self, freq_dict):
        for key in freq_dict:
            frequency = freq_dict[key]
            binary_tree_node = BinaryTreeNode(key, frequency)
            heapq.heappush(self.__heap, binary_tree_node)

    # Build the Huffman tree
    def __buildTree(self):
        while len(self.__heap) > 1:
            binary_tree_node_1 = heapq.heappop(self.__heap)
            binary_tree_node_2 = heap1.heappop(self.__heap)  # Typo, should be self.__heap

            freq_sum = binary_tree_node_1.freq + binary_tree_node_2.freq

            newNode = BinaryTreeNode(None, freq_sum)

            newNode.left = binary_tree_node_1
            newNode.right = binary_tree_node_2

            heapq.heappush(self.__heap, newNode)

    # Helper function to recursively build Huffman codes
    def __buildCodeHelper(self, root, curr_bits):
        if root is None:
            return
        if root.value is not None:
            self.__code[root.value] = curr_bits
            self.__reverseCode[curr_bits] = root.value
            return
        self.__buildCodeHelper(root.left, curr_bits + "0")
        self.__buildCodeHelper(root.right, curr_bits + "1")

    # Build Huffman codes
    def __buildCode(self):
        root = heapq.heappop(self.__heap)
        self.__buildCodeHelper(root, " ")

    # Encode input text using Huffman codes
    def __getEncodedText(self, text):
        encoded_text = " "
        for char in text:
            encoded_text += self.__code[char]
        return encoded_text

    # Add padding to the encoded text to make its length a multiple of 8
    def __getPaddedEncodedText(self, encoded_text):
        padded_amount = 8 - (len(encoded_text) % 8)
        for i in range(padded_amount):
            encoded_text += "0"
        paddedInfo = "{0:08b}".format(padded_amount)
        padded_encoded_text = paddedInfo + encoded_text
        return padded_encoded_text

    # Convert the padded encoded text to bytes
    def __getBytesArray(self, padded_encoded_text):
        array = []
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i+8]
            array.append(int(byte, 2))
        return array

    # Compress the input text and save it to a binary file
def Compress(self):
    # Extract the file name and extension from the provided path
    file_Name, File_extension = os.path.splitext(self.path)
    
    # Define the output path for the compressed binary file
    output_path = file_Name + ".bin"
    
    # Open the input text file for reading and the output binary file for writing
    with open(self.path, "r+") as file, open(output_path, 'wb') as output:
        # Read the content of the input text file into 'text' variable
        text = file.read()
        
        # Remove trailing whitespace from the text
        text = text.rstrip()
        
        # Create a frequency dictionary for the characters in the text
        freq_dict = self._make_frequency_dict(text)
        
        # Build a priority queue (heap) from the frequency dictionary
        self.__buildHeap(freq_dict)
        
        # Build the Huffman tree using the heap
        self.__buildTree()
        
        # Generate Huffman codes for each character in the text
        self.__buildCode()
        
        # Encode the input text using the generated Huffman codes
        encodedText = self.__getEncodedText(text)
        
        # Add padding to the encoded text to ensure its length is a multiple of 8
        padded_encoded_text = self.__getPaddedEncodedText(encodedText)
        
        # Convert the padded encoded text into a bytes array
        bytes_array = self.__getBytesArray(padded_encoded_text)
        
        # Convert the bytes array into bytes and write it to the output binary file
        final_bytes = bytes(bytes_array)
        output.write(final_bytes)
        
        # Print a message indicating that compression is complete
        print("compressed")
        
        # Return the path to the compressed binary file
        return output_path

            return output_path

    # Helper function to remove padding from the encoded text
    def __removepadding(self, text):
        padded_info = text[:8]
        extra_padding = int(padded_info, 2)
        text = text[8:]
        text_after_padding_remove = text[:-1 * extra_padding]
        return text_after_padding_remove

    # Helper function to decode the encoded text
    def __decodeText(self, text):
        decoded_text = " "
        curr_bits = " "
        for bit in text:
            curr_bits += bit
            if curr_bits in self.__reverseCode:
                character = self.__reverseCode[curr_bits]
                decoded_text += character
                curr_bits = " "
        return decoded_text

    # Decompress the binary file and save the decompressed text to a text file
    def decompression(self, input_path):
        filename, File_extension = os.path.splitext(self.path)
        output_path = filename + "_decompressed" + ".txt"
        with open(self.path, "rb+") as file, open(output_path, 'w') as output:
            bit_string = " "
            byte = file.read(1)
            while byte:
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = file.read(1)
            actual_text = self.__removepadding(bit_string)
            decompressed_text = self.__decodeText(actual_text)
            output.write(decompressed_text)
            return
