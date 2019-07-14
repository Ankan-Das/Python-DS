class Node:
	def __init__(self,data=None):
		self.data = data
		self.next = None
class SLinkedList:
	def __init__(self):
		self.headval = None
	def Atbeginning(self, newdata):
		NewNode = Node(newdata)
		NewNode.next = self.headval
		self.headval = NewNode
	def listprint(self):
		printval = self.headval
		while printval is not None:
			print(printval.data)
			printval = printval.next
	def RemoveNode(self,Removekey):
		Headval = self.headval
		if(Headval is not None):
			if(Headval.data == Removekey):
				self.next = Headval.next
				Headval = None
				return
		while(Headval is not None):
			if Headval.data == Removekey:
				break
			prev = Headval
			Headval = Headval.next
		if(Headval == None):
			return
		prev.next = Headval.next
		Headval = None

llist = SLinkedList()
llist.Atbeginning("Mon")
llist.Atbeginning("Tue")
llist.Atbeginning("Wed")
llist.Atbeginning("Thu")
llist.RemoveNode("Tue")
llist.listprint()
