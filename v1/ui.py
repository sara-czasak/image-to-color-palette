import tkinter as tk
import tkinter.ttk as ttk
from button_func import *



window = tk.Tk()
window.title("Color Palette from Image Generator")
window.minsize(150, 150)
frame = ttk.Frame(window)
frame.pack()


# CHOSE IMAGE AND PALETTE LEN
# Let user choose img
choose_img_button = ttk.Button(frame, text="Choose Image")
choose_img_button.grid(column=0, row=0, padx=10, pady=10)

choose_palette_len = ttk.Spinbox(frame, from_=0, to=50)
choose_palette_len.grid(column=1, row=0, padx=10, pady=10)

confirl_palette_len = ttk.Button(frame, text="Ok")
confirl_palette_len.grid(column=2, row=0, padx=10, pady=10)


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


