import tkinter as tk
from src.gui.gameGUI import GameGUI
from src.service.rootService import RootService

class Starter:
    def run(self):
        root = tk.Tk()
        rootService = RootService()
        gui = GameGUI(root, rootService)

        root.mainloop()

if __name__ == "__main__":
    starter = Starter()
    starter.run()