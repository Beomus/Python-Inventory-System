import tkinter as tk
import tkinter.ttk as ttk
import main as m


"""
Functions go here
"""
def lend():
	status.set('Student 17229041 has borrowed laptop 130.')
	tree.insert("", 0, values = ( 1, 2, 3))

def hback():
	status.set('Student 17229041 has returned laptop 130.')
	tree.insert("", 0, values = ( 1, 2, 3))



#settings for the main window
root = tk.Tk()
root.title("Laptop System")
root.geometry("1600x900")
#root.minsize(width = 1600, height = 900)
root.resizable(0, 0)

""" 
#settings for the background
back = tk.Frame(master = root)
back.pack_propagate(0)
back.pack(fill = tk.BOTH, expand = 1)
"""

#Lending and returning button
lend_button = tk.Button(master = root, text = "Lend", font = "Times 25", width = 10, command = lend) 
# fill in command whenver you import main
lend_button.place(x = 448, y = 333)
return_button = tk.Button(master = root, text = "Return", font = "Times 25", width = 10, command = hback) 
# fill in command whenver you import main
return_button.place(x = 960, y = 333)

#Main label
main_label = tk.Label(master = root, text = "LAPTOP SYSTEM", font = "Times 60 bold")
main_label.pack()

#S_ID and L_ID label
s_id_label = tk.Label(master = root, text = "Student ID", font = "Times 30 bold")
s_id_label.place(x = 128, y = 162)

l_id_label = tk.Label(master = root, text = "Laptop ID", font = "Times 30 bold")
l_id_label.place(x = 128, y = 252)

#Status label
status = tk.StringVar()
status.set("")

status_label = tk.Label(master = root, textvariable = status, font = "Times 30")
status_label.place(x = 480, y = 423)

# Table view
TableMargin = tk.Frame(root, width = 1200, height = 300)
TableMargin.place(x = 320, y = 495)
scrollbary = tk.Scrollbar(TableMargin, orient= 'vertical')
tree = ttk.Treeview(TableMargin, columns=("TIME STAMP", "STUDENT ID", "LAPTOP ID"), height = 200, selectmode="extended", yscrollcommand=scrollbary.set)
scrollbary.config(command = tree.yview)
scrollbary.pack(side = 'right')
tree.heading('TIME STAMP', text = "TIME STAMP", anchor = 'w')
tree.heading('STUDENT ID', text = "STUDENT ID", anchor = 'w')
tree.heading('LAPTOP ID', text = "LAPTOP ID", anchor = 'w')
tree.column('#0', stretch = 'no', minwidth = 0, width = 0)
tree.column('#1', stretch = 'n', minwidth = 400, width = 400)
tree.column('#2', stretch = 'no', minwidth = 300, width = 300)
tree.column('#3', stretch = 'no', minwidth = 300, width = 300)

style = ttk.Style()
style.configure("Treeview.Heading", font = "Times 25 bold")

tree.pack()

#Entries for s_id and l_id
var1 = tk.StringVar()
var1.set('Student ID')
var2 = tk.StringVar()
var2.set('Laptop ID')
s_id_entry = tk.Entry(master = root, textvariable = var1, font = "Times 25", width = 70)
s_id_entry.place(relx = 0.21, rely = 0.1805)

l_id_entry = tk.Entry(master = root, textvariable = var2, font = "Times 25", width = 70)
l_id_entry.place(relx = 0.21, rely = 0.2805)


#Main loop for the program
if __name__ == "__main__":
	root.mainloop()