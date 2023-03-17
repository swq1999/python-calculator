import customtkinter as ctk
from tkinter import messagebox


class Calculator(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Creating window
        self.geometry("360x500")
        self.resizable(False, False)
        self.wm_title("Calculator")

        # Creating grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)  


        # Creating display
        self.display = ctk.CTkEntry(
            self.master,
            font=("Helvetica bold", 50),
            width=320,
            height=80,
            state="normal",
            corner_radius=10,
            )
        
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=(10,5), sticky="nsew")


        # create buttons
        my_font = ("Helvetica bold", 30)
        self.clear = ctk.CTkButton(self.master, text="AC", font=my_font, width=79, height=70, command=lambda: clear())
        self.negative = ctk.CTkButton(self.master, text="(", font=my_font, width=79, height=70, command=lambda: btn_click("("))
        self.percent = ctk.CTkButton(self.master, text=")", font=my_font, width=79, height=70, command=lambda: btn_click(")"))
        self.divide = ctk.CTkButton(self.master, text="/", font=my_font, width=79, height=70, command=lambda: btn_click("/"))
        
        self.num1 = ctk.CTkButton(self.master, text="1", font=my_font, width=79, height=70, command=lambda: btn_click("1"))
        self.num2 = ctk.CTkButton(self.master, text="2", font=my_font, width=79, height=70, command=lambda: btn_click("2"))
        self.num3 = ctk.CTkButton(self.master, text="3", font=my_font, width=79, height=70, command=lambda: btn_click("3"))
        self.multiply = ctk.CTkButton(self.master, text="x", font=my_font, width=79, height=70, command=lambda: btn_click("*"))
        
        self.num4 = ctk.CTkButton(self.master, text="4", font=my_font, width=79, height=70, command=lambda: btn_click("4"))
        self.num5 = ctk.CTkButton(self.master, text="5", font=my_font, width=79, height=70, command=lambda: btn_click("5"))
        self.num6 = ctk.CTkButton(self.master, text="6", font=my_font, width=79, height=70, command=lambda: btn_click("6"))
        self.subtract = ctk.CTkButton(self.master, text="-", font=my_font, width=79, height=70, command=lambda: btn_click("-"))
        
        self.num7 = ctk.CTkButton(self.master, text="7", font=my_font, width=79, height=70, command=lambda: btn_click("7"))
        self.num8 = ctk.CTkButton(self.master, text="8", font=my_font, width=79, height=70, command=lambda: btn_click("8"))
        self.num9 = ctk.CTkButton(self.master, text="9", font=my_font, width=79, height=70, command=lambda: btn_click("9"))
        self.add = ctk.CTkButton(self.master, text="+", font=my_font, width=79, height=70, command=lambda: btn_click("+"))
        
        self.decimal = ctk.CTkButton(self.master, text=".", font=my_font, width=79, height=70, command=lambda: btn_click("."))
        self.num0 = ctk.CTkButton(self.master, text="0", font=my_font, width=79, height=70, command=lambda: btn_click("0"))
        self.delete = ctk.CTkButton(self.master, text="<<", font=my_font, width=79, height=70, command=lambda: delete())
        self.equals = ctk.CTkButton(self.master, text="=", font=my_font, width=79, height=70, command=lambda: calculate())


        # add buttons to the grid
        self.clear.grid(row=1, column=0, columnspan=1, padx=(10,5), pady=5, sticky="nsew")
        self.negative.grid(row=1, column=1, columnspan=1, padx=5, pady=5, sticky="nsew")
        self.percent.grid(row=1, column=2, columnspan=1, padx=5, pady=5, sticky="nsew")
        self.divide.grid(row=1, column=3, columnspan=1, padx=(5,10), pady=5, sticky="nsew")
        
        self.num1.grid(row=2, column=0, columnspan=1, padx=(10,5), pady=5, sticky="nsew")
        self.num2.grid(row=2, column=1, columnspan=1, padx=5, pady=5, sticky="nsew")
        self.num3.grid(row=2, column=2, columnspan=1, padx=5, pady=5, sticky="nsew")
        self.multiply.grid(row=2, column=3, columnspan=1, padx=(5,10), pady=5, sticky="nsew")
        
        self.num4.grid(row=3, column=0, columnspan=1, padx=(10,5), pady=5, sticky="nsew")
        self.num5.grid(row=3, column=1, columnspan=1, padx=5, pady=5, sticky="nsew")
        self.num6.grid(row=3, column=2, columnspan=1, padx=5, pady=5, sticky="nsew")
        self.subtract.grid(row=3, column=3, columnspan=1, padx=(5,10), pady=5, sticky="nsew")
        
        self.num7.grid(row=4, column=0, columnspan=1, padx=(10,5), pady=5, sticky="nsew")
        self.num8.grid(row=4, column=1, columnspan=1, padx=5, pady=5, sticky="nsew")
        self.num9.grid(row=4, column=2, columnspan=1, padx=5, pady=5, sticky="nsew")
        self.add.grid(row=4, column=3, columnspan=1, padx=(5,10), pady=5, sticky="nsew")
        
        self.decimal.grid(row=5, column=0, columnspan=1, padx=(10,5), pady=(5,10), sticky="nsew")
        self.num0.grid(row=5, column=1, columnspan=1, padx=5, pady=(5,10), sticky="nsew")
        self.delete.grid(row=5, column=2, columnspan=1, padx=5, pady=(5,10), sticky="nsew")
        self.equals.grid(row=5, column=3, columnspan=1, padx=(5,10), pady=(5,10), sticky="nsew")


        # All methods
        self.equation = ""

        def btn_click(click):
            global index
            global equation
            self.equation += click
            self.display.insert("end", click)

        
        def clear():
            global equation
            global index
            self.display.delete(0,"end")
            self.equation = ""

        
        def calculate():
            try:
                global equation
                result = ""
                result = eval(self.equation)
                clear()
                self.display.insert(0, result)
                self.equation = str(result)
            except ZeroDivisionError:
                messagebox.showerror(title="Error", message="Cannot divide by zero")
                raise ZeroDivisionError("Cannot divide by zero")
            except:
                messagebox.showerror(title="Error", message="Invalid equation")
                raise ValueError("Error: Invalid equation")


        def delete():
            global equation
            self.equation = self.equation[:-1]
            value = self.display.get()
            value = value[:-1]
            self.display.delete(0,"end")
            self.display.insert(0, value)


def main():
    app = Calculator()
    app.mainloop()


if __name__ == "__main__":
    main()

# get random forest model