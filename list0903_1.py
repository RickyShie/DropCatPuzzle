import tkinter as tk

root = tk.Tk()
root.title("Display Image in Canvas")

canvas = tk.Canvas(root, width=912, height=768)
canvas.pack()

# Load and display the image
image = tk.PhotoImage(file="./neko_bg.png") # Replace with your image path
canvas.create_image(200, 200, image=image)  # 200, 200 is the center of the canvas

root.mainloop()