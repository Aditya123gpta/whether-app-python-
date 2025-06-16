
import tkinter as tk
import math

class ScientificCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Advanced Scientific Calculator")
        self.geometry("450x600")
        self.resizable(False, False)
        self.configure(bg="#282c34")

        self.total_expression = ""
        self.current_expression = ""

        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()

        self.buttons_frame = self.create_buttons_frame()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.operations = {
            '÷': "\u00F7",
            '×': "\u00D7",
            '-': '-',
            '+': '+'
        }
        self.buttons = {}
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.create_scientific_buttons()

        self.bind_keys()

    def bind_keys(self):
        self.bind("<Return>", lambda event: self.evaluate())
        self.bind("<BackSpace>", lambda event: self.backspace())
        for key in '1234567890.+-*/':
            self.bind(key, lambda event, digit=key: self.add_to_expression(digit))
        self.bind('c', lambda event: self.clear())
        self.bind('C', lambda event: self.clear())

    def create_display_frame(self):
        frame = tk.Frame(self, height=120, bg="#1e2127")
        frame.pack(expand=True, fill="both")
        return frame

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg="#1e2127", fg="#aaaaaa", padx=24, font=("Arial", 16))
        total_label.pack(expand=True, fill="both")
        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg="#1e2127", fg="white", padx=24, font=("Arial", 40, "bold"))
        label.pack(expand=True, fill="both")
        return total_label, label

    def create_buttons_frame(self):
        frame = tk.Frame(self)
        frame.pack(expand=True, fill="both")
        frame.configure(bg="#282c34")
        for x in range(6):
            frame.rowconfigure(x, weight=1)
        for x in range(4):
            frame.columnconfigure(x, weight=1)
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg="#3a3f4b", fg="white", font=("Arial", 24), borderwidth=0,
                               command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)
            self.buttons[str(digit)] = button

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=operator, bg="#fe9505", fg="white", font=("Arial", 24), borderwidth=0,
                               command=lambda x=symbol: self.add_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            self.buttons[operator] = button
            i += 1

    def add_operator(self, operator):
        if self.current_expression == "":
            return
        if self.current_expression[-1] in "+-×÷":
            self.current_expression = self.current_expression[:-1]
        self.current_expression += operator
        self.update_label()

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def create_special_buttons(self):
        clear_button = tk.Button(self.buttons_frame, text="C", bg="#d33f49", fg="white", font=("Arial", 24), borderwidth=0, command=self.clear)
        clear_button.grid(row=0, column=1, sticky=tk.NSEW)

        equal_button = tk.Button(self.buttons_frame, text="=", bg="#00b894", fg="white", font=("Arial", 24), borderwidth=0, command=self.evaluate)
        equal_button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

        backspace_button = tk.Button(self.buttons_frame, text="⌫", bg="#636e72", fg="white", font=("Arial", 24), borderwidth=0, command=self.backspace)
        backspace_button.grid(row=0, column=0, sticky=tk.NSEW)

        open_paren_button = tk.Button(self.buttons_frame, text="(", bg="#636e72", fg="white", font=("Arial", 24), borderwidth=0,
                                     command=lambda: self.add_to_expression('('))
        open_paren_button.grid(row=0, column=2, sticky=tk.NSEW)

        close_paren_button = tk.Button(self.buttons_frame, text=")", bg="#636e72", fg="white", font=("Arial", 24), borderwidth=0,
                                      command=lambda: self.add_to_expression(')'))
        close_paren_button.grid(row=0, column=3, sticky=tk.NSEW)

    def backspace(self):
        self.current_expression = self.current_expression[:-1]
        self.update_label()

    def create_scientific_buttons(self):
        # Row 5 for these buttons
        sci_funcs = [
            ("sin", self.sin),
            ("cos", self.cos),
            ("tan", self.tan),
            ("log", self.log),  # Base 10 logarithm
            ("ln", self.ln),    # Natural logarithm
            ("√", self.sqrt),
            ("x²", self.square),
            ("xʸ", self.power),
            ("!", self.factorial)
        ]

        for i, (text, func) in enumerate(sci_funcs):
            button = tk.Button(self.buttons_frame, text=text, bg="#6c5ce7", fg="white", font=("Arial", 14, "bold"), borderwidth=0, command=func)
            button.grid(row=5, column=i % 4, sticky=tk.NSEW, padx=1, pady=1)

    def sin(self):
        try:
            value = float(self.current_expression)
            result = math.sin(math.radians(value))
            self.current_expression = str(result)
            self.update_label()
        except:
            self.display_error()

    def cos(self):
        try:
            value = float(self.current_expression)
            result = math.cos(math.radians(value))
            self.current_expression = str(result)
            self.update_label()
        except:
            self.display_error()

    def tan(self):
        try:
            value = float(self.current_expression)
            result = math.tan(math.radians(value))
            self.current_expression = str(result)
            self.update_label()
        except:
            self.display_error()

    def log(self):
        try:
            value = float(self.current_expression)
            if value <= 0:
                raise ValueError
            result = math.log10(value)
            self.current_expression = str(result)
            self.update_label()
        except:
            self.display_error()

    def ln(self):
        try:
            value = float(self.current_expression)
            if value <= 0:
                raise ValueError
            result = math.log(value)
            self.current_expression = str(result)
            self.update_label()
        except:
            self.display_error()

    def sqrt(self):
        try:
            value = float(self.current_expression)
            if value < 0:
                raise ValueError
            result = math.sqrt(value)
            self.current_expression = str(result)
            self.update_label()
        except:
            self.display_error()

    def square(self):
        try:
            value = float(self.current_expression)
            result = value ** 2
            self.current_expression = str(result)
            self.update_label()
        except:
            self.display_error()

    def power(self):
        # User must input base, press xʸ button, then input exponent
        if self.current_expression == "" or self.current_expression[-1] in "+-×÷^":
            return
        self.current_expression += "^"
        self.update_label()

    def factorial(self):
        try:
            value = int(float(self.current_expression))
            if value < 0:
                raise ValueError
            result = math.factorial(value)
            self.current_expression = str(result)
            self.update_label()
        except:
            self.display_error()

    def display_error(self):
        self.current_expression = "Error"
        self.update_label()

    def evaluate(self):
        self.total_expression = self.current_expression
        try:
            # Replace symbols with python operators
            expression = self.current_expression.replace('÷', '/').replace('×', '*').replace('^', '**')
            result = str(eval(expression))
            self.current_expression = result
            self.update_label()
            self.update_total_label()
        except Exception as e:
            self.display_error()

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(symbol, operator)
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])


if __name__ == "__main__":
    calc = ScientificCalculator()
    calc.mainloop()
                                        

    


          
                        
                          

















