# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tnl.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import time
import urllib.request
from bs4 import BeautifulSoup
import os
from PIL import Image

class ReTbmm():
    def Retbmm(self):
        start = time.time()
        self.cdir = os.getcwd()
        # 网址https://www.autohome.com.cn
        # 车身外观
        url1 ='https://car.autohome.com.cn/pic/series/2664-1.html#pvareaid=2042220'
        # 中控方向盘
        url2='https://car.autohome.com.cn/pic/series/2664-10.html#pvareaid=2042220'
        # 车厢座椅
        url3 = 'https://car.autohome.com.cn/pic/series/2664-3.html#pvareaid=2042220'
        # 其他细节
        url4 = 'https://car.autohome.com.cn/pic/series/2664-12.html#pvareaid=2042220'
        self.getImag('车身外观',url1)
        self.getImag('中控方向盘', url2)
        self.getImag('车厢座椅', url3)
        self.getImag('其他细节', url4)
        end=time.time()
        print('run time:'+str(end -start))

    def getImag(self,name,urls):
        user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
        headers={'User-Agent':user_agent}
        request= urllib.request.Request(urls,headers=headers)
        response =urllib.request.urlopen(request)
        bsObj = BeautifulSoup(response,'html.parser')
        t1 =bsObj.find_all('img')
        for t2 in t1:
            t3 =t2.get('src')
            print(t3)
        path = self.cdir +'/mrsoft/'+str(name)
        if not os.path.exists(path):
            os.makedirs(path)
        n =0
        for img in t1:
            n=n+1
            link =img.get('src')
            if link:
                s ='https:'+str(link)
                i = link[link.rfind('.'):]
                try:
                    request=urllib.request.Request(s)
                    response =urllib.request.urlopen(request)
                    imgData=response.read()
                    pathfile =path+r'/'+str(n)+i
                    with open( pathfile,'wb') as f:
                        f.write(imgData)
                        f.close()
                        print('下载完成'+n)
                except:
                    print('sorry')

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1300, 900)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(20, 70, 181, 800))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 179, 800))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.treeView = QTreeWidget(self.scrollAreaWidgetContents)
        self.treeView.setGeometry(QtCore.QRect(0, 0, 181, 761))
        self.treeView.setObjectName("treeView")
        self.treeView.setHeaderLabel('爬出的结果')
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea_2 = QtWidgets.QScrollArea(Form)
        self.scrollArea_2.setGeometry(QtCore.QRect(200, 70, 1000, 800))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 161, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "爬虫"))
        self.pushButton.setText(_translate("Form", "特斯拉"))
        self.root = QTreeWidgetItem(self.treeView)
        self.root.setText(0,'model x')
        self.pushButton.clicked.connect(self.btnstate)

    def btnstate(self):
        ui =ReTbmm()
        ui.Retbmm()
        self.path =cdir +'/mrsoft'
        dirs =os.listdir(self.path)
        for dir in dirs:
            QTreeWidgetItem(self.root).setText(0,dir)
        self.treeView.clicked.connect(self.onTreeclicked)
    def onTreeclicked(self):
        items =self.treeView.currentItem()
        if items.text(0)=='model x':
            self.root.takeChild()
            dirs = os.listdir(self.path)
            for dir in dirs:
                QTreeWidgetItem(self.root).setText(0, dir)
            self.treeView.clicked.connect(self.onTreeclicked)
        else:
            while self.gridLayout.count():
                item =self.gridLayout.takeAt(0)
                widget=item.widget()
                widget.deleteLater()
            filenames=[]
            for filename in os.listdir(cdir+'/mrsoft/'+items.text(0)):
                filenames.append(filename)
            i=-1
            for n in range(len(filenames)):
                x = n%3
                if(x ==0 ):
                    i +=1
                self.widget=QWidget()
                self.widget.setGeometry(QtCore.QRect(110,40,350,300))
                self.widget.setObjectName('widget'+str(n))
                self.label=QLabel(self.widget)
                self.label.setGeometry(QtCore.QRect(0, 0, 350, 300))
                self.label.setPixmap(QPixmap(self.path+'/'+items.text(0)+'/'+filenames[n]))
                self.label.setScaledContents(True)
                self.label.setObjectName('label'+str(n))

                self.commandLinkButton = QCommandLinkButton(self.widget)
                self.commandLinkButton.setGeometry(QtCore.QRect(0, 0, 111, 41))
                self.commandLinkButton.setText(filenames[n])
                self.commandLinkButton.setObjectName('commandLinkButton'+str(n))
                self.commandLinkButton.clicked.connect(lambda : self.wichbtn(self.path+'/'+items.text(0)+'/'))
                self.gridLayout.addWidget(self.widget,i,x)
            self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
            self.verticalLayout.addWidget(self.scrollArea_2)
            self.scrollAreaWidgetContents_2.setMaximumWidth(800)
            self.scrollAreaWidgetContents_2.setMinimumHeight(i*300)
        pass
    def wichbtn(self,tppath):
        sender = self.gridLayout.sender()
        img = Image.open(tppath +sender.text())
        img.show()
class FirstWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(249, 212)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(40, 30, 181, 151))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录"))
        self.label.setText(_translate("Form", "用户名（leenry）"))
        self.label_2.setText(_translate("Form", "密码（123456）"))
        self.pushButton.setText(_translate("Form", "登录"))
        self.pushButton_2.setText(_translate("Form", "退出"))
#       登录
        self.pushButton.clicked.connect(self.onclick)
        # 退出
        self.pushButton_2.clicked.connect(quit)

    def onclick(self):
        if self.lineEdit.text()=='leenry':
             if self.lineEdit_2.text()=='123456':
                 MainWindow1.close()
                 MainWindow.show()
             else:
                 self.lineEdit_2.setText('密码错误请重新输入')
        else:
            self.lineEdit.setText('用户名错误请重新输入')
if __name__ =='__main__':
    App =QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    cdir = os.getcwd()
    ex = FirstWindow()
    ex.setupUi(MainWindow1)
    MainWindow1.show()
    MainWindow =QtWidgets.QMainWindow()
    ui= Ui_Form()
    ui.setupUi(MainWindow)
    sys.exit(App.exec_())