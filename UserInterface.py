from math import floor
import tkinter as tk
from PIL import Image, ImageTk

class CreateUI:

        def __init__(self):
                self.root = tk.Tk()
                self.root.title('Frikandelbroodjes App')
                self.root.resizable(0, 0)

                self.root.iconbitmap('graphics/favicon.ico')

                # Window size and position defaults
                window_width = 300
                window_height = 200
                colour = "dark orange"

                center_x = int(self.root.winfo_screenwidth() / 2 - window_width / 2)
                center_y = int(self.root.winfo_screenheight() / 2 - window_height / 2)

                self.root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

                # BACKGROUND
                self.bg = Image.open("graphics/background.jpg")
                self.bg = self.bg.resize((window_width, window_height))  # optional
                self.bg_img = ImageTk.PhotoImage(self.bg)

                background_label = tk.Label(self.root, image=self.bg_img)
                background_label.place(relwidth=1, relheight=1)

                font = "Arial"
                fontsize_s = 10
                fontsize_l = 16

                # app
                tk.Label(self.root, text="Zakgeld (€)", bg=colour, font=(font, fontsize_s, "bold")).pack(pady=5)
                self.money_entry = tk.Entry(self.root)
                self.money_entry.focus()
                self.money_entry.pack()

                tk.Label(self.root, text="Prijs per stuk (€)", bg=colour, font=(font, fontsize_s, "bold")).pack(pady=5)
                self.price_entry = tk.Entry(self.root)
                self.price_entry.pack()

                self.button = tk.Button(self.root, text="Bereken", command=self.get_user_data, bg="dark orange", activebackground="yellow",
                                   font=(font, fontsize_s, "bold"))
                self.button.pack(pady=10)

                self.result = tk.Label(self.root, text="____", font=(font, fontsize_l), bg="dark orange")
                self.result.pack()


        # Grab user submitted data
        def get_user_data(self):

                money = self.money_entry.get()  # Store value from money entry
                price = self.price_entry.get()  # Store value from price entry
                self.calculate_quantity(money, price)


        # Calculation of how many frikandelbroodjes can be bought
        def calculate_quantity(self, money, price):

                try:
                        quantity = floor(float(money) / float(price))  # hoeveel broodjes gekocht kunnen worden
                        print(quantity)
                        self.show_result(quantity)

                except:
                        # tell the user to input a number
                        self.result.config(text="Das geen getal")


        # Show the result to the user
        def show_result(self, quantity):
            string = ""
            if quantity > 1 or quantity == 0:
                self.result.configure(text=str(quantity) + " frikandelbroodjes!")
            elif quantity < 0:
                self.result.config(text="Lol poor")
            else:
                self.result.configure(text=str(quantity) + " frikandelbroodje!")

