import time
import os
import pickle
import csv

# creating folders to save data, config, and progress
if not os.path.exists("bin"):
	os.mkdir("bin")

if not os.path.exists("log"):
	os.mkdir("log")

# calling necessary list
MUN_list = list()
borrow_list = dict()
return_list = dict()
ban_list = dict()
unban_list = list()

# need actual laptop and a function to add laptops
laptop_list = ["130", "131", "132", "133", "134"]


DATA = [MUN_list, borrow_list, return_list, ban_list, unban_list, laptop_list]
for item in DATA:
	if os.path.isfile("bin/" + str(item)+ ".dat"):
		item = pickle.load(open("bin/" + str(item) + ".dat", "rb"))


# defining standard ban rules
ban_duration = {0: 1, 1: 7, 2: 14, 3: 31, 4: "indefinitely"}


# creating files for logging lending/returning information
if not os.path.isfile("log/" + "borrow.csv"):
	with open("log/" + "borrow.csv", "w") as f:
		f.write("time_stamp, student_id, laptop_id \n")

if not os.path.isfile("log/" + "return.csv"):
	with open("log/" + "return.csv", "w") as f:
		f.write("time_stamp, student_id, laptop_id \n")

if not os.path.isfile("log/" + "display.txt"):
	with open("log/" + "display.txt", "w") as f:
		f.write("time_stamp, student_id, laptop_id \n")

def borrow(student_id, laptop_id):
	"""
	pair student id and laptop id into a dictionary
	also with the time stamp
	using condition that student id is not in the ban list
	"""
	t_stamp = time.strftime("%H:%M")
	d_stamp = time.strftime("%a %d %b %Y %H:%M")
	# taking the current time stamp

	if not student_id in ban_list:
		# checking if student is in the ban list 
		if student_id in borrow_list:
			# check if student is currently borrowing any laptop
			result = ("Student {} is currently borrowing laptop {}.".format(student_id, borrow_list[student_id][0]))
			return result
		else:
			# add the key-value pair of student id and laptop id + time stamp
			if laptop_id in laptop_list:
				borrow_list[student_id] = laptop_id, t_stamp
				laptop_list.remove(laptop_id)
				pickle.dump(borrow_list, open("bin/" + "borrow_list.dat", "wb"))
				pickle.dump(laptop_list, open("bin/" + "laptop_list.dat", "wb"))
				with open("log/" + "borrow.csv", "a") as f:
					f.write(str(d_stamp) + "," + str(student_id) + "," + str(laptop_id) + "\n")
				with open("log/" + "display.txt", "a") as f:
					f.write(str(d_stamp) + "," + str(student_id) + "," + str(laptop_id) + "\n")
				result = ("Student {} has borrowed laptop {} at {}.".format(student_id, laptop_id, t_stamp))
				return result
			elif not laptop_id in laptop_list:
				result = ("Student {} is currently borrowing laptop {}.".format(list(borrow_list.keys())[list(borrow_list.values())[0].index(laptop_id)], laptop_id))
				return result
	elif student_id in ban_list:
		# get info on the student who got banned
		result = ("Student {} is banned until {}".format(student_id, ban_list[student_id]))
		return result


def hand_back(student_id, laptop_id):
	"""
	find in the borrow list said student ID and laptop ID
	verifies if they actually borrowed it
	then return it with a time stamp
	also check if they have returned it after or before the limit
	then implements the ban according ly
	"""
	t_stamp = time.strftime("%H:%M")
	d_stamp = time.strftime("%a %d %b %Y %H:%M")
	hour = int(time.strftime("%H"))
	mins = int(time.strftime("%M"))
	if student_id in MUN_list:
		# check if student is in MUN list, if yes then double check limit with 19:45
		if hour >= 19 and mins > 45:
			ban(student_id)
		else:
			return_list[student_id] = laptop_id, t_stamp
			laptop_list.append(laptop_id)
			pickle.dump(return_list, open("bin/" + "return_list.dat", "wb"))
			pickle.dump(laptop_list, open("bin/" + "laptop_list.dat", "wb"))
			with open("log/" + "return.csv", "a") as f:
				f.write(str(d_stamp) + "," + str(student_id) + "," + str(laptop_id) + "\n")

			# remove the specific row
			with open("log/" + "display.txt", "w") as f:
				lines = f.readlines()
				for line in lines:
					if line.strip("\n").split(",")[1] != student_id and line.strip("\n").split(",")[2] != laptop_id:
						f.write(line)
			result = ("Student {} returned laptop {} at {}".format(student_id, laptop_id, t_stamp))
			return result
	else:
		# this is the case when it's just a normal student, then time limit is 19:30
		if hour >= 19 and mins > 30:
			ban(student_id)
		else:
			return_list[student_id] = laptop_id, t_stamp
			laptop_list.append(laptop_id)
			pickle.dump(return_list, open("bin/" + "return_list.dat", "wb"))
			pickle.dump(laptop_list, open("bin/" + "laptop_list.dat", "wb"))
			with open("log/" + "return.csv", "a") as f:
				f.write(str(d_stamp) + "," + str(student_id) + "," + str(laptop_id) + "\n")

			# remove the specific row
			with open("log/" + "display.txt", "r") as f:
				lines = f.readlines()
			with open("log/" + "display.txt", "w") as f:
			    for line in lines:
			        if line.strip("\n").split(",")[1] != student_id and line.strip("\n").split(",")[2] != laptop_id:
			            f.write(line)
			result = ("Student {} returned laptop {} at {}".format(student_id, laptop_id, t_stamp))
			return result


def ban(student_id, duration = None):
	"""
	function to ban student, default to non
	"""
	count = 0
	for i in unban_list:
		if i == student_id:
			count += 1
	duration = ban_duration[count]
	t_stamp = time.strftime("%a %d %b %Y %H:%M")
	ban_list[student_id] = t_stamp, duration
	pickle.dump(ban_list, open("ban_list.dat", "wb"))
	result = ("Student {} has been banned for {} day(s).".format(student_id, duration))
	return result


def unban(student_id):
	"""
	call this function to unban a student
	"""
	ban_list.pop(student_id)
	unban_list.append(student_id)

	pickle.dump(ban_list, open("ban_list.dat", "wb"))
	pickle.dump(unban_list, open("unban_list.dat", "wb"))

	result = "Student {} has been unbanned.".format(student_id)
	return result


def find_laptop(laptop_id):
	"""
	This function is called to locate a laptop
	whether it is available or currently being borrowed by a student
	"""
	if laptop_id in laptop_list:
		result = ("Laptop {} is available.".format(laptop_id))
		return result
	elif not laptop_id in laptop_list:
		result = "Student {} has laptop {}.".format(list(borrow_list.keys())[list(borrow_list.values())[0].index(laptop_id)], laptop_id)
		return result

def add_laptops(laptop_id):
	"""
	This function is called to add a new laptop or 
	a list of laptops to the current rotation
	"""
	for i in range(len(laptop_id)):
		if i == ',':
			laptop_list_to_update = laptop_id.split(',').strip()
			for item in laptop_list_to_update:
				laptop_list.append(int(item))
				result = 'Laptop list has been updated with {}.'.format(laptop_id)
				return result
		else:
			laptop_list.append(int(laptop_id))
			result = 'Laptop list has been updated with {}.'.format(laptop_id)
			return result

