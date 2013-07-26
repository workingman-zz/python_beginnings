class OddNumbers(object):
	"""This is a class of odd numbers between 1 and 50"""
	
	LIMIT = 1000000

	def __init__(self, a, b):
		print " I just called the init"
		self.odd_number_list = self.make_list(a, b, self.LIMIT)
		self.another = None


	def make_list(self, a, b, LIMIT):
		"""Function that makes a list of odd numbers between a and b"""
		print "I just made a list"
		list_a_b = []
		for i in range(a,b + 1):
			if (i % 2 != 0 and i < LIMIT):
				list_a_b.append(i)
		return list_a_b


list1 = OddNumbers(1,50)

print list1.odd_number_list
print list1.another
print list1.LIMIT

