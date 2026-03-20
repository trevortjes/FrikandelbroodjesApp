import tkinter as tk
from PIL import Image, ImageTk
from math import floor

class CreateUI:

        def __init__(self):

                self.root = tk.Tk()
                self.root.title('Frikandelbroodjes App')
                self.root.resizable(0, 0)

                # Window size and position defaults
                window_width = 300
                window_height = 200

                color = "dark orange"  # color for the backdrop

                font = "Arial"  # default font, catch if font does not exist??
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

                self.button = tk.Button(self.root, text="Bereken", command=self.get_user_data, bg="dark orange", activebackground="yellow",
                                   font=(font, fontsize_s, "bold"))
                self.button.pack(pady=10)

                self.result = tk.Label(self.root, text="____", font=(font, fontsize_l), bg="dark orange")
                self.result.pack()


        # Grab user submitted data
        def get_user_data(self) -> None:

                money = self.money_entry.get()  # Store value from money entry
                price = self.price_entry.get()  # Store value from price entry
                self.calculate_quantity(money, price)


        # Calculation of how many frikandelbroodjes can be bought
        def calculate_quantity(self, money, price):

                try:
                        quantity = floor(float(money) / float(price))  # hoeveel broodjes gekocht kunnen worden
                        self.show_result(quantity)
                        return quantity

                except:
                        # tell the user to input a number
                        self.result.config(text="Das geen getal")
                        return "wrong input"


        # Show the result to the user
        def show_result(self, quantity) -> None:

            if quantity > 1 or quantity == 0:
                self.result.configure(text=str(quantity) + " frikandelbroodjes!")
                return "broodjes"
            elif quantity < 0:
                self.result.config(text="Lol poor")
                return "invalid"
            else:
                self.result.configure(text=str(quantity) + " frikandelbroodje!")
                return "broodje"