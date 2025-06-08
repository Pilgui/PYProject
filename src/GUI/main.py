from src.GUI.MainMenuWindow import MainMenuWindow
from src.utils.Properties import Properties

properties = Properties()
main_size = properties.get("window-size")

if(__name__ == "__main__"):
    MainMenuWindow.mainMenu(size=main_size)
