
class Linklist:
    def __init__(self) -> None:
        self.head = None
        self.size = 0
        self.max = None
        self.min = None

    #  add a node with value x at the head of a list.
    def addToHead(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size = self.size + 1
        
    # add a node with value x at the tail of a list.
    def addToTail(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.size = self.size + 1

    # add a node with value x before the node p
    def addBefore(self, new_node, index):
        current = self.head
        pos = 1
        while pos < index - 1:
            current = current.next
            pos += 1
        after = current.next
        current.next = new_node
        new_node.next = after
        self.size = self.size + 1

        
        
    # add a node with value x after the node p.
    def addAfter(self, new_node, index):
        pos = 1
        current = self.head
        while pos < index:
            current = current.next
            pos += 1
        after = current.next
        current.next = new_node
        new_node.next = after
        self.size += 1

        
    # delete the head and return its info.
    def deleteFromHead(self):
        current = self.head
        self.head = current.next
        current.next = None

    # delete the tail and return its info
    def deleteFromTail(self):
        current = self.head
        after = current.next
        while after.next is not None:
            current = current.next
            after = after.next
        current.next = None
        self.size = self.size - 1

    # delete the node after the node p and return its info.
    def deleteAter(self, index):
        pass

    # delele the first node whose info is equal to x.
    def Delete_firstnode_data(self, data):
        current = self.head
        while current:
            if current.data == data:
                break
            prev = current
            current = current.next
        if current == self.head:
            current = self.head
            self.head = current.next
            current.next = None
        else:
            after = current.next
            prev.next = after
            current.next = None
        self.size = self.size - 1
        

    # search and return the reference to the first node having info x
    def search(self, data):
        current = self.head
        pos = 1
        while current:
            if current.data == data:
                return pos
            else:
                pos += 1
                current = current.next
        return None

    # count and return number of nodes in the list.
    def count(self):
        return self.size
    

    
    def Delete_node_th(self, index):
        if self.size < index:
            print("no existing")
        else:
            pass
            
    # sorting list
    def sort(self):
        for i in range(self.size - 1, 0, -1):
            tmp = self.head
            for j in range(i):
                if int(tmp.data) > int(tmp.next.data):
                    temp = tmp.data
                    tmp.data = tmp.next.data
                    tmp.next.data = temp
                tmp = tmp.next


    def delete_node_data(self, data):
        current = self.head
        while current:
            if current.data == data:
                break
            current = current.next
            

    # create and return array containing info of all nodes in the list.
    def toArray(self):
        list_info = []
        current = self.head
        while current:
            list_info.append(current.data)
            current = current.next
        return list_info

    # max value of the linked list
    def Max(self):
        current = self.head
        max = int(current.data)
        while current.next is not None:
            if max < int(current.data):
                max = int(current.data)
            current = current.next
        return max

    # min of the linklist
    def Min(self):
        current = self.head
        min = int(current.data)
        while current.next is not None:
            if min > int(current.data):
                min = int(current.data)
            current = current.next
        return min

    def Sum(self):
        current = self.head
        sum = 0
        while current: 
            try:
                current.data = int(current.data)
            except: 
                pass
            else:
                sum += current.data
            current = current.next
        return sum
    
    # return the average of all values in the list.
    def avg(self, sum): 
        return sum / self.size
    

    # check sorted
    def sorted(self) -> bool:
        current = self.head
        while current.next is not None:
            if int(current.data) > int(current.next.data):
                return False
            current = current.next
        return True
    

    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next

