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


def balanceParen(symbols):
	
	# instaniate a stack
	s=Stacks()
	
	balanced = True
	index=0
	
	#for i in range(len(symbols)) and balanced:
	while index < len(symbols) and balanced:
		
		symbol = symbols[index]
		

		# if left paren push it into the stack.
		if symbol == '(':
			s.push(symbol)
			
		# anything other than left paren
		else:
			# check if there is anything in the stack to match up with right paren
			if s.isEmpty():
				# if the stack was empty then set balanced to False and bounce out of the loop
				balanced=False
			else:
				# stack still has items in it therefore pop a paren off and 
				# bind it to variable.  Send the popped item and the symbol 
				# in the findMatching method.
				paren = s.pop()
				if not findMatching(paren, symbol)

		# increment the index position
		index+=1


	return True if balanced and s.isEmpty() else False


def findMatching(open, close):
	opener='([{'
	closer = ')]}'

	return opener.index[open] == closer.index[close]

		



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


print '***************checking balanceParen function***************'
print(balanceParen('((()))'))
print(balanceParen('(()'))



