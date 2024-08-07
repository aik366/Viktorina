import customtkinter as ctk
from random import randint, shuffle, choices

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class Timer(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("+600+300")
        self.grid_rowconfigure((0, 1, 2, 3), weight=1, uniform="a")  # configure grid system
        self.grid_columnconfigure((0, 1, 2), weight=1, uniform="a")

        self.label = ctk.CTkLabel(self, text="", font=("Arial", 40), )
        self.label.grid(row=0, column=0, columnspan=3, padx=20, pady=10, sticky="nsew")
        self.number = 31
        self.counter = 0

        self.label1 = ctk.CTkLabel(self, text="Нажмите старт", font=("Arial", 40), )
        self.label1.grid(row=1, column=0, columnspan=3, padx=20, pady=10, sticky="nsew")

        self.button1 = ctk.CTkButton(master=self, text="Старт", font=("Arial", 20), height=50, command=self.start)
        self.button1.grid(row=3, column=0, columnspan=2, padx=5, pady=10, sticky="we")
        self.button1.bind("<Button-1>", self.random_multiplication)

        self.btn_exit = ctk.CTkButton(master=self, text="Выход", font=("Arial", 20), height=50, command=self.destroy,
                                      fg_color="#B22222", hover_color="#DC143C",)
        self.btn_exit.grid(row=3, column=2,  padx=5, pady=10, sticky="we")

        self.btn1 = ctk.CTkButton(master=self, text="", height=50, font=("Arial", 20), )
        self.btn2 = ctk.CTkButton(master=self, text="", height=50, font=("Arial", 20), )
        self.btn3 = ctk.CTkButton(master=self, text="", height=50, font=("Arial", 20), )

    def random_multiplication(self, e):
        while True:
            lst = [f"{randint(2, 9)} * {randint(2, 9)}" for _ in range(3)]
            if len(set([eval(i) for i in lst])) == 3:
                break
        self.label1.configure(text=f"{lst[0]} = ?")
        shuffle(lst)
        self.btn1.configure(text=eval(lst[0]), command=lambda t=eval(lst[0]): self.click(t))
        self.btn2.configure(text=eval(lst[1]), command=lambda t=eval(lst[1]): self.click(t))
        self.btn3.configure(text=eval(lst[2]), command=lambda t=eval(lst[2]): self.click(t))
        self.btn1.grid(row=3, column=0, padx=5, pady=10, sticky="we")
        self.btn2.grid(row=3, column=1, padx=5, pady=10, sticky="we")
        self.btn3.grid(row=3, column=2, padx=5, pady=10, sticky="we")

    def rgb_color(self):
        return "#" + "".join(choices("0123456789ABCDEF", k=6))

    def click(self, text):
        if text == eval(self.label1.cget("text").split("=")[0]):
            self.label.configure(text_color=self.rgb_color())
            self.counter += 1
        self.random_multiplication(None)

    def start(self):
        self.number = 31
        self.counter = 0
        self.button1.grid_forget()
        self.btn_exit.grid_forget()
        self.update_clock()

    def my_grid(self):
        self.button1.grid(row=3, column=0, columnspan=2, padx=5, pady=10, sticky="we")
        self.btn_exit.grid(row=3, column=2, padx=5, pady=10, sticky="we")

    def update_clock(self):
        if self.number == 0:
            self.label.configure(text_color='gray84')
            self.label1.configure(font=("Arial", 30), text=f"Правильных ответов: {self.counter}")
            self.btn1.grid_forget()
            self.btn2.grid_forget()
            self.btn3.grid_forget()
            self.after(3000, self.my_grid())
            return
        self.number -= 1
        self.label.configure(text=str(self.number))
        self.after(1000, self.update_clock)


if __name__ == "__main__":
    app = Timer()
    app.mainloop()
