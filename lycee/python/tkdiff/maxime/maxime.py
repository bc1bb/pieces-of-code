#!/usr/bin/env python3

import tkinter
import tkinter.messagebox
import serial


class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.minsize(150, 150)
        # Create window

        self.ser = serial.Serial("COM1", 9600, timeout=1)

        self.line1 = tkinter.Frame(self.master)
        self.firstLbl = tkinter.Label(self.line1, text="First Number")
        self.firstEntry = tkinter.Entry(self.line1)

        self.line2 = tkinter.Frame(self.master)
        self.secondLbl = tkinter.Label(self.line2, text="Second Number")
        self.secondEntry = tkinter.Entry(self.line2)

        self.line3 = tkinter.Frame(self.master)
        self.opVar = tkinter.StringVar()
        self.opVar.set("x")
        self.multiBtn = tkinter.Radiobutton(self.line3, variable=self.opVar, value="x", text="x")
        self.additionBtn = tkinter.Radiobutton(self.line3, variable=self.opVar, value="+", text="+")
        self.divideBtn = tkinter.Radiobutton(self.line3, variable=self.opVar, value="/", text="/")
        self.minusBtn = tkinter.Radiobutton(self.line3, variable=self.opVar, value="-", text="-")

        self.line4 = tkinter.Frame(self.master)
        self.calculateBtn = tkinter.Button(self.line4, command=self.calculate, text="Calculate !")

        self.line1.pack(side=tkinter.TOP, fill=tkinter.BOTH)
        self.firstLbl.pack(side=tkinter.LEFT)
        self.firstEntry.pack(side=tkinter.RIGHT)

        self.line2.pack(side=tkinter.TOP, fill=tkinter.BOTH)
        self.secondLbl.pack(side=tkinter.LEFT)
        self.secondEntry.pack(side=tkinter.RIGHT)

        self.line3.pack(side=tkinter.TOP, anchor=tkinter.CENTER)
        self.multiBtn.pack(side=tkinter.LEFT)
        self.additionBtn.pack(side=tkinter.LEFT)
        self.divideBtn.pack(side=tkinter.LEFT)
        self.minusBtn.pack(side=tkinter.LEFT)

        self.line4.pack(side=tkinter.TOP, fill=tkinter.BOTH)
        self.calculateBtn.pack(side=tkinter.TOP, fill=tkinter.BOTH)

    def calculate(self):
        op = self.opVar.get()
        res = 0

        if op == "x":
            res = int(self.firstEntry.get()) * int(self.secondEntry.get())
        elif op == "/":
            res = int(self.firstEntry.get()) / int(self.secondEntry.get())
        elif op == "+":
            res = int(self.firstEntry.get()) + int(self.secondEntry.get())
        elif op == "-":
            res = int(self.firstEntry.get()) - int(self.secondEntry.get())

        text = self.firstEntry.get() + op + self.secondEntry.get() + "=" + str(res)
        tkinter.messagebox.showinfo("Calculator", text)

        if self.ser.writable():
            if res == 10:
                self.ser.write(str(1).encode("utf-8"))
            else:
                self.ser.write(str(0).encode("utf-8"))


if __name__ == "__main__":
    # Only when calling file, will not do anything if file is imported from another script
    root = tkinter.Tk()
    window = Calculator(root)
    root.mainloop()
    # Starts window
