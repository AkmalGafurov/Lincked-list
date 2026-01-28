class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_all(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")



ll = LinkedList()
ll.append(40)
ll.append(50)
ll.append(55)
ll.append(60)

ll.print_all()



# Stack LIFO
stack = []


stack.append(10)
stack.append(50)
stack.append(90)


print(stack.pop())   
print(stack)         



# Queue FIFO
from collections import deque

queue = deque()


queue.append(10)
queue.append(20)
queue.append(30)


print(queue.popleft())  
print(queue)            
