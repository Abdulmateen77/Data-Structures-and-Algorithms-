# Define a class to represent nodes in the hashmap
class mapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Define the hashmap class
class map:
    def __init__(self):
        self.bucket_size = 10
        self.bucket = [None for i in range(self.bucket_size)] # Initialize a list of buckets
        self.count = 0

    def size(self):
        return self.count

    def getBucketIndex(self, hc):
        return (abs(hc) % self.bucket_size) # Compute the index of the bucket using the hash code

  def rehash(self):
    # Store the current bucket array in a temporary variable
    temp = self.bucket
    
    # Create a new bucket array with twice the size
    self.bucket = [None for i in range(2 * self.bucketsize)]
    
    # Update the bucketsize to reflect the new size
    self.bucketsize = 2 * self.bucketsize
    
    # Reset the count to zero for the new bucket array
    self.count = 0
    
    # Iterate through the old bucket array and reinsert elements into the new array
    for head in temp:
        while head is not None:
            #Reinsert the key-value pair into the new bucket array using insert method
            self.insert(head.key, head.value)
            head = head.next

def loadFactor(self):
    # Calculate and return the load factor of the hashmap
    return self.count / self.bucketsize

    
    def insert(self, key, value):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.bucket[index] # Get the head of the linked list in the selected bucket
        while head is not None:
            if head.key == key: # Update value if key already exists
                head.value = value
                return
            head = head.next
        head = self.bucket[index] # Reset head to the bucket's head
        newNode = mapNode(key, value) # Create a new node
        newNode.next = head # Attach the new node to the current head
        self.bucket[index] = newNode # Update the head to the new node
        self.count += 1
        leadFactor = self.count / self.bucketsize
        if loadFactor >= 0.7:
            self.rehash()

    def getValue(self, key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.bucket[index] # Get the head of the linked list in the selected bucket
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None

    def remove(self, key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.bucket[index] # Get the head of the linked list in the selected bucket
        prev = None
        while head is not None:
            if head.key == key:
                if prev is None: # If head needs to be removed
                    self.bucket[index] = head.next
                else:
                    prev.next = head.next # If a middle node needs to be removed
                self.count -= 1
                return head.value
            prev = head
            head = head.next
        return None

#Create an instance of the hashmap
hash_map = mao()

#Insert key-value pairs into the hashmap
hash_map.insert("key1", "value1")
hash_map.insert("key2", "value2")
hash_map.insert("key3", "value3")

#Get values using keys
print(hash_map.getValue("key1"))  # Output: value1
print(hash_map.getValue("key2"))  # Output: value2
print(hash_map.getValue("key3"))  # Output: value3

#Remove a key-value pair from the hashmap
removed_value = hash_map.remove("key2")
print("Removed:", removed_value)  # Output: Removed: value2

# Try to get the value for the removed key
print(hash_map.getValue("key2"))  # Output: None

# Test the size of the hashmap
print("Size:", hash_map.size())    # Output: Size: 2
