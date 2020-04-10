import time
import os
import pickle

student_list = []

ban_list = []

MUN_list = []

"""
limit = [9, 29]

hour = int(time.strftime("%H"))
mins = int(time.strftime("%M"))

if hour >= limit[0] and mins > limit[1]:
	print("ban")
"""

class Student:
	def __init__(self, s_ID, l_ID = None):
		self.s_ID = s_ID
		self.l_ID = l_ID
		self.holding = False
		#by default the holding status will be false, meaning that they do not have any laptop
		if s_ID in MUN_list:
			self.limit = [19, 45]
		else:
			self.limit = [19, 30]

_17229041 = Student(17229041)


"""
ban = dict()
ban[17229041] = 20
print(ban)
print(17229041 in ban)
ban.pop(17229041)
print(ban)
"""

"""
unban_list = list()

unban_list.append(17229041)
unban_list.append(17229041)
unban_list.append(17229041)

print(unban_list)
"""

"""
ban_duration = {0: 1, 1: 7, 2: 14, 3: 31, 4: "indefinitely"}
print(type(ban_duration[1]))
"""

"""
mydict = {'george':(16, 22),'amber':(19, 23)}
print(list(mydict.keys())[list(mydict.values()).index(16)])

print(list(mydict.values())[0].index(16))
"""

"""
out_borrow = time.strftime("%d_%b_%Y") + "_borrow.csv"
out_return = time.strftime("%d_%b_%Y") + "_return.csv"

if not os.path.isfile(out_borrow):
	with open(out_borrow, "w") as f_out:
		f_out.write("time,s_id,l_id")

if not os.path.isfile(out_return):
	with open(out_return, "w") as f_out:
		f_out.write("time,s_id,l_id")
"""



test = pickle.load(open("bin/test_list.dat", "rb"))
print(test)
print(os.path.exists("bin"))
