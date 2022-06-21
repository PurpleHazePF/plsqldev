import cx_Oracle, sys, configparser, pprint
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
        for i in range(4):
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

        ########
        #SELECT#
        ########
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
        #TABLE
        table = QTableWidget(self)  # Create a table

        table.resize(700, 400)
        table.move(0, 200)

        # Set the tooltips to headings
        # Set the alignment to the headers

        # Fill the first line

        # Do the resize of the columns by content
        table.resizeColumnsToContents()
        self.selectgroup.append(table)
        self.search.clicked.connect(self.SELECTBUTTON)
        for i in self.selectgroup:
            i.hide()

        ########
        #UPDATE#
        ########
        updateguide = ['таблица', 'колонка', "условия", "значение"]
        self.updategroup = []
        self.updatetexts = []
        x = 0
        for i in range(4):
            dir = QLineEdit(self)
            text = QLabel(self)
            dir.move(0 + x, 70)
            dir.resize(170, 30)
            text.setText(updateguide[i])
            text.move(0 + x, 55)
            self.updatetexts.append(dir)
            self.updategroup.append(dir)
            self.updategroup.append(text)
            x += 175
        self.UPDATE = QPushButton(self)
        self.UPDATE.setGeometry(QtCore.QRect(450, 100, 200, 60))
        self.UPDATE.setText("ОБНОВИТЬ")
        self.UPDATE.setFont(font1)
        self.updategroup.append(self.UPDATE)
        self.UPDATE.clicked.connect(self.UPDATEBUTTON)
        for i in self.updategroup:
            i.hide()



        ########
        #INSERT#
        ########
        insertguide = ['таблица', 'значения']
        self.insertgroup = []
        self.inserttexts = []
        x = 0
        for i in range(2):
            dir = QLineEdit(self)
            text = QLabel(self)
            dir.move(0 + x, 70)
            dir.resize(170, 30)
            text.setText(insertguide[i])
            text.move(0 + x, 55)
            self.inserttexts.append(dir)
            self.insertgroup.append(dir)
            self.insertgroup.append(text)
            x += 175
        self.insertb = QPushButton(self)
        self.insertb.setGeometry(QtCore.QRect(450, 100, 200, 60))
        self.insertb.setText("ВСТАВИТЬ")
        self.insertb.setFont(font1)
        self.insertgroup.append(self.insertb)
        self.insertb.clicked.connect(self.INSERTBUTTON)
        for i in self.insertgroup:
            i.hide()

        ########
        #DELETE#
        ########
        deleteguide = ['таблица', 'условие']
        self.deletegroup = []
        self.deletetexts = []
        x = 0
        for i in range(2):
            dir = QLineEdit(self)
            text = QLabel(self)
            dir.move(0 + x, 70)
            dir.resize(170, 30)
            text.setText(deleteguide[i])
            text.move(0 + x, 55)
            self.deletetexts.append(dir)
            self.deletegroup.append(dir)
            self.deletegroup.append(text)
            x += 175
        self.deleteb = QPushButton(self)
        self.deleteb.setGeometry(QtCore.QRect(450, 100, 200, 60))
        self.deleteb.setText("УДАЛИТЬ")
        self.deleteb.setFont(font1)
        self.deletegroup.append(self.deleteb)
        self.deleteb.clicked.connect(self.DELETEBUTTON)
        for i in self.deletegroup:
            i.hide()

        self.otkat = QPushButton(self)
        self.otkat.setGeometry(QtCore.QRect(10, 10, 40, 40))
        self.otkat.setText("←")
        self.otkat.setFont(font2)
        self.otkat.hide()
        self.otkat.clicked.connect(self.otkat1)
        self.show()
        self.exit.clicked.connect(self.sysexit)
        self.startBtn.clicked.connect(self.startfunk)
        self.test_instant.clicked.connect(self.testinstant)
        self.cmdlist[0].clicked.connect(self.selectbtn)
        self.cmdlist[1].clicked.connect(self.updatebtn)
        self.cmdlist[2].clicked.connect(self.insertbtn)
        self.cmdlist[3].clicked.connect(self.deletebtn)
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

    def otkat1(self):
        a = [self.selectgroup, self.updategroup, self.insertgroup, self.deletegroup]
        for i in a:
            for j in i:
                j.hide()
        for i in self.cmdlist:
            i.show()
        self.congrats.setText("")
        self.otkat.hide()

    def startfunk(self):
        for i in self.startobjects:
            i.hide()
        for i in self.test_instant_objects:
            i.show()

    def testinstant(self):
        a = "\i"[0]
        newdir = self.dir.text().replace('/', a)
        self.connect(newdir)
        if self.connect_status:
            self.config.set("settings", "dir", newdir)
            self.config.set("settings", "instantg", "y")
            file = open("update.ini", mode="w")
            self.config.write(file)
            for i in self.test_instant_objects:
                i.hide()
            for i in self.con_date:
                i.show()
            self.no.hide()
            b = [self.config.get('settings', 'lastuser'), self.config.get('settings', 'lasthost'),
                 self.config.get('settings', 'lastport'),
                 self.config.get('settings', 'lastsid')]
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
        self.otkat.show()

    def SELECT(self, table, columns, where="", order=""):
        try:
            cmd = f"SELECT {columns} FROM {table}"
            if where:
                cmd += f" WHERE {where}"
            if order:
                cmd += f" ORDER by {order}"
            self.cursor.execute(cmd)
            a = self.cursor.fetchall()
            return a
        except Exception as e:
            return e

    def SELECTBUTTON(self):
        values = self.SELECT(self.selecttexts[0].text(), self.selecttexts[1].text(), self.selecttexts[2].text(), self.selecttexts[3].text())
        table = self.selectgroup[-1]
        column_names = self.cursor.execute(f"""SELECT column_name
FROM USER_TAB_COLUMNS
WHERE table_name = '{self.selecttexts[0].text().upper()}'""")
        a = []
        for i in column_names.fetchall():
            a.append(i[0])
        table.setColumnCount(len(values[0]))  # Set three columns
        table.setRowCount(len(values))
        table.setHorizontalHeaderLabels(a)
        ii = len(values)
        jj = len(values[0])
        table.setItem(0, 0, QTableWidgetItem('1'))
        table.setItem(0, 2, QTableWidgetItem('2'))
        print(values)
        print(table)
        print(column_names)
        for i in range(ii):
            for j in range(jj):
                table.setItem(i, j, QTableWidgetItem(str(values[i][j])))
                # QTableWidgetItem(values[i][j])"""

    def updatebtn(self):
        for i in self.cmdlist:
            i.hide()
        self.congrats.setText("")
        for i in self.updategroup:
            i.show()
        self.otkat.show()

    def UPDATE1(self, table, column, where, value):
        self.cursor.execute(f"""UPDATE {table}
SET {str(column)} = {str(value)}
WHERE {str(where)}""")
        self.db.commit()


    def UPDATEBUTTON(self):
        try:
            self.UPDATE1(self.updatetexts[0].text(), self.updatetexts[1].text(), self.updatetexts[2].text(), self.updatetexts[3].text())
            self.congrats.setText(f"вы успешно обновили таблицу {self.updatetexts[0].text()}")
        except Exception:
            self.congrats.setText(f"ошибка обновления")

    def insertbtn(self):
        for i in self.cmdlist:
            i.hide()
        self.congrats.setText("")
        for i in self.insertgroup:
            i.show()
        self.otkat.show()

    def insert(self, table, values):
        self.cursor.execute(f"""insert into {table} values ({values})""")
        self.db.commit()

    def INSERTBUTTON(self):
        try:
            self.insert(self.inserttexts[0].text(), self.inserttexts[1].text())
            self.congrats.setText(f"вы успешно добавили значение")
        except Exception:
            self.congrats.setText(f"ошибка добавления")

    def deletebtn(self):
        for i in self.cmdlist:
            i.hide()
        self.congrats.setText("")
        for i in self.deletegroup:
            i.show()
        self.otkat.show()

    def delete1(self, table, where):
        self.cursor.execute(f"""DELETE FROM {table}
            WHERE {where}""")
        self.db.commit()

    def DELETEBUTTON(self):
        try:
            self.delete1(self.deletetexts[0].text(), self.deletetexts[1].text())
            self.congrats.setText(f"вы успешно удалили значение")
        except Exception as e:
            self.congrats.setText(f"ошибка удаления")

    def defolt(self):
        print('test')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())










# update('salary', '500', 'salary < 10000')
# insert("ES", 10, "churka", '10999')
# delete("ES", "salary = 10999")
