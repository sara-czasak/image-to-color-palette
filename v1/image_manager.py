from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
from color_logic import *


class ImageManager:
    def __init__(self):
        self.image_frame = None
        self.colors = None
        self.image_path = None
        self.palette = None


    def get_or_change_img(self,button, image_frm):
        if self.image_frame is None:
            self.image_frame = image_frm
        for child in image_frm.winfo_children():
            child.destroy()
        file_types = [('Image Files', '*.png *.jpg *.jpeg *.gif')]
        self.image_path = tk.filedialog.askopenfilename(filetypes=file_types)
        if len(self.image_path) > 0:
            img = Image.open(self.image_path)
            if img.size[0] > 300 or img.size[1] > 300:
                img = img.resize((img.size[0] // 3, img.size[1] // 3))
            photo = ImageTk.PhotoImage(img)
            image_label = tk.Canvas(self.image_frame, width=img.size[0], height=img.size[1])
            image_label.create_image(0, 0, image=photo, anchor=tk.NW)
            image_label.image = photo
            image_label.pack()
            button.config(text="CHANGE IMAGE")
            self.get_colors()
            self.get_palette(16)
            return None
        else:
                return None


    def get_colors(self):
        if self.image_frame is not None and self.image_path is not None:
            img = Image.open(self.image_path).convert('RGB')
            colors = img.getcolors(img.size[0] * img.size[1])
            self.colors = sorted(colors, reverse=True)[:300]


    def get_palette(self, length):
        if self.image_frame is not None and self.colors is not None:
            self.palette = self.colors[:length]
            self.palette = [i[1] for i in self.palette]
            self.colors = self.colors[length:]




