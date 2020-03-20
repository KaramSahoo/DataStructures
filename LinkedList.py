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
		self.size+=1

	def append(self, data):
		last = self.head
		while last.next is not None:
			last = last.next
		last.next = Node(data, None)
		self.size+=1

	def delete_front(self):
		if self.is_empty() is False:
			value = self.head.data
			self.head = self.head.next
			return value

	def delete_last(self):
		if self.is_empty() is False:
			if self.head.next is None:
				return self.delete_front()
			second_last = self.head
			value = second_last.next.data
			while second_last.next.next is not None:
				second_last = second_last.next
				value = second_last.next.data
			second_last.next = None
			return value


	def display(self):
		if self.is_empty() is False:
			temp = self.head
			while temp is not None:
				print(temp.data)
				temp = temp.next

	def is_empty(self):
		if self.size == 0:
			print("LinkedList is empty!")
			return True
		return False

l1 = LinkedList()
l1.display()
l1.delete_front()
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
print("Deleted value is : ", l1.delete_front())
print("Deleted value is : ", l1.delete_last())
l1.display()
