import cx_Oracle, sys, configparser, time
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QRadioButton, QButtonGroup, QLabel, \
    QMainWindow
from PyQt5.QtGui import QIcon


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
        for i in range(5):
            self.cmd = QPushButton(self)
            self.cmd.setGeometry(QtCore.QRect(100, 100 + x, 300, 60))
            self.cmd.setText(z[i])
            self.cmd.setFont(font1)
            x += 70
        self.congrats = self
        self.show()
        self.exit.clicked.connect(self.sysexit)
        self.startBtn.clicked.connect(self.startfunk)
        self.test_instant.clicked.connect(self.testinstant)
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
            db = cx_Oracle.connect(self.texts[0].text(), self.texts[1].text(),
                                   f'{self.texts[2].text()}:{self.texts[3].text()}/{self.texts[4].text()}')
            cursor = db.cursor()
            for i in self.con_date:
                i.hide()
            cursor.execute("SELECT * FROM ES")
            a = cursor.fetchall()
            for i in a:
                print(i)
        except Exception as e:
            self.no.show()
            self.no.setText("неверные данные")


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
