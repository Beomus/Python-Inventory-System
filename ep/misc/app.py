"""
Cool idea might not work so well
"""


import time

ban_list = []

MUN_list = []

class Student:
	"""
	Creating a student class that can call
	borrow(lend) or return method.

	Student will have their own IDs and status of 
	currently borrowing or not

	If they are currently borrowing a laptop
	they will not be able to borrow an extra 
	"""

	def __init__(self, s_ID, l_ID = None):
		self.s_ID = s_ID
		self.l_ID = l_ID
		self.holding = False
		#by default the holding status will be false, meaning that they do not have any laptop
		if s_ID in MUN_list:
			self.limit = [19, 45]
		else:
			self.limit = [19, 30]


	def borrow(self, laptop_ID):
		if not self.s_ID in ban_list:
			if self.holding == True:
				print("Student {} is currently borrowing laptop {}.".format(self.s_ID, self.l_ID))
			else:
				#get current time
				tstamp = time.strftime("%a, %d %b %Y %H:%M:%S")

				#update new values
				self.l_ID = laptop_ID
				self.holding = True

				##log to csv time, s_id, and l_id
				print("Student {} borrowed laptop {} at {}".format(self.s_ID, self.l_ID, tstamp))
				
		elif self.s_ID in ban_list:
			#need to update the time system
			print("Student {} is currently being banned until ____")

	def hand_back(self, laptop_ID): 
		tstamp = time.strftime("%a, %d %b %Y %H:%M:%S") 
		if self.holding == True and self.l_ID == laptop_ID:
			hour = int(time.strftime("%H"))
			mins = int(time.strftime("%M"))
			if hour >= self.limit[0] and mins > self.limit[1]:
				#if the return time is later than the limit proceed to ban the student
				ban()
			else:
				#get current time, log info:
				
				#log to csv time, s_id, and l_id

				#update new values
				self.l_ID = None
				self.holding = False
				print("Student {} returned laptop {} at {}".format(self.s_ID, laptop_ID, tstamp))

		elif self.holding == False:
			#case of wrong student ID
			print("Student {} is not currently borrowing any laptop.".format(self.s_ID))
		elif self.holding == True and self.l_ID != laptop_ID:
			#case of wrong laptop ID
			print("Student {} did not borrow laptop {}.".format(self.s_ID, laptop_ID))

	def ban(self):
		#write a ban function that add itself into the list
		ban_list.append(self.s_ID)
		pass



if __name__ == "__main__":
	#testing
	hau = Student(17229041)
	time.sleep(2)
	hau.borrow("000130")
	time.sleep(2)
	hau.borrow("000131")
	time.sleep(2)
	hau.hand_back("000131")
	time.sleep(2)
	hau.hand_back("000130")
	time.sleep(2)
	hau.hand_back("000130")
			
print(__name__)
