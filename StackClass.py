# using the builtin list type with append and pop.  This will
# allow me to append to the end and pop from the end which is a 
# faster run time O(1) then appending to front of list and popping 
# from the front O(n)

class Stacks():

	def __init__(self):
		self.items=[]

	def isEmpty(self):
		return self.items==[]

	def push(self,item):
		return self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)



s=Stacks()
s.push('one')
s.push(2)
s.push('trees')
s.push('phones')
s.push(3)
print s.items
print s.size()
print s.pop()
print s.pop()
print s.peek()
print s.size()
print s.items