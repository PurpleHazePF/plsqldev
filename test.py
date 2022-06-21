from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt


class MainWindow(QMainWindow):
    # Override class constructor
    def __init__(self):
        # You must call the super class method
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(700, 600))  # Set sizes
        self.setWindowTitle("Работа с QTableWidget")  # Set the window title

        table = QTableWidget(self)  # Create a table
        table.setColumnCount(3)  # Set three columns
        table.setRowCount(3)  # and one row

        # Set the table headers
        table.setHorizontalHeaderLabels(["Header 1", "Header 2", "Header 3"])
        table.resize(700, 400)
        table.move(0, 200)

        # Set the tooltips to headings
        table.horizontalHeaderItem(0).setToolTip("Column 1 ")
        table.horizontalHeaderItem(1).setToolTip("Column 2 ")
        table.horizontalHeaderItem(2).setToolTip("Column 3 ")

        # Set the alignment to the headers
        table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)

        # Fill the first line
        table.setItem(0, 0, QTableWidgetItem("Text in column 1"))
        table.setItem(0, 1, QTableWidgetItem("Text in column 2"))
        table.setItem(0, 2, QTableWidgetItem("Text in column 3"))

        # Do the resize of the columns by content
        table.resizeColumnsToContents()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())

































"""import configparser

name = "Варианты обновления"
# первый шаг:  Получить объект конфигурации
config = configparser.ConfigParser()


config.read("update.ini")
 # Шаг третий:Получить значение опции
try:
   auto = config.get("эль примо","биби")
   noupdate = config.get("эль примо","эдгар")
except Exception as e:
    print(e)
# Шаг 2: Добавьте название раздела
config.add_section('эль примо')
# Шаг третий:Добавить вариант
config.set("эль примо", "эдгар", "хуесос")
config.set("эль примо", "биби", "лофа")
config.set("эль примо", "вольт", "хуесос")
# Шаг 4: Создайте файл конфигурации
file = open("update.ini", mode="w")
config.write(file)
print(">> Конфигурационный файл ini записан успешно")"""