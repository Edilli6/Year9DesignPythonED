import tkinter as tk

print("Start Program")

print("WHATTT!!!")
def onclick():
	print("Luca = Weird")

	

root = tk.Tk() #Build yoir main window

#Widget/Element is an element in a GUI.
#Button, Textbox, Dropdown

#Step 1 is constructing the widget
btn1 = tk.Button(root, width = 20, height = 3)
#Step 2: Configure the widget
btn1.config(text = "WHATTT!!!!", command = onclick)
#Step 3: Place the widget 
btn1.pack()

output = tk.Text(root, width = 60, height = 20)
output.config()
output.pack();

btn2 = tk.Button(root, width = 20, height = 3)

btn2.config(text = "I definitly a button")

btn2.pack()

root.mainloop()

print("END PROGRAM")