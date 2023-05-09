class node:
    def __init__(self,value):
        self.value = value
        self.next = None

class linkedlist:
    def __init__(self,value):
        new_node = node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self,value):
        new_node = node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True 
    def maxValue(self):
        temp = self.head
        max = temp.value
        while temp is not None:
            if temp.value > max:
                max = temp.value
            temp = temp.next
        return max
    
    def append_list(self,list):
        for value in list:
            self.append(value)
        return True
            
            

ll = linkedlist(3)
ll.append(10)
ll.append_list([2,4,8,6])
print(f"max value is {ll.maxValue()}")
ll.print_list()