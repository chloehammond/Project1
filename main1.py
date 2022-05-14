from gui import *


def main():
    window = Tk()
    window.title('Lab 10')
    window.geometry('350x180')
    widgets = GUI(window)
    window.resizable(False, False)

    window.mainloop()


if __name__ == '__main__':
    main()
