from tkinter import filedialog
import tkinter.ttk as ttk
import tkinter as tk
from PIL import Image, ImageTk


def get_image():
    file_types = [('Image Files', '*.png *.jpg *.jpeg *.gif')]
    img = tk.filedialog.askopenfilename(filetypes=file_types)
    display_img = ImageTk.PhotoImage(img)
    return display_img


def get_palette_length(frm, length):
    length = length.get()
    length = int(length)
    if length > 0:
        return length
    else:
        return None
