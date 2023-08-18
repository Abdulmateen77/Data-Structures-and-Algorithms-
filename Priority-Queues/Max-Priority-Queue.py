class PriorityQueueNode:
    def __init__(self, ele, priority):
        self.ele = ele
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.pq = []

    def isEmpty(self):
        #Implement the isEmpty() function here
        return self.getSize() == 0
    
    def getSize(self):
        #Implement the getSize() function here
        return len(self.pq)

    def getMax(self):
        #Implement the getMax() function here
        if self.isEmpty():
            return None
        return self.pq[0].priority
    
    def __procolateUp(self):
        childIndex = self.getSize()-1

        while childIndex > 0:
            parentIndex = (childIndex - 1) // 2
            if self.pq[childIndex].priority > self.pq[parentIndex].priority:
                self.pq[childIndex], self.pq[parentIndex] = self.pq[parentIndex], self.pq[childIndex]
                childIndex = parentIndex

            else:
                break

    def insert(self,ele,priority):
        #Implement the insert() function here
        pqNode = PriorityQueueNode(ele, priority)
        self.pq.append(pqNode)
        self.__procolateUp()
    
    def __procolateDown(self):
        parentIndex = 0
        leftChildIndex = 2 * parentIndex + 1
        rightChildIndex = 2 * parentIndex + 2

        while leftChildIndex < self.getSize():
            maxIndex = parentIndex

            if self.pq[maxIndex].priority < self.pq[leftChildIndex].priority:
                maxIndex = leftChildIndex
            
            if rightChildIndex < self.getSize() and self.pq[maxIndex].priority < self.pq[rightChildIndex].priority:
                maxIndex = rightChildIndex

            if maxIndex == parentIndex:
                break

            self.pq[parentIndex], self.pq[maxIndex] = self.pq[maxIndex], self.pq[parentIndex]

            parentIndex = maxIndex

            leftChildIndex = 2 * parentIndex + 1
            rightChildIndex = 2 * parentIndex + 2 




    def removeMax(self):
        #Implement the removeMax() function here
        if self.isEmpty():
            return None
        ele = self.pq[0].priority
        self.pq[0] = self.pq[self.getSize()-1]
        self.pq.pop()
        self.__procolateDown()

        return ele


myPq = PriorityQueue()
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i=1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i+=1
        myPq.insert(element,element)
    elif choice == 2:
        print(myPq.getMax())
    elif choice == 3:
        print(myPq.removeMax())
    elif choice == 4:
        print(myPq.getSize())
    elif choice == 5:
        if myPq.isEmpty():
            print('true')
        else:
            print('false')
        break
    else:
        pass
    choice = curr_input[i]
    i+=1
