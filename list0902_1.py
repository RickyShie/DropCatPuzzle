import tkinter as tk


mouse_x = 0
mouse_y = 0
is_mouse_pressed = 0
font = ("Times New Roman", 30)


def mouse_move(e):
    global mouse_x
    global mouse_y
    mouse_x = e.x
    mouse_y = e.y


def mouse_press(e):
    global is_mouse_pressed
    is_mouse_pressed = 1


def mouse_release(e):

    global is_mouse_pressed
    is_mouse_pressed = 0


def game_main():
    txt = f"mouse({mouse_x}, {mouse_y}){is_mouse_pressed}"
    canvas.delete("TEST")
    canvas.create_text(456, 384, text=txt, fill="black", font=font, tags="TEST")
    root.after(100, game_main)


root = tk.Tk()
root.title("Mouse Input")
root.resizable(False, False)

# Bind mouse event to root widget
root.bind("<ButtonPress>", mouse_press)
root.bind("<ButtonRelease>", mouse_release)
root.bind("<Motion>", mouse_move)
canvas = tk.Canvas(master=root, width=912, height=768)
canvas.pack()
game_main()

canvas.create_text(456, 384, text='HELLO', fill="black", font=font, tags="TEST")

root.mainloop()