import tkinter as tk
from tkinter import messagebox
from styles import *
from diet_window import show_diet_window

def open_main_window(root):
    root.title("محاسبه BMI")
    root.geometry("400x350")
    root.config(bg=BG_COLOR)

    main_frame = tk.Frame(root, bg=BG_COLOR, padx=20, pady=20)
    main_frame.pack(expand=True)

    tk.Label(
        main_frame,
        text="محاسبه BMI",
        font=FONT_TITLE,
        bg=BG_COLOR
    ).grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(main_frame, text="قد (سانتی‌متر):", font=FONT_LABEL, bg=BG_COLOR).grid(row=1, column=0)
    entry_height = tk.Entry(main_frame, font=FONT_LABEL)
    entry_height.grid(row=1, column=1)

    tk.Label(main_frame, text="وزن (کیلوگرم):", font=FONT_LABEL, bg=BG_COLOR).grid(row=2, column=0)
    entry_weight = tk.Entry(main_frame, font=FONT_LABEL)
    entry_weight.grid(row=2, column=1)

    def calculate_bmi():
        try:
            height_cm = float(entry_height.get())
            weight = float(entry_weight.get())
            height = height_cm / 100

            bmi = weight / (height ** 2)

            if bmi < 18.5:
                category = "کمبود وزن"
            elif bmi < 25:
                category = "وزن نرمال"
            elif bmi < 30:
                category = "اضافه وزن"
            else:
                category = "چاقی"

            top = tk.Toplevel(root)
            top.title("نتیجه BMI")
            top.geometry("300x200")

            tk.Label(
                top,
                text=f"BMI: {bmi:.2f}\n{category}",
                font=FONT_LABEL
            ).pack(pady=10)

            btn = tk.Button(
                top,
                text="برنامه غذایی",
                font=FONT_BTN,
                bg=BTN_COLOR,
                fg=BTN_TEXT,
                command=lambda: show_diet_window(root, category)
            )
            btn.pack(pady=10)
            add_hover(btn)

        except:
            messagebox.showerror("خطا", "اعداد معتبر وارد کنید")

    btn_calc = tk.Button(
        main_frame,
        text="محاسبه",
        font=FONT_BTN,
        bg=BTN_COLOR,
        fg=BTN_TEXT,
        command=calculate_bmi
    )
    btn_calc.grid(row=3, column=0, columnspan=2, pady=15)
    add_hover(btn_calc)
