import tkinter as tk
from os import listdir
import random


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        # Import image files
        self.background_image = tk.PhotoImage(file="./neko_bg.png")
        self.cursor_image = tk.PhotoImage(file="./neko_cursor.png")
        self.blue_cat_image = tk.PhotoImage(file="./blue_cat.png")
        self.green_cat_image = tk.PhotoImage(file="./green_cat.png")
        self.pink_cat_image = tk.PhotoImage(file="./pink_cat.png")
        self.purple_cat_image = tk.PhotoImage(file="./purple_cat.png")
        self.red_cat_image = tk.PhotoImage(file="./red_cat.png")
        self.yellow_cat_image = tk.PhotoImage(file="yellow_cat.png")
        self.cat_image_list = [tk.PhotoImage(file=file) for file in listdir() if file.endswith('_cat.png')]

        # Mouse coordinates
        self.mouse_x = 0
        self.mouse_y = 0

        # Cursor coordinates
        self.cursor_x = 0
        self.cursor_y = 0

        # Mouse status
        self.is_mouse_pressed = 0

        # Create game board
        self.canvas = tk.Canvas(master=self, width=912, height=768)
        self.canvas.pack()
        self.canvas.create_image(456, 384, image=self.background_image)

        # Generate a random cat image when the app is launched
        self.current_cat_image = self.generate_random_cat_image()

        # Bind mouse events
        self.bind("<Motion>", self.track_mouse_movement)
        self.bind("<ButtonPress>", self.mouse_press)
        self.bind("<ButtonRelease>")

    def track_mouse_movement(self, event=None):
        self.mouse_x = event.x
        self.mouse_y = event.y
        if (24 <= self.mouse_x) and \
                (self.mouse_x < 24 + 72 * 8) and \
                (24 <= self.mouse_y) and \
                (self.mouse_y < 24 + 72 * 10):
            self.cursor_x = int((self.mouse_x - 24) / 72)
            self.cursor_y = int((self.mouse_y - 24) / 72)
            self.canvas.delete("CURSOR")
            self.canvas.create_image(self.cursor_x * 72 + 60,
                                     self.cursor_y * 72 + 60,
                                     image=self.cursor_image,
                                     tags="CURSOR")
            print(f"Cursor at x: {self.cursor_x} y: {self.cursor_y}")

    def mouse_press(self, event=None):
        self.is_mouse_pressed = 1
        print(f'Mouse has been pressed at x: {self.mouse_x}, y: {self.mouse_y}')
        self.canvas.create_image(self.cursor_x * 72 + 60,
                                 self.cursor_y * 72 + 60,
                                 image=self.current_cat_image)

        self.generate_random_cat_image()

    def mouse_release(self):
        self.is_mouse_pressed = 0

    def generate_random_cat_image(self):
        image = random.choice(self.cat_image_list)
        self.canvas.delete("RANDOM_CAT")
        self.current_cat_image = image
        self.canvas.create_image(750, 110, image=image, tags="RANDOM_CAT")
        return image


app = App()


app.mainloop()

