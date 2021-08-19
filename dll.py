'''
    doubly linked list similar to browser history
'''

class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next =next
        self.prev = prev
        self.data = data

class DLL:
    def __init__(self):
        self.head == None

    def push(self,data):
        newNode = Node(data)
        newNode.next =  self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode

    def insert(self,prev,data):
        if prev_node is None:
            return print('error')

        newNode =  Node(data)
        newNode.next =  prev_node.next
        prev_nose.next = newNode

        if newNode.next:
            newNode.next.prev = newNode

    def append(self,data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next

        last.next = newNode
        newNode.prev = last

        return

    
