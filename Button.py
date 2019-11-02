import tkinter as tk

root = tk.Tk()

#Step 1 is constructing the widget
btn1 = tk.Button(root, width = 20, height = 3)
#Step 2: Configure the widget
btn1.config(text = "Hello World")
#Step 3: Place the widget 
btn1.pack()

root.mainloop()

