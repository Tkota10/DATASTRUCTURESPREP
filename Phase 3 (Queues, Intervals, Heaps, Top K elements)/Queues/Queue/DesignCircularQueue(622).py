class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode

class MyCircularQueue(object):

    def __init__(self, k):
        
        self.capacity = k
        self.head = None
        self.tail = None
        self.count = 0
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.capacity == self.count:
            return False
        
        #Insert the value into the queues

        if self.count == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            #Might have to make the newNode = Node(value)
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self.count += 1
        return True

    def deQueue(self):
        """
        :rtype: bool
        """

        if self.count == 0:
            return False

        self.head = self.head.next
        self.count -= 1
        return True
        

    def Front(self):
        """
        :rtype: int
        """
        
        if self.count == 0:
            return -1
        
        return self.head.value

    def Rear(self):
        """
        :rtype: int
        """
        if self.count == 0:
            return -1
        
        return self.tail.value
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.count == 0:
            return True
        else:
            False
        

    def isFull(self):
        """
        :rtype: bool
        """
        if self.count == self.capacity:
            return True
        else:
            return False