from tkinter import ttk
from image_manager import *


window = tk.Tk()
window.title("Color Palette from Image Generator")
window.minsize(150, 150)
main_frm = ttk.Frame(window)
main_frm.pack()


img_mgr = ImageManager()


# CHOSE IMAGE AND PALETTE LEN
# Let user choose img
choose_img_button = ttk.Button(main_frm, text="CHOOSE IMAGE", command=lambda: img_mgr.get_or_change_img(choose_img_button, image_frm))
choose_img_button.grid(column=0, row=0, padx=10, pady=10)


# FRAME FOR DISPLAYING IMAGE
image_frm = ttk.Frame(window)
image_frm.pack()


# FRAME TO DISPLAY COLOR PALETTE
palette_frm = ttk.Frame(window)
palette_frm.pack()
palette_placeholder = ttk.Label(palette_frm, text='PALETTE GOES HERE')
palette_placeholder.grid(row=0, column=0)




window.mainloop()


