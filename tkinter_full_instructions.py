from tkinter import *

def click ():
    print("in the name of God!!!") # it is not important it is just for that we need a function for our button config

window = Tk() #instantiate an intense of a window 

window.geometry("450x400") # for changing the window size.

window.title("mohammad tkinter GUI training.") #for changing the window title.

icon = PhotoImage(file='tkinter_practice.py/photoe12.png')

window.iconphoto(True, icon) # we use line of 12 and 14 for changing the window logo

window.config(background="#0238FD") # for changing background color and we can use this too: button.config(bg='#05fc85')

button = Button(window, text='push here...') # for making a buton and to wirte something on that

button.config(command=click) #performs call back of function just you made

button.config(font=('ink free', 50 , 'bold')) # so in free is name of a font and 50 the size and bold make it bold
button.pack() # this pack make the button enable to push it 

button.config(fg='#05fac5') # for changing the text color

button.config(activebackground='#FF0000') # that si for when you click on the button change the color of button background

button.config(activeforeground="#ffffff") # for changing the text color when you click on the button


window.mainloop() #place window on computer screen, listen for events.

# seach "hex color picker" on google for knowing the name of python color tochange it.