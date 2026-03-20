import tkinter as tk
from PIL import Image, ImageTk
from src.logic import calculate_quantity, format_result

class CreateUI:

        def __init__(self):

                self.root = tk.Tk()
                self.root.title('Frikandelbroodjes App')
                self.root.resizable(False, False)

                # Window size and position defaults
                window_width = 300
                window_height = 200

                color = "dark orange"  # color for the backdrop

                font = "Arial"  # default font, catch ikf font does not exist??
                fontsize_s = 10
                fontsize_l = 16

                center_x = int(self.root.winfo_screenwidth() / 2 - window_width / 2)
                center_y = int(self.root.winfo_screenheight() / 2 - window_height / 2)

                self.root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

                # ICON
                # if icon does not exist, just don't draw it
                try:
                        self.root.iconbitmap('graphics/favicon.ico')
                except Exception:
                        pass

                # BACKGROUND
                # if background file does not exist, just don't draw it
                try:
                        self.bg = Image.open("graphics/background.jpg")
                        self.bg = self.bg.resize((window_width, window_height))  # optional
                        self.bg_img = ImageTk.PhotoImage(self.bg)
                        background_label = tk.Label(self.root, image=self.bg_img)
                        background_label.place(relwidth=1, relheight=1)

                except Exception:
                        pass

                # WIDGETS
                tk.Label(self.root, text="Zakgeld (€)", bg=color, font=(font, fontsize_s, "bold")).pack(pady=5)
                self.money_entry = tk.Entry(self.root)
                self.money_entry.focus()
                self.money_entry.pack()
                self.money_entry.bind("<Return>", lambda event: self.get_user_data())

                tk.Label(self.root, text="Prijs per stuk (€)", bg=color, font=(font, fontsize_s, "bold")).pack(pady=5)
                self.price_entry = tk.Entry(self.root)
                self.price_entry.pack()
                self.price_entry.bind("<Return>", lambda event: self.get_user_data())

                self.button = tk.Button(self.root, text="Bereken", command=self.process_input, bg="dark orange", activebackground="yellow",
                                   font=(font, fontsize_s, "bold"))
                self.button.pack(pady=10)

                self.result = tk.Label(self.root, text="____", font=(font, fontsize_l), bg="dark orange")
                self.result.pack()


        def process_input(self):

                money = self.money_entry.get()
                price = self.price_entry.get()

                quantity = calculate_quantity(money, price)
                text = format_result(quantity)

                self.result.config(text=text)

