# Kalkulator 3.0
# Wersja z GUI

import sys

from tkinter import *
# importuję messagebox celem obsługi błędów
from tkinter import messagebox

class Application(Frame):
    """ Aplikacja z GUI pozwalająca na proste obliczenia"""

    def __init__(self, master):
        """ inicjalizuję ramkę """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    # tworzę funkcję kalkulującą
    def Calculation(self):

        #z okna self.display pobieram wprowadzone dane
        self.calculation = self.display.get()
        #dodaję zamianę % na /100 aby można było szybko wyliczać procent
        self.calculation = self.calculation.replace("%", "/100")

        # za pomocą funkcji eval obliczam wyrażenie wpisane
        # w self.calculation (self.display)
        try:
            self.result = eval(self.calculation)
            # następnie wyświetlam wynik i doświeżam w oknie
            # za pomocą self.Replace
            self.Replace(self.result)
        except:
            messagebox.showinfo("Error", "Invalid input")

    # za pomocą funkcji Replace usuwam wcześniejszą treść display
    # i zastępuję nową treścią
    def Replace(self, text):
        self.display.delete(0, END)
        self.display.insert(0, text)

    def Append(self, text):
        self.entryText = self.display.get()
        self.textLenght = len(self.entryText)

        if self.entryText == "0":
            self.Replace(text)
        else:
            self.display.insert(self.textLenght, text)

    def Cancel(self):
        actual_state = self.display.get()
        new_state = actual_state[:len(actual_state)-1]
        self.display.delete(0, END)
        self.display.insert(0, new_state)

    def Clear(self):
        self.Replace("0")



    def create_widgets(self):

        self.display = Entry(self, font=("Helvetica", 16), borderwidth=0, relief=RAISED, justify=RIGHT)
        self.display.insert(0, "0")
        self.display.grid(row=0, column=0, columnspan=5)

        # Tworzę przycisk równiania i w komendzie
        # przypisuję lambdę z wyrażeniem wpisanym do self.Calculation
        self.Equal = Button(self, text = "=", command = lambda: self.Calculation())
        self.Equal.grid(row = 3, column = 4, rowspan = 2, sticky = "NWNESWSE")

        self.Seven = Button(self, text = "7", command = lambda: self.Append("7"))
        self.Seven.grid(row = 1, column = 0, sticky = "NWNESWSE")

        self.Eight = Button(self, text = "8", command = lambda: self.Append("8"))
        self.Eight.grid(row = 1, column = 1, sticky = "NWNESWSE")

        self.Nine = Button(self, text = "9", command = lambda: self.Append("9"))
        self.Nine.grid(row = 1, column = 2, sticky = "NWNESWSE")

        self.Four = Button(self, text = "4", command = lambda: self.Append("4"))
        self.Four.grid(row = 2, column = 0, sticky = "NWNESWSE")

        self.Five = Button(self, text = "5", command = lambda: self.Append("5"))
        self.Five.grid(row = 2, column = 1, sticky = "NWNESWSE")

        self.Six = Button(self, text = "6", command = lambda: self.Append("6"))
        self.Six.grid(row = 2, column = 2, sticky = "NWNESWSE")

        self.One = Button(self, text = "1", command = lambda: self.Append("1"))
        self.One.grid(row = 3, column = 0, sticky = "NWNESWSE")

        self.Two = Button(self, text = "2", command = lambda: self.Append("2"))
        self.Two.grid(row = 3, column = 1, sticky = "NWNESWSE")

        self.Three = Button(self, text = "3", command = lambda: self.Append("3"))
        self.Three.grid(row = 3, column = 2, sticky = "NWNESWSE")

        self.Zero = Button(self, text = "0", command = lambda: self.Append("0"))
        self.Zero.grid(row = 4, column = 0, sticky = "NWNESWSE")

        self.Cancel = Button(self, text = "C", command = self.Cancel)
        self.Cancel.grid(row = 4, column = 1, sticky = "NWNESWSE")

        self.Clear = Button(self, text = "CE", command = self.Clear)
        self.Clear.grid(row = 4, column = 2, sticky = "NWNESWSE")

        self.Plus = Button(self, text = "+", command = lambda: self.Append("+"))
        self.Plus.grid(row = 3, column = 3, sticky = "NWNESWSE")

        self.Minus = Button(self, text = "-", command = lambda: self.Append("-"))
        self.Minus.grid(row = 2, column = 3, sticky = "NWNESWSE")

        self.Multiply = Button(self, text = "*", command = lambda: self.Append("*"))
        self.Multiply.grid(row = 1, column = 3, sticky = "NWNESWSE")

        self.Divide = Button(self, text = "/", command = lambda: self.Append("/"))
        self.Divide.grid(row = 1, column = 4, sticky = "NWNESWSE")

        self.Percent = Button(self, text = "%", command = lambda: self.Append("%"))
        self.Percent.grid(row = 2, column = 4, sticky = "NWNESWSE")

        self.Dot = Button(self, text = ".", command = lambda: self.Append("."))
        self.Dot.grid(row = 4, column = 3, sticky = "NWNESWSE")
        


# main
root = Tk()
root.title("Kalkulator")
app = Application(root)
root.mainloop()


              
