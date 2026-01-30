class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"Node => {self.data}"


A = Node('Monday')
B = Node('Tuesday')
C = Node('Wednesday')
#
# A.next = B
# B.next = C

class LinkedList:
    def __init__(self):
        self.head = None
        


    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return ""

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        return ""


    def display(self):
        if self.head is None:
            print("LList is empty")
            return ""

        current = self.head
        while current:
            print(current.data)
            current = current.next

        return ""

    def prepend(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return ""

        new_node.next = self.head
        self.head = new_node
        return ""

    def insert(self,old_node,new_node, data):
        if old_node is None:
            print("Old node mavjud emas")
            return

        new_node = Node(data)
        new_node.next = old_node.next
        old_node.next = new_node

    def delete(self, data):
        if self.head is None:
            print("LList is empty")
            return ""

        if self.head.data == data:
            self.head = self.head.next
            return ""

        current = self.head
        prev = None

        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:
            print("Bunday element topilmadi")
            return ""

        prev.next = current.next
        return ""









linked_list = LinkedList()

linked_list.append('Monday')
linked_list.append('Tuesday')
linked_list.append('Wednesday')
linked_list.prepend('Sunday')

# print(linked_list.head)

print(linked_list.display())
