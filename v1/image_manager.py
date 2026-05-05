from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk


class ImageManager:
    def __init__(self):
        pass

    def get_or_change_img(self,button, image_frm):
        for child in image_frm.winfo_children():
            child.destroy()
        file_types = [('Image Files', '*.png *.jpg *.jpeg *.gif')]
        img_path = tk.filedialog.askopenfilename(filetypes=file_types)
        if len(img_path) > 0:
            img = Image.open(img_path)
            if img.size[0] > 300 or img.size[1] > 300:
                img = img.resize((img.size[0] // 3, img.size[1] // 3))
            photo = ImageTk.PhotoImage(img)
            image_label = tk.Canvas(image_frm, width=img.size[0], height=img.size[1])
            image_label.create_image(0, 0, image=photo, anchor=tk.NW)
            image_label.image = photo
            image_label.pack()
            button.config(text="CHANGE IMAGE")
            return None
        else:
                return None