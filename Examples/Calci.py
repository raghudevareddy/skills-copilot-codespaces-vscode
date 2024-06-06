import tkinter as tk

def add():
    result.set(float(num1.get()) + float(num2.get()))

def subtract():
    result.set(float(num1.get()) - float(num2.get()))

root = tk.Tk()

num1 = tk.StringVar()
num2 = tk.StringVar()
result = tk.StringVar()

tk.Entry(root, textvariable=num1).pack()
tk.Entry(root, textvariable=num2).pack()

tk.Button(root, text='Add', command=add).pack()
tk.Button(root, text='Subtract', command=subtract).pack()

tk.Label(root, textvariable=result).pack()

root.mainloop()