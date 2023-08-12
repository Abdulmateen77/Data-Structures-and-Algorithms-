class mapNode:
  def __init__(self,key,value):
    self.key = key
    self.value = value
    self.next = None

class mao:
  def __init__(self):
    self.bucket.size=10
    self.bucket = [None for i in range(self.bucketsize)]
    self.count = 0

  def size(self):
    return self.count

  def getBucketIndex(self,hc):
    return (abs(hc) % self.bucket)

  def insert(self,key,value):
    hc = hash(key)
    index = self.getBucketIndex(hc)
    head = self.bucket[index]
    while head id not None:
      if head.key == key:
        head.value = value
        return
      head = head.next
    head = self.bucket[index]
    newNode = mapNode(key,value)
    newNode.next = head
    self.bucket[index] = newNode
    self.count += 1
    
