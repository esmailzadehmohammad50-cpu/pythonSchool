import tkinter as tk
from tkinter import messagebox
from styles import *

def open_login():
    login=tk.Tk()
    # login = tk.Toplevel()
    login.title("ورود")
    login.geometry("300x200")
    login.config(bg=BG_COLOR)

    tk.Label(login, text="ورود به برنامه", font=FONT_TITLE, bg=BG_COLOR).grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(login, text="نام کاربری:", font=FONT_LABEL, bg=BG_COLOR).grid(row=1, column=0)
    entry_user = tk.Entry(login, font=FONT_LABEL)
    entry_user.grid(row=1, column=1)

    tk.Label(login, text="رمز عبور:", font=FONT_LABEL, bg=BG_COLOR).grid(row=2, column=0)
    entry_pass = tk.Entry(login, show="*", font=FONT_LABEL)
    entry_pass.grid(row=2, column=1)
    login.mainloop()
    def check_login():
        if entry_user.get() == "mohammad" and entry_pass.get() == "A123456":
            login.destroy()
            
            import main_window
            
            root.deiconify()

        else:
            messagebox.showerror("خطا", "اطلاعات نادرست")


    btn_login = tk.Button(
        login,
        text="ورود",
        font=FONT_BTN,
        bg=BTN_COLOR,
        fg=BTN_TEXT,
        command=check_login
    )
    btn_login.grid(row=3, column=0, columnspan=2, pady=15)
    add_hover(btn_login)

    
