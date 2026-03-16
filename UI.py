import tkinter as tk
from PIL import Image, ImageTk
from main import *

class ui():
    def __init__(self):
        root = tk.Tk()
        root.title('Frikandelbroodjes App')
        root.resizable(0, 0)

        root.iconbitmap('graphics/favicon.ico')

        # Window size and position defaults
        window_width = 300
        window_height = 200
        colour = "dark orange"

        center_x = int(root.winfo_screenwidth() / 2 - window_width / 2)
        center_y = int(root.winfo_screenheight() / 2 - window_height / 2)

        root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

        # BACKGROUND
        bg = Image.open("graphics/background.jpg")
        bg = bg.resize((window_width, window_height))  # optional
        bg_img = ImageTk.PhotoImage(bg)

        background_label = tk.Label(root, image=bg_img)
        background_label.place(relwidth=1, relheight=1)

        font = "Arial"
        fontsize_s = 10
        fontsize_l = 16

        # app
        tk.Label(root, text="Zakgeld (€)", bg=colour, font=(font, fontsize_s, "bold")).pack(pady=5)
        money_entry = tk.Entry(root)
        money_entry.focus()
        money_entry.pack()

        tk.Label(root, text="Prijs per stuk (€)", bg=colour, font=(font, fontsize_s, "bold")).pack(pady=5)
        price_entry = tk.Entry(root)
        price_entry.pack()

        button = tk.Button(root, text="Bereken", command=get_user_data, bg="dark orange", activebackground="yellow",
                           font=(font, fontsize_s, "bold"))
        button.pack(pady=10)

        result = tk.Label(root, text="____", font=(font, fontsize_l), bg="dark orange")
        result.pack()



def set_result(value):
    result.configure(text=str(value))
