from tkinter import filedialog
import tkinter.ttk as ttk
import tkinter as tk
from PIL import Image, ImageTk


def get_image_path():
    file_types = [('Image Files', '*.png *.jpg *.jpeg *.gif')]
    img_path = tk.filedialog.askopenfilename(filetypes=file_types)
    if len(img_path) > 0:
        return img_path
    else:
        return None


def get_palette_length(main_frm, length):
    length = length.get()
    length = int(length)
    if length > 0:
        return length
    else:
        return None
