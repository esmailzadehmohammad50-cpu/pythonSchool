import tkinter as tk

BG_COLOR = "#F5F7FA"
BTN_COLOR = "#4CAF50"
BTN_HOVER = "#2196F3"
BTN_TEXT = "white"
LABEL_COLOR = "#333333"

FONT_TITLE = ("Arial", 18, "bold")
FONT_LABEL = ("Arial", 12)
FONT_BTN = ("Arial", 12, "bold")

def add_hover(widget):
    widget.bind("<Enter>", lambda e: widget.config(bg=BTN_HOVER))
    widget.bind("<Leave>", lambda e: widget.config(bg=BTN_COLOR))
