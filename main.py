import cx_Oracle, sys, configparser
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QRadioButton, QButtonGroup, QLabel, \
    QMainWindow, QTableWidget, QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt


def dd():
    pass


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.config = configparser.ConfigParser()
        config = self.config
        try:
            config.read("update.ini")
            tc = config.get("settings", "launch")
            print(tc)
        except Exception:
            config.add_section('settings')
            config.set("settings", "launch", "pass")
            config.set("settings", "dir", "")
            config.set("settings", "instantg", "n")
            config.set("settings", "lastuser", "")
            config.set("settings", "lastport", "")
            config.set("settings", "lasthost", "")
            config.set("settings", "lastsid", "")
            file = open("update.ini", mode="w")
            config.write(file)
            print(2)
        self.setFixedSize(700, 600)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.jpg'))
        self.startBtn = QPushButton(self)
        self.startBtn.setGeometry(QtCore.QRect(200, 100, 300, 80))
        self.startBtn.setText("ВХОД")
        font1 = QtGui.QFont()
        font2 = QtGui.QFont()
        font2.setPointSize(12)
        font1.setPointSize(24)
        self.startBtn.setFont(font1)
        self.exit = QPushButton(self)
        self.exit.setGeometry(QtCore.QRect(200, 200, 300, 80))
        self.exit.setText("ВЫХОД")
        self.exit.setFont(font1)
        self.plsql = QLabel(self)
        self.pix = QtGui.QPixmap("plsql.png")
        self.plsql.setPixmap(self.pix)
        self.plsql.resize(400, 400)
        self.plsql.move(-60, 250)
        self.ins = QLabel(self)
        self.pix = QtGui.QPixmap("ic.png")
        self.ins.setPixmap(self.pix)
        self.ins.resize(400, 400)
        self.ins.move(150, 0)
        self.ins.hide()
        self.test_instant = QPushButton(self)
        self.test_instant.setGeometry(QtCore.QRect(450, 420, 200, 60))
        self.test_instant.setText("ТЕСТ")
        self.test_instant.setFont(font1)
        self.test_instant.hide()
        self.dir = QLineEdit(self)
        self.dir.move(150, 420)
        self.dir.resize(250, 30)
        self.dir.setText(config.get("settings", "dir"))
        self.dir.hide()
        x = 0
        self.con_date = []
        value = ['user', 'password', 'host', 'port', 'SID']
        self.texts = []
        for i in range(5):
            dir = QLineEdit(self)
            text = QLabel(self)
            text.setText(value[i])
            text.move(50, 187 + x)
            dir.move(50, 200 + x)
            dir.resize(250, 30)
            x += 40
            self.con_date.append(dir)
            self.texts.append(dir)
            self.con_date.append(text)
        self.texts[1].setEchoMode(QLineEdit.Password)
        self.dbcon = QPushButton(self)
        self.dbcon.setGeometry(QtCore.QRect(450, 420, 200, 60))
        self.dbcon.setText("CONNECT")
        self.dbcon.setFont(font1)
        self.con_date.append(self.dbcon)
        self.no = QLabel(self)
        self.no.setGeometry(QtCore.QRect(200, 20, 300, 60))
        self.no.setText('неверные данные')
        self.no.setFont(font1)
        self.con_date.append(self.no)
        for i in self.con_date:
            i.hide()
        x = 0
        z = ["SELECT", "UPDATE", "INSERT", "DELETE", "СВОЙ SQL СКРИПТ"]
        self.cmdlist = []
        for i in range(5):
            cmd = QPushButton(self)
            cmd.setGeometry(QtCore.QRect(100, 100 + x, 300, 60))
            cmd.setText(z[i])
            cmd.setFont(font1)
            cmd.hide()
            self.cmdlist.append(cmd)
            x += 70
        self.congrats = QLabel(self)
        self.congrats.setGeometry(QtCore.QRect(200, 20, 300, 60))
        self.congrats.setFont(font2)
        #command's_scripts


        #SELECT
        x = 0
        selectguide = ['таблица', 'колонки (через запятую)', "условия", "сортировка"]
        self.selectgroup = []
        self.selecttexts = []
        for i in range(4):
            dir = QLineEdit(self)
            text = QLabel(self)
            dir.move(0 + x, 70)
            dir.resize(170, 30)
            text.setText(selectguide[i])
            text.move(0 + x, 55)
            self.selecttexts.append(dir)
            self.selectgroup.append(dir)
            self.selectgroup.append(text)
            x += 175
        self.search = QPushButton(self)
        self.search.setGeometry(QtCore.QRect(450, 100, 200, 60))
        self.search.setText("ПОИСК")
        self.search.setFont(font1)
        self.selectgroup.append(self.search)
        print(self.selectgroup)
        self.search.clicked.connect(self.SELECTBUTTON)
        #TABLE
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
        self.selectgroup.append(table)
        for i in self.selectgroup:
            i.hide()






        self.show()
        self.exit.clicked.connect(self.sysexit)
        self.startBtn.clicked.connect(self.startfunk)
        self.test_instant.clicked.connect(self.testinstant)
        self.cmdlist[0].clicked.connect(self.selectbtn)
        self.startobjects = [self.plsql, self.startBtn, self.exit]
        self.test_instant_objects = [self.test_instant, self.dir, self.ins]
        self.connect_status = False
        self.dbcon.clicked.connect(self.dbconfunc)

    def connect(self, dir):
        try:
            if sys.platform.startswith("darwin"):
                # lib_dir = r"D:\instantclient_21_6"
                lib_dir = dir
                cx_Oracle.init_oracle_client(lib_dir=lib_dir)
                print(1)
                self.connect_status = True
            elif sys.platform.startswith("win32"):
                lib_dir = dir
                cx_Oracle.init_oracle_client(lib_dir=lib_dir)
                self.connect_status = True
        except Exception as err:
            print(err)
            sys.exit(1)

    def sysexit(self):
        sys.exit()

    def startfunk(self):
        for i in self.startobjects:
            i.hide()
        for i in self.test_instant_objects:
            i.show()

    def testinstant(self):
        a = "\i"[0]
        newdir = self.dir.text().replace('/', a)
        print(newdir)
        self.connect(newdir)
        print(self.connect_status)
        if self.connect_status:
            self.config.set("settings", "dir", newdir)
            self.config.set("settings", "instantg", "y")
            file = open("update.ini", mode="w")
            self.config.write(file)
            print('вы молодец!!!')
            for i in self.test_instant_objects:
                i.hide()
            for i in self.con_date:
                i.show()
            self.no.hide()
            b = [self.config.get('settings', 'lastuser'), self.config.get('settings', 'lasthost'),
                 self.config.get('settings', 'lastport'),
                 self.config.get('settings', 'lastsid')]
            print(b)
            self.texts[0].setText(b[0])
            self.texts[2].setText(b[1])
            self.texts[3].setText(b[2])
            self.texts[4].setText(b[3])

    def dbconfunc(self):
        self.config.set("settings", "lastuser", self.texts[0].text())
        self.config.set("settings", "lasthost", self.texts[2].text())
        self.config.set("settings", "lastport", self.texts[3].text())
        self.config.set("settings", "lastsid", self.texts[4].text())
        file = open("update.ini", mode="w")
        self.config.write(file)
        try:
            self.db = cx_Oracle.connect(self.texts[0].text(), self.texts[1].text(),
                                   f'{self.texts[2].text()}:{self.texts[3].text()}/{self.texts[4].text()}')
            self.cursor = self.db.cursor()
            for i in self.con_date:
                i.hide()
            for i in self.cmdlist:
                i.show()
            self.congrats.setText(f"""вы успешно подключились
            к базе {self.texts[4].text()}""")
        except Exception as e:
            self.no.show()
            self.no.setText("неверные данные")

    def selectbtn(self):
        for i in self.cmdlist:
            i.hide()
        self.congrats.setText("")
        for i in self.selectgroup:
            i.show()

    def SELECT(self, table, columns, where="", order=""):
        try:
            cmd = f"SELECT {columns} FROM {table}"
            if where:
                cmd += f" WHERE {where}"
            if order:
                cmd += f" ORDER by {order}"
            print(cmd)
            self.cursor.execute(cmd)
            a = self.cursor.fetchall()
            return a
        except Exception as e:
            return e

    def SELECTBUTTON(self):
        print(self.SELECT(self.selecttexts[0].text(), self.selecttexts[1].text(), self.selecttexts[2].text(), self.selecttexts[3].text()))
        table = self.selectgroup[-1]
        table.setColumnCount(4)  # Set three columns
        table.setRowCount(4)
        table.setHorizontalHeaderLabels(["Header 1", "Header 2", "Header 3", "очко"])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())



def update(column, value, where):
    cursor.execute(f"""UPDATE ES
SET {str(column)} = {str(value)}
WHERE {str(where)}""")
    db.commit()


def insert(table, number, name, value):
    cursor.execute(f"""insert into {table} values ({str(number)},'{name}',{str(value)})""")
    db.commit()


def delete(table, where):
    cursor.execute(f"""DELETE FROM {table}
    WHERE {where}""")
    db.commit()


# update('salary', '500', 'salary < 10000')
# insert("ES", 10, "churka", '10999')
# delete("ES", "salary = 10999")

cursor.close()
db.close()
