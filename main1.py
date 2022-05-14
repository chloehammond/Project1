from gui1 import *


def main() -> None:
    window = Tk()
    window.title('Hammond - Project 1')
    window.geometry('350x180')
    widgets = GUI(window)
    window.resizable(False, False)

    window.mainloop()


if __name__ == '__main__':
    """
    Function to call the main function, which accesses the GUI window
    """

    main()
