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
    
