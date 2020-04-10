import time
import csv

tstamp = time.strftime("%H-%M")
"""
with open("display.csv", "w") as f:
	f.write("time_stamp, student_id, laptop_id")
	for i in range(10):
		f.write('\n' + tstamp + "," + str(i) + "," + str(i + 5))
"""
"""
lines = []
with open('display.csv', 'r') as inp:
    for row in csv.reader(inp):
        if row[1] != "5" and row[2] != "10":
            lines.append(row)

with open('display.csv', 'w') as out:
    writer = csv.writer(out)
    for line in lines:
    	writer.writerow(line.strip)
"""
"""
with open("display.txt", "w") as f:
	f.write("time_stamp, student_id, laptop_id")
	for i in range(10):
		f.write('\n' + tstamp + "," + str(i) + "," + str(i + 5))
"""
with open("display.txt", "r") as f:
    lines = f.readlines()
with open("display.txt", "w") as f:
    for line in lines:
        if line.strip("\n").split(",")[1] != "7" and line.strip("\n").split(",")[2] != "12":
            f.write(line)

with open("display.txt", "r") as f:
	lines = f.readlines()
	lines.pop(0)
print(len(lines))
for i in range(len(lines)):
	print(i)
	display_text = "\n" + " ".join(lines[i].split(","))
print(display_text)