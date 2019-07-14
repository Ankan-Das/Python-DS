class Node:
	def  __init__(self,dataval=None):
		self.dataval = dataval
		self.nextval = None
class SLinkedList:
	def __init__(self):
		self.headval = None
	def AtEnd(self, newdata):
		NewNode = Node(newdata)
		if self.headval is None:
			self.headval = NewNode
			return
		laste = self.headval
		while laste.nextval is not None:
			laste = laste.nextval
		laste.nextval = NewNode
	def listprint(self):
		printval = self.headval
		while printval is not None:
			print(printval.dataval)
			printval = printval.nextval


list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list.headval.nextval = e2
e2.nextval = e3

list.AtEnd("Thu")

list.listprint()
