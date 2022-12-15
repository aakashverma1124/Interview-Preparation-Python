class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

class DesignLinkedList:

	def __init__(self):
		self.head = None

	def insert_at_beginning(self, data):
		node = Node(data)
		node.next = self.head
		self.head = node

	def insert_at_end_n(self, data):
		node = Node(data)
		if self.head is None:
			self.head = node
		else:
			temp = self.head
			while temp.next is not None:
				temp = temp.next
			temp.next = node

	def delete_node(self, data):
		if self.head == None:
			return -1
		temp = self.head
		if temp.data == data:
			self.head = temp.next
			return data
		prev = temp
		temp = temp.next
		while temp is not None:
			if temp.data == data:
				prev.next = temp.next
				return data
			prev = temp
			temp = temp.next
		return -1

	def print_list(self):
		temp = self.head;
		while temp is not None:
			print(temp.data, end = " -> ")
			temp = temp.next
		print("None")

if __name__ == '__main__':
	ll = DesignLinkedList()
	ll.insert_at_end_n(40)
	ll.insert_at_end_n(50)
	ll.insert_at_beginning(30)
	ll.insert_at_beginning(20)
	ll.insert_at_beginning(10)
	ll.print_list()
	ll.delete_node(30)
	ll.print_list()