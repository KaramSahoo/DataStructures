class Node:
	def __init__(self, data, next):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None
		self.size = 0

	def push(self, data):
		self.head = Node(data, self.head)

	def append(self, data):
		last = self.head
		while last.next is not None:
			last = last.next
		last.next = Node(data, None)

	def display(self):
		temp = self.head
		while temp is not None:
			print(temp.data)
			temp = temp.next

l1 = LinkedList()
l1.push(1)
l1.push(2)
l1.push(3)
l1.push(4)
l1.push(5)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
l1.display()