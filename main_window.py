import data
from styles import *
import webbrowser

def show_diet_window(category):
    plan = data.diet_plans[category]

    win = tk.Toplevel(root)
    win.title(f"برنامه غذایی - {category}")
    win.geometry("420x620")
    win.config(bg=BG_COLOR)

    tk.Label(
        win,
        text=f"برنامه غذایی ({category})",
        font=FONT_TITLE,
        bg=BG_COLOR
    ).pack(pady=10)

    text_box = tk.Text(
        win,
        font=FONT_LABEL,
        height=14,
        width=40,
        wrap="word"
    )
    text_box.pack(pady=10)
    text_box.config(state="disabled")

    link_label = tk.Label(
        win,
        text="🔗 اطلاعات بیشتر",
        font=FONT_LABEL,
        fg="blue",
        cursor="hand2",
        bg=BG_COLOR
    )
    link_label.pack(pady=5)

    def show_meal(meal):
        text_box.config(state="normal")
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, f"{meal}\n{plan[meal]}")
        text_box.config(state="disabled")

        link_label.bind(
            "<Button-1>",
                    lambda e: webbrowser.open("https://www.google.com")
        )

    for meal in plan:
        btn = tk.Button(
            win,
            text=meal,
            font=FONT_BTN,
            bg=BTN_COLOR,
            fg=BTN_TEXT,
            width=25,
            command=lambda m=meal: show_meal(m)
        )
        btn.pack(pady=3)
        add_hover(btn)
