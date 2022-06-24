import tkinter as tk
from tkinter import filedialog

class App:
    path = None

    def __init__(self) -> None:
        self.app = tk.Tk()
        self.app.geometry("1025x765")

        self._component1_()
        self._component2_()

        self.app.mainloop()

    def _component1_(self):
        app = self.app

        title = tk.Label(app, text='Check Similarity Source Code',
                         font=('Arial', 20, 'bold'))
        title.place(x=340, y=30)

        pathLabel = tk.Label(app, text='Path Files', font=('Arial', 12, 'normal'))
        pathLabel.place(x=55, y=100)

        extentionLabel = tk.Label(app, text='Extention Files', font=('Arial', 12, 'normal'))
        extentionLabel.place(x=55, y=150)

        toleranceLabel = tk.Label(app, text='Tolerance Score', font=('Arial', 12, 'normal'))
        toleranceLabel.place(x=55, y=200)


        self.pathEntry = tk.Entry(app, font=('Arial', 11, 'normal'))
        self.pathEntry.place(x=200, y=100, width=500, height=28)

        # self.extentionEntry = tk.Entry(app, font=('Arial', 11, 'normal'))
        # self.extentionEntry.place(x=200, y=150, width=100, height=28)
        self._file_extention_()

        self.toleranceEntry = tk.Entry(app, font=('Arial', 11, 'normal'))
        self.toleranceEntry.place(x=200, y=200, width=70, height=28)

        dirButton = tk.Button(app, text='Open', command=self._open_dir_)
        dirButton.place(x=710, y=100)

        execButton = tk.Button(app, text='Check', command=self._check_)
        execButton.place(x=200, y=245, width=100, height=35)

    def _file_extention_(self):
        options = [
            '.txt', '.java', '.c++'
        ]
        clicked = tk.StringVar()
        
        # initial menu text
        clicked.set( options[0] )
        self.extentionEntry = tk.OptionMenu(self.app, clicked, *options)
        self.extentionEntry.place(x=200, y=145, width=100, height=35)

    def _open_dir_(self):
        folder_selected = filedialog.askdirectory(initialdir='./')
        self.pathEntry.delete(0, 'end')
        self.pathEntry.insert(0, folder_selected)


    def _component2_(self):
        app = self.app

        self.frameLeft = tk.Frame(app, bg="White", borderwidth=3)
        self.frameLeft.place(x=15, y=300, width=200, height=430)

        self.frameRight = tk.Frame(app, bg="White", borderwidth=3)
        self.frameRight.place(x=220, y=300, width=790, height=430)

    def _check_(self):
        pass

App()
