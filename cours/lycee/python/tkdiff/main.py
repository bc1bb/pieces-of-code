#!/usr/bin/env python3

import difflib
import tkinter
import tkinter.filedialog
import tkinter.messagebox
import socket
import os
import sys
import threading


def getIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Open a socket so we can catch our local IP
    s.settimeout(0)
    try:
        s.connect(("255.255.255.255", 1))
        # IP that does not exist, so we don't annoy anything
        ip = s.getsockname()[0]
    except:
        ip = "127.0.0.1"
        # In case of error, IP is 127.0.0.1
    finally:
        s.close()
    return ip


class DiffWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("TkDiff")
        self.master.minsize(340, 510)
        # Create window

        self.f1 = "/"
        self.f2 = "/"
        # Basic variables for location of master and slave files

        self.line1 = tkinter.Frame(self.master)
        self.fileBtn1 = tkinter.Button(
            self.line1, text="Master File", command=self.fileSelctMaster
        )
        self.fileBtn2 = tkinter.Button(
            self.line1, text="Slave File", command=self.fileSlctSlave
        )
        self.valBtn = tkinter.Button(
            self.line1, text="Calculate difference", command=self.calcDiff
        )
        # We create a tkinter.Frame that will contain the first line of graphical elements (buttons)
        # and bind functions to them

        self.line2 = tkinter.Frame(self.master)
        self.ipEntry = tkinter.Entry(self.line2)
        self.connectBtn = tkinter.Button(self.line2, text="Send", command=self.connect)
        # We create a Frame that will contain the second line of elements (button and text box)

        self.diffFrame = tkinter.Frame(self.master)
        self.diffBox = tkinter.Text(self.diffFrame, state=tkinter.DISABLED)
        self.diffBox.bind("<Button-1>", self.whereAmI)
        # Now a Frame for diffBox (text box to show diff)

        self.bottomBar = tkinter.Frame(self.master, bd=1, relief=tkinter.SUNKEN)
        self.ipLabel = tkinter.Label(
            self.bottomBar, text="IP Address: " + getIP(), anchor=tkinter.W
        )
        self.charLabel = tkinter.Label(self.bottomBar, text="0:0", anchor=tkinter.W)
        # Finally, a Frame that will contain two labels, one to tell user what his IP is
        # And a second one to tell where the cursor is when clicking on text (L:C)

        self.line1.pack(side=tkinter.TOP)
        self.fileBtn1.pack(side=tkinter.LEFT)
        self.fileBtn2.pack(side=tkinter.LEFT)
        self.valBtn.pack(side=tkinter.LEFT)
        # Tell Tkinter to show what we have declared for the first line

        self.line2.pack(side=tkinter.TOP)
        self.ipEntry.pack(side=tkinter.LEFT)
        self.connectBtn.pack(side=tkinter.LEFT)
        # Same for second line

        self.diffFrame.pack(expand=True, fill=tkinter.BOTH)
        self.diffBox.pack(expand=True, fill=tkinter.BOTH)
        # Same for diffBox and it's Frame

        self.bottomBar.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        self.ipLabel.pack(side=tkinter.LEFT)
        self.charLabel.pack(side=tkinter.RIGHT)
        # Same for bottom bar and its content

        self.diffServerThread = threading.Thread(target=self.diffServer)
        self.diffServerThread.daemon = True
        self.diffServerThread.start()
        # Start listening for connection in a separate thread

    def fileSelctMaster(self):
        self.f1 = tkinter.filedialog.askopenfilename(
            title="Select primary file",
            initialdir=os.getcwd(),
            filetypes=[("All Files", "*.*"), ("Diff files (*.diff)", "*.diff")],
        )
        # Select master file

        if self.f1.endswith(".diff"):
            self.calcDiff()
        return

    def fileSlctSlave(self):
        self.f2 = tkinter.filedialog.askopenfilename(
            title="Select secondary file",
            initialdir=os.getcwd(),
            filetypes=[("All Files", "*.*")],
        )
        # Select slave file
        return

    def whereAmI(self, oui):
        # fmt:off
        self.charLabel["text"] = str(self.diffBox.index(tkinter.CURRENT)).replace(".", ":")
        # fmt:on
        # Tell user where his cursor is when clicking diffBox
        return

    def connect(self):
        toSend = str(self.diffBox.get(1.0, tkinter.END)).encode("utf-8")
        # Encode in UTF-8 a string that contains content of diffBox

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.ipEntry.get(), 42000))
            s.send(toSend)
            # send encoded content to server asked by user
        except:
            self.handleErrors("connect")
            # In case of error show it in a popup
            return

        return

    def changeDiffBox(self, text):
        self.diffBox["state"] = tkinter.NORMAL
        self.diffBox.delete(1.0, tkinter.END)
        self.diffBox.insert(tkinter.END, text)
        self.diffBox["state"] = tkinter.DISABLED
        # Enables edits in diffBox, cleans, adds text, disables it again

    def diffServer(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            s.bind(("0.0.0.0", 42000))
            s.listen()
        except:
            self.handleErrors("diffServer")
            # In case of error show it in a popup
            return
        try:
            while True:
                c, addr = s.accept()
                # Accept connection when one is coming
                while True:
                    data = c.recv(1024)
                    tkinter.messagebox.showinfo(
                        "Diff Received!", "Diff Received from " + str(addr[0]) + "!"
                    )

                    self.changeDiffBox(data.decode("utf-8"))
                    # Decode data and put it in diffBox

                    if data != b"":
                        break
                        # break connection when no more content is sent
        except:
            self.handleErrors("diffServer")
            # In case of error show it in a popup
            return

    def calcDiff(self):
        if self.f1 == "/":
            tkinter.messagebox.showerror("Error (calcDiff)", "Please select two files.")
            # If user did not select two files
            return

        try:
            if self.f1.endswith(".diff") and self.f2 == "/":
                # If user has selected a dot diff file (file that contains diff) print it in diffBox
                # But also store it in case user would want diff between diff files (lol)
                f = open(self.f1).readlines()

                content = ""
                for i in f:
                    content += i

                self.changeDiffBox(content)
                return  # Drop function here
            else:
                f1 = open(self.f1).readlines()
                f2 = open(self.f2).readlines()
        except:
            self.handleErrors("calcDiff")
            return

        if "\r\n" in (f1, f2):
            nl = "\r\n"  # CRLF (Windows)
        elif "\r" in (f1, f2):
            nl = "\r"  # CR (macOS)
        else:
            nl = "\n"  # LF (Linux)
        # Detects different types of new lines characters in file

        diff = ""
        for line in difflib.unified_diff(f1, f2, lineterm=nl):
            diff += line + "\n"
        # Calculates difference between files and puts it in a string

        self.changeDiffBox(diff)
        return

    def handleErrors(self, func):
        # fmt:off
        err = (
                str(sys.exc_info()[0]) + "\n" +
                str(sys.exc_info()[1]) + "\n" +
                str(sys.exc_info()[2])
        )
        # fmt:on
        tkinter.messagebox.showerror("Error (" + func + ")", "Traceback :\n" + err)
        # In case of error show it in a popup


if __name__ == "__main__":
    # Only when calling file, will not do anything if file is imported from another script
    root = tkinter.Tk()
    window = DiffWindow(root)
    root.mainloop()
    # Starts window
