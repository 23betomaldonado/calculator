from tkinter import *

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("615x680+400+100")
        self.root.configure(bg='cadet blue')

        self.Mainframe = Frame(self.root, border=18, width=600, height=670, relief=RIDGE, background='powder blue')
        self.Mainframe.grid()
        self.WidgetFrame = Frame(self.root, border=18, width=590, height=660, relief=RIDGE, background='cadet blue')
        self.WidgetFrame.grid()

        self.lblDisplay = Label(self.WidgetFrame, width=30, height=2, background='white', font=('arial', 20, 'bold'), anchor='e')
        self.lblDisplay.grid(row=0, column=0, columnspan=4, padx=10, pady=10)



root = Tk()
app = Calculator(root)
root.mainloop()



