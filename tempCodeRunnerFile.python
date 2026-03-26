import tkinter as tk


class SmartHomeGUI:

    def __init__(self, root):

        self.root = root
        self.root.title("Smart Home Control Panel")
        self.root.geometry("500x550")
        self.root.resizable(False, False)

        # Time
        self.hour = 0

        # Prices (24 Hours)
        self.prices = [
            3,3,3,3,3,3,
            5,5,5,5,
            7,7,7,7,
            9,9,9,9,
            6,6,5,4
        ]

        # Appliances & Power
        self.devices = {
            "Fan": 1,
            "Light": 0.5,
            "AC": 3,
            "TV": 1.5,
            "Washer": 2
        }

        # Status (0 = OFF, 1 = ON)
        self.status = {d: 0 for d in self.devices}

        # ===== TITLE =====
        tk.Label(
            root,
            text="SMART HOME DASHBOARD",
            font=("Consolas", 18, "bold"),
            fg="cyan"
        ).pack(pady=10)


        # ===== DEVICE FRAME =====
        self.frame = tk.Frame(root, bd=2, relief="ridge")
        self.frame.pack(padx=20, pady=10, fill="x")


        self.labels = {}
        self.dots = {}


        for d in self.devices:

            row = tk.Frame(self.frame)
            row.pack(pady=6, padx=10, fill="x")


            tk.Label(
                row, text=d,
                font=("Consolas", 12),
                width=8
            ).pack(side="left")


            lbl = tk.Label(
                row, text="OFF",
                fg="red",
                font=("Consolas", 12, "bold"),
                width=4
            )
            lbl.pack(side="left", padx=5)


            dot = tk.Label(
                row, text="●",
                fg="red",
                font=("Consolas", 14)
            )
            dot.pack(side="left")


            btn = tk.Button(
                row, text="Toggle",
                width=8,
                command=lambda x=d: self.toggle(x)
            )
            btn.pack(side="right", padx=5)


            self.labels[d] = lbl
            self.dots[d] = dot


        # ===== INFO FRAME =====
        self.info = tk.Frame(root, bd=2, relief="ridge")
        self.info.pack(padx=20, pady=15, fill="x")


        self.time_lbl = tk.Label(
            self.info, text="Hour : 00:00",
            font=("Consolas", 12)
        )
        self.time_lbl.pack(pady=4)


        self.price_lbl = tk.Label(
            self.info, text="Price/unit : ₹0",
            font=("Consolas", 12)
        )
        self.price_lbl.pack(pady=4)


        self.cost_lbl = tk.Label(
            self.info, text="Cost : ₹0",
            font=("Consolas", 12, "bold")
        )
        self.cost_lbl.pack(pady=4)


        # Start Clock
        self.update_time()



    # ================= TOGGLE =================

    def toggle(self, device):

        if self.status[device] == 0:
            self.status[device] = 1
        else:
            self.status[device] = 0

        self.update_ui()



    # ================= UPDATE UI =================

    def update_ui(self):

        price = self.prices[self.hour]

        total_cost = 0


        for d in self.devices:

            if self.status[d] == 1:

                self.labels[d].config(text="ON", fg="green")
                self.dots[d].config(fg="green")

                total_cost += self.devices[d] * price

            else:

                self.labels[d].config(text="OFF", fg="red")
                self.dots[d].config(fg="red")


        self.price_lbl.config(text=f"Price/unit : ₹{price}")

        self.cost_lbl.config(
            text=f"Cost : ₹{round(total_cost,2)}"
        )



    # ================= TIME =================

    def update_time(self):

        self.hour = (self.hour + 1) % 24

        self.time_lbl.config(
            text=f"Hour : {self.hour:02d}:00"
        )

        self.update_ui()

        # Update every 2 seconds
        self.root.after(2000, self.update_time)



# ================= MAIN =================

if __name__ == "__main__":

    root = tk.Tk()

    SmartHomeGUI(root)

    root.mainloop()