import PIL
from PIL import Image


class ColorPicker:
    def __init__(self, img_path):
        self.cols = self.get_all_colors(img_path)
        self.palette = []

    def get_all_colors(self, img_path):
        img = Image.open(img_path).convert('RGB')
        colors = img.getcolors(img.size[0] * img.size[1])
        cols = sorted(colors, reverse=True)[:300]
        return cols


    def get_initial_palette(self):
        self.palette = self.cols[:20]
        self.cols = self.cols[20:]


    def get_new_color(self):
        color = self.cols[0]
        self.palette.append(color)
        self.cols = self.cols[1:]


    def remove_a_color(self, color):
        self.palette.remove(color)


    def swap_colors(self, cols_to_swap):
        for color in cols_to_swap:
            self.remove_a_color(color)
            self.get_new_color()



