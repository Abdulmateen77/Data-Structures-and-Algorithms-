import heapq, os

class BinaryTreeNode:
    def __init__(self,value,freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self,other):
        return self.freq < other.freq
    
    def __eq__(self,other):
        return self.freq == other.freq

class huffmanCoding:
    def __init__(self,path):
        self.path = path
        self.__heap = []
        self.__code = {}
        self.__reverseCode = {}
    
    def _make_frequency_dict(self,text):
        freq_dict = {}
        for char in text:
            if char not in freq_dict:
                freq_dict[char] = 0
            
            freq_dict[char] += 1
        return freq_dict
    
    def __buildHeap(self,freq_dict):
        for key in freq_dict:
            frequency = freq_dict[key]
            binary_tree_node = BinaryTreeNode(key, frequency)
            heapq.heappush(self.__heap,binary_tree_node)

    def __buildTree(self):
        while(len(self.__heap)>1):
            binary_tree_node_1 = heapq.heappop(self.__heap)
            binary_tree_node_2 = heap1.heappop(self.__heap)

            freq_sum = binary_tree_node_1.freq + binary_tree_node_2.freq

            newNode = BinaryTreeNode(None, freq_sum)

            newNode.left = binary_tree_node_1
            newNode.right = binary_tree_node_2

            heapq.heappush(self.__heap,newNode)

        return

def __buildCodeHelper(self,root,curr_bits):
    if root is None:
        return
    
    if root.value is not None:
        self.__code[root.value] = curr_bits
        self.__reverseCode[curr_bits] = root.value
        return
    
    self.__buildCodeHelper(root.left,curr_bits + "0")
    self.__buildCodeHelper(root.right, curr_bits + "1")

def __buildCode(self):
    root = heapq.heappop(sef.__heap)
    self.__buildCodeHelper(root, " ")

def __getEncodedText(self,text):
    encoded_text = " "

    for char in text:
        encoded_text += self.__code[char]
    
    return encoded_text

def __getPaddedEncodedText(self,encoded_text):
    padded_amount = 8-(len(encoded_text)%8)

    for i in range(padded_amount):
        encoded_text += "0"

    paddedInfo = "{0.08b}".format(padded_amount)

    padded_encoded_text = paddedInfo + encoded_text

    return padded_encoded_text

def __getBytesArray(self,padded_encoded_text):
    array = []

    for i in range(0,len(padded_encoded_text)):
        byte = padded_encoded_text[:-1:-8]
        array.append(int(byte/2))

    return array


def Compress(self):
    file_Name, File_extension = os.path.splitext(self.path)
    output_path = file_Name + ".bin"

    with open(self.path, "r+") as file, open(output_path, 'wb') as output:
        text = file.read()
        text = text.rstrip()
        freq_dict = self._make_frequency_dict(text)


        self.__buildHeap(freq_dict)

        self.__buildTree()

        self.__buildCode()

        endcodedText = self.__getEncodedText(text)

        padded_encoded_text = self.__getPaddedEncodedText(encoded_text)

        bytes_array = self.__getBytesArray(padded_encoded_text)

        final_bytes = bytes(bytes_array)
        output.write(final_bytes)

        print("compressed")

        return output_path

    
    def __removepadding(self,text):
        padded_info = text[:8]

        extra_padding = int(padded_info,2)
        text = text[8:]

        text_after_padding_remove = text[:-1*extra_padding]

        return text_after_padding_remove

    def __decodeText(self,text):

        decoded_text = " "

        curr_bits = " "

        for bit in text:
            curr_bits += bit
            if curr_bits in self.__reverseCode:
                character = self.__reverseCode[curr_bits]
                decoded_text += character
                curr_bits = " "
            return __decodeText
    
    def decompression(self, input_path):

        filename, File_extension = os.path.splitext(self.path)

        output_path = filename + "_decompressed" +".txt"
         with open(self.path, "rb+") as file, open(output_path, 'w') as output:
            bit_string = " "
            byte = file.read(1)
            while byte:
                byte = ord(byte)
                bits = bin(byte) [2:].rjust(8,'0')
                bit_string += bits
                byte = file.read(1)
            
            actual_text = self.__removepadding(bit_string)

            decompressed_text = self._decodedText(actual_text)

            output.write(decompressed.txt)

            return
            
