import tkinter as tk
import tkinter.ttk as ttk
from button_func import *
from tkinter import filedialog


window = tk.Tk()
window.title("Color Palette from Image Generator")
window.minsize(150, 150)
main_frm = ttk.Frame(window)
main_frm.pack()


img_path = ''


def get_image_path():
    global img_path
    file_types = [('Image Files', '*.png *.jpg *.jpeg *.gif')]
    img_path = tk.filedialog.askopenfilename(filetypes=file_types)
    if len(img_path) > 0:
        with Image.open(img_path) as im:
            im.rotate(45).show()
        return img_path
    else:
        return None


# CHOSE IMAGE AND PALETTE LEN
# Let user choose img
choose_img_button = ttk.Button(main_frm, text="Choose Image", command=get_image_path)
choose_img_button.grid(column=0, row=0, padx=10, pady=10)

choose_palette_len = ttk.Spinbox(main_frm, from_=0, to=20)
choose_palette_len.grid(column=1, row=0, padx=10, pady=10)


# FRAME FOR DISPLAYING IMAGE
image_frm = ttk.Frame(window)
image_frm.pack()


image_placeholder = ttk.Label(image_frm, text='IMAGE GOES HERE')
image_placeholder.pack()


# FRAME TO DISPLAY COLOR PALETTE
palette_frm = ttk.Frame(window)
palette_frm.pack()
palette_placeholder = ttk.Label(palette_frm, text='PALETTE GOES HERE')
palette_placeholder.grid(row=0, column=0)











window.mainloop()


