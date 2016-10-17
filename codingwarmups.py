"""Google Coaching Call example questions / Glickman

	>>> sum_checker([5,3], 9)
	False

	>>> sum_checker([5,4,2,4], 8)
	True


    """

# this is a more elegant approach
def sum_checker(check_lst=[], sum_to=0):

	# we need the list to be more than one element long.
	if len(check_lst) <= 1:	# This is O(1) because it is a onetime comparision
		return False
	

	#myDict = dict.fromkeys(check_lst,None)
	myCheck = {}
	
	for item in check_lst:	# this is O(n) at worst because we would have to iterate through entire list
		
		if myCheck.has_key(sum_to - item):  # Check for corresponding item in dict and because this is a dictionary lookup runtime is O(1)
			return True		#break out of function and return True 
			
		myCheck[item]=None  # Insert the key and because this is a dictionary insert runtime is O(1)

	return False	

# this is more of a brute force method
def sum_checker2(check_lst=[],sum_to=0):
	if len(check_lst) <=1:
		return False

		
	for i in range(len(check_lst)):

		# check for memberbership in first part of list up to but not including the element
		if (sum_to-i) in check_lst[0:i]:
			return True
		
		#check for membership in second part of list not including the element itself
		elif (i+1)<len(check_lst):
			if (sum_to-i) in check_lst[i+1:]:
				return True

	# exhaust the list with no match return false
	return False

##########################################
if __name__ == "__main__":
	import doctest
	doctest.testmod()

print (sum_checker([3,5,8,9], 8))
print (sum_checker([4,8,6,6], 12))
print (sum_checker([5,8,5,5], 15))
print (sum_checker([3,6,9,10,5,7,3], 20))
print (sum_checker([],10))
print (sum_checker([3,4],))




