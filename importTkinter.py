import tkinter as tk

def operation_creating1():
    a = float(entry1.get()) #باید انتری ها شماره کلا گذاری شوند
    b = float(entry2.get())
    p = (a+b)
    labelResult.configure(text = p)

def operation_creating2():
    a = float(entry1.get()) #باید انتری ها شماره کلا گذاری شوند
    b = float(entry2.get())
    p = (a-b)
    labelResult.configure(text = p)

def operation_creating3():
    a = float(entry1.get()) #باید انتری ها شماره کلا گذاری شوند
    b = float(entry2.get())
    p = (a*b)
    labelResult.configure(text = p)

# The tkinter codes
root = tk.Tk()
tk.Label(root, text ="عدد اول").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="عدد دوم").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Label(root, text="نتیجه برنامه").grid(row=2, column=0)
labelResult=tk.Label(root, text='')
labelResult.grid(row=2, column=1)


btn = tk.Button(root, text=" + ", font=("Arial", 18), command=(operation_creating1))
btn.grid(row=3, column=0)

btn = tk.Button(root, text=" - ", font=("Arial", 20), command=(operation_creating2))
btn.grid(row=4, column=0)


btn = tk.Button(root, text=" * ", font=("Arial", 20), command=(operation_creating3))
btn.grid(row=5, column=0)



root.mainloop()