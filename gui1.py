from tkinter import *
import csv


class GUI:
    def __init__(self, window):
        """
        - The code provided is meant to guide you on the dimensions used and variable names standards.
        - Add the widgets responsible for the name, status, and save button.
        """
        self.window = window

        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text='Name')
        self.entry_name = Entry(self.frame_name)
        self.label_name.pack(padx=5, side='left')
        self.entry_name.pack(padx=5, side='left')
        self.frame_name.pack(anchor='w', pady=10)   # anchor='w' helps to change the frame position from center to west.

        self.frame_age = Frame(self.window)
        self.label_age = Label(self.frame_age, text='Age')
        self.entry_age = Entry(self.frame_age)
        self.label_age.pack(padx=5, side='left')
        self.entry_age.pack(padx=16, side='left')
        self.frame_age.pack(anchor='w', pady=10)

        self.frame_grade = Frame(self.window)
        self.label_grade = Label(self.frame_grade, text='Grade')
        self.entry_grade = Entry(self.frame_grade)
        self.label_grade.pack(padx=5, side='left')
        self.entry_grade.pack(padx=16, side='left')
        self.frame_grade.pack(anchor='w', pady=10)

        '''
        self.frame_middle = Frame(self.window)
        self.label_name3 = Label(self.frame_middle, text='Status')
        self.radio_1 = IntVar()
        self.radio_1.set(-1)
        self.radio_Student = Radiobutton(self.frame_middle, text='Student', variable=self.radio_1, value=0)
        self.radio_Staff = Radiobutton(self.frame_middle, text='Staff', variable=self.radio_1, value=1)
        self.radio_Both = Radiobutton(self.frame_middle, text='Both', variable=self.radio_1, value=2)
        self.label_name3.pack(padx=5, side='left')
        self.radio_Student.pack(side='left')
        self.radio_Staff.pack(side='left')
        self.radio_Both.pack(side='left')
        self.frame_middle.pack()
        '''

        self.frame_middle = Frame(self.window)
        self.label_name3 = Label(self.frame_middle, text='Status')

        options = ['Select One', 'Student', 'Staff', 'Both']

        clicked = StringVar()
        clicked.set(options[0])
        self.drop = OptionMenu(window, clicked, *options)
        self.drop.pack()
        self.frame_middle.pack()

        self.frame_bottom = Frame(self.window)
        self.button_save = Button(self.frame_bottom, text='Save', command=self.clicked)
        self.button_save.pack()
        self.frame_bottom.pack()

    def clicked(self):
        data = []
        name = self.entry_name.get()
        age = self.entry_age.get()
        grade = self.entry_grade.get()
        status = self.clicked

        age = int(age)

        if status == 0:
            status = "Didn't choose a correct option"
        elif status == 1:
            status = 'Student'
        elif status == 2:
            status = 'Staff'
        elif status == 3:
            status = 'Both'

        data.append(name)
        data.append(age)
        data.append(grade)
        data.append(status)

        with open('records.csv', 'a', newline='') as csvfile:
            content = csv.writer(csvfile)
            content.writerow(data)

        self.entry_name.delete(0, END)
        self.entry_age.delete(0, END)
        self.entry_grade.delete(0, END)

