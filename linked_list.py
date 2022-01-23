class Node():
	def __init__(self,data =None):
		self.data = data
		self.next = None

class LL():
	def __init__(self):
		self.head = None

	def 



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