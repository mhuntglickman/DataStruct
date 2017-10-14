# using the builtin list type with append and pop.  This will
# allow me to append to the end and pop from the end which is a 
# faster run time O(1) then appending to front of list and popping 
# from the front O(n)
# Adding some testing information and using this as a push agent for a Jenkins job


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
 

def balanceParen(symbols):
	
	# instaniate a stack
	s=Stacks()
	
	balanced = True
	index=0
	
	#for i in range(len(symbols)) and balanced:
	while index < len(symbols) and balanced:
		
		while index < len(symbols) and balanced:
			symbol = symbols[index]
	        
			if symbol in "([{":
				s.push(symbol)
	        
			else:
				if s.isEmpty():
					balanced = False
				else:
					top = s.pop()
					if not subChecker(top,symbol):
						balanced = False
			# increment the index position
			index+=1


	return True if balanced and s.isEmpty() else False

def subChecker(open, close):

	opens = '([{'
	closers = ')]}'

	return opens.index(open) == closers.index(close)
	



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


print '**************checking balanceParen function**************'

print(balanceParen( '((()))' ))
print(balanceParen( '(()' ))

print '**************checking Extended balanceParen function**************'

print(balanceParen( '{{([][])}()}' ))
print(balanceParen( '[{()]' ))


