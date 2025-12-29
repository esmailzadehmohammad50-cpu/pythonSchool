import tkinter as tk
import turtle

def shekl():
    num_z=int(entry1.get())
    num_forwrd=int(entry2.get())
    root = turtle.Turtle()
    b = num_z
    c = num_forwrd
    degree=360/num_z
    for i in range(num_z):
        root.forward(num_forwrd)
        root.left(degree)

app = tk.Tk()
app.config(background="red")
app.config()
tk.Label(app, text="num_z :  ").grid(row=0, column=1)
entry1 = tk.Entry(app)
entry1.grid(row=0, column=0)

tk.Label(app, text="num_forwrd     : ").grid(row=1, column=1)
entry2 = tk.Entry(app)
entry2.grid(row=1, column=0)

btn = tk.Button(app, text="draw it", font=("Arial", 14), command=shekl)
btn.grid(row=3, column=0)

app.mainloop()
turtle.done()