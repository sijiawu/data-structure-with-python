class Stack:
	#the stack class
	def __init__(self): 
		self.items = []
	def push(self,item):
		self.items.append(item)
	def isEmpty(self):
		if self.items == []:
			return True
		else: 
			return False

myStack = Stack()
print(myStack.isEmpty)
myStack.push("Bob")
myStack.push("Charles")
print(myStack.isEmpty)