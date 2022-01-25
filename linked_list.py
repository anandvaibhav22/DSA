class Node():
	def __init__(self,data =None):
		self.data = data
		self.next = None

class LL():
	def __init__(self):
		self.head = None

	def print_ll(self):
		print(self.head.data)
		copy = self.head
		while(copy.next) != None:
			copy = copy.next
			print(copy.data)

	def len_ll(self):
		count = 1
		copy = self.head
		while(copy.next) != None:
			copy = copy.next
			count += 1
		print(count)

	def insert_head(self):
		e_new = Node("Sun")
		e_new.next = self.head
		self.head = e_new

	def insert_tail(self):
		e_tail = Node("Thu")
		copy = self.head
		while(copy.next) != None:
			copy = copy.next
		copy.next = e_tail

	def find_middle_node(self):
		fast = self.head
		slow = self.head
		while (fast.next != None and fast.next.next != None):
			fast = fast.next.next
			slow = slow.next
		return slow

	def insert_at_middle_LL(self):
		middleNode = self.find_middle_node()
		nexttomiddle = middleNode.next
		new_node = Node("Holiday")
		new_node.next = nexttomiddle
		middleNode.next = new_node


 
object_id = LL()
object_id.head = Node()
object_id.head.data = "Mon"
e2 = Node("Tue")
object_id.head.next = e2
print(object_id.head.data)
e3 = Node("Wed")
e2.next= e3
print(e2.data)
print(e2.next)

object_id.print_ll()
object_id.len_ll()
object_id.insert_head()
object_id.insert_tail()
print(object_id.find_middle_node())
object_id.insert_at_middle_LL()
object_id.print_ll()
