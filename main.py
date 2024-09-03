import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configurações da janela
        self.title("Calculadora")
        self.geometry("400x600")
        self.configure(bg="#1F1B24")
        self.resizable(False, False)

        # Variável para o display
        self.equation = ""

        # Display
        self.display = tk.Label(self, text="", anchor=tk.E, bg="#272132", fg="#9F7AEA", 
                                font=("Courier", 30, "bold"), relief=tk.SUNKEN, padx=10, pady=10)
        self.display.pack(expand=True, fill="both", padx=10, pady=10)

        # Criação dos botões
        button_frame = tk.Frame(self, bg="#1F1B24")
        button_frame.pack(expand=True, fill="both")

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['C']
        ]

        for row in buttons:
            button_row = tk.Frame(button_frame, bg="#1F1B24")
            button_row.pack(expand=True, fill="both")
            for button_text in row:
                button = tk.Button(
                    button_row, text=button_text, font=("Courier", 20, "bold"), fg="#FFFFFF", bg="#6B46C1",
                    activebackground="#805AD5", activeforeground="#FFFFFF",
                    command=lambda text=button_text: self.on_button_click(text),
                    relief=tk.RAISED, borderwidth=2
                )
                button.pack(side=tk.LEFT, expand=True, fill="both", padx=5, pady=5)

    def on_button_click(self, char):
        if char == "C":
            self.equation = ""
        elif char == "=":
            try:
                self.equation = str(eval(self.equation))
            except ZeroDivisionError:
                self.equation = "Erro: Div/0"
            except Exception as e:
                self.equation = "Erro"
        else:
            self.equation += str(char)
        
        self.update_display()

    def update_display(self):
        self.display.config(text=self.equation)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
