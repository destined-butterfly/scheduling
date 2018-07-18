from PyQt5.QtWidgets import QApplication ,QMainWindow
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time
import random
import threading
import os
from ui import *

class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.pgbs=[]
        self.pgbsid=-1
        self.pgb_i_1=70
        self.pgb_i_2=70
        self.pgb_i_3=70
        self.lab11=30
        self.lab21=30
        self.lab31=30
        self.lab1_1=[]
        self.lab2_1=[]
        self.lab3_1=[]
        #pcb
        #self.RR_info_sl=RR_info()
        #RR
        self.timer = QTimer()
        self.RR_thread1=RR_Thread()
        self.timer.timeout.connect(self.RR_i_item)
        self.RR_thread1.start()
        #HR
        self.timer3 = QTimer()
        self.timer3.timeout.connect(self.HR_time)
        self.HR_thread2=HR_Thread()
        self.HR_thread2.start()
        #PS
        self.PS_thread3=PS_Thread()
        self.PS_thread3.start()
        #performed---RR
        #self.thread1_RR_time_R = threading.Thread(target=self.RR_time_R(),args=())
        #self.RR_time_R()
        #self.thread1_RR = threading.Thread(target=self.RR(),args=())
        #self.thread1_RR_time_R.start()
        #self.thread1_RR.start()
        #self.RR()

    def RR_i_item(self):
        rr_info.RR_i+=1
        #print(str(rr_info.RR_i))

    def HR_time(self):
        rr_info.mem_time+=1
        #print(str(rr_info.achive_time))

    def new_work_1(self):
        if rr_info.item1==1:
            #self.thread1_RR_time_R = threading.Thread(target=self.RR_time_R(),args=())
            self.timer.start(2000)
            #self.RR_thread1.start()
        self.add(self.tab,self.lab11,rr_info.item1,1,self.pgb_i_1)
        self.lab11+=70
        rr_info.item1+=1
        self.pgb_i_1+=70
        

    def new_work_2(self):
        self.add(self.tab_2,self.lab21,rr_info.item2,2,self.pgb_i_2)
        self.lab21+=70
        rr_info.item2+=1
        self.pgb_i_2+=70

    def new_work_3(self):
        if rr_info.item3==1:
            self.timer3.start(1000)
        self.add(self.tab_3,self.lab31,rr_info.item3,3,self.pgb_i_3)
        self.lab31+=70
        rr_info.item3+=1
        self.pgb_i_3+=70

    def add(self,tab_num,lab1_i,item,tab2or3,pgbnum):
        #lab1
        new_lab1 = QtWidgets.QLabel(tab_num)
        new_lab1.setGeometry(QtCore.QRect(0, lab1_i, 81, 31))
        new_lab1.setText("work"+str(item))
        new_lab1.show()
        #lab2
        new_lab2 = QtWidgets.QLabel(tab_num)
        new_lab2.setGeometry(QtCore.QRect(140, lab1_i, 131, 31))
        leng=random.randint(50,100)
        new_lab2.setText("length:"+str(leng))
        new_lab2.show()
        #lab3
        new_lab3 = QtWidgets.QLabel(tab_num)
        new_lab3.setGeometry(QtCore.QRect(280, lab1_i, 131, 31))
        new_lab3.setText("")
        new_lab3.show()
        #pgb
        new_pgb = QtWidgets.QProgressBar(tab_num)
        new_pgb.setGeometry(QtCore.QRect(0, pgbnum, 781, 23))
        new_pgb.setProperty("value", 0)
        new_pgb.show()
        #lab4
        if tab2or3 ==1:
            self.lab1_1.append(new_lab1)
            rr_info.lab1_len.append(new_lab2)
            rr_info.lab1_stata.append(new_lab3)
            rr_info.pgb1.append(new_pgb)
            new_pcb = Pcb(leng,item)
            rr_info.Pcb1.append(new_pcb)
        if tab2or3 ==2:
            #lab4 work level
            new_lab4 = QtWidgets.QLabel(tab_num)
            new_lab4.setGeometry(QtCore.QRect(470, lab1_i, 131, 31))
            new_level=random.randint(1,5)
            new_lab4.setText("work level:"+str(new_level))
            new_lab4.show()
            self.lab2_1.append(new_lab1)
            rr_info.lab2_len.append(new_lab2)
            rr_info.lab2_stata.append(new_lab3)
            rr_info.lab_level.append(new_lab4)
            rr_info.pgb2.append(new_pgb)
            new_pcb = Pcb(leng,item)
            new_pcb.level=new_level
            rr_info.Pcb2.append(new_pcb)
        if tab2or3 ==3:
            #lab4 work Ratio%
            new_lab4 = QtWidgets.QLabel(tab_num)
            new_lab4.setGeometry(QtCore.QRect(470, lab1_i, 131, 31))
            new_lab4.setText("")
            new_lab4.show()
            self.lab3_1.append(new_lab1)
            rr_info.lab3_len.append(new_lab2)
            rr_info.lab3_stata.append(new_lab3)
            rr_info.lab_bfb.append(new_lab4)
            rr_info.pgb3.append(new_pgb)
            new_pcb = Pcb(leng,item)
            rr_info.Pcb3.append(new_pcb)
            rr_info.achive_time.append(rr_info.mem_time)

class Pcb():
    def __init__(self,length,num):
        self.length=length
        self.name_num=num
        self.performed=0
        self.level=0

class RR_Thread(QThread):
    #time_rr_gx_signal =pyqtsignal()
    def __init__(self):
        super(RR_Thread,self).__init__()
    def run(self):
        if rr_info.item1>=2:
            if rr_info.RR_i >rr_info.item1-2:
                rr_info.RR_i=rr_info.RR_i % (rr_info.item1-1)
            if rr_info.RR_i not in rr_info.RR_ywc:
                #set pbg vale
                rr_info.Pcb1[rr_info.RR_i].performed+=1
                if rr_info.Pcb1[rr_info.RR_i].performed >=rr_info.Pcb1[rr_info.RR_i].length:
                    value=100
                    rr_info.RR_ywc.append(rr_info.RR_i)
                else:
                    value=rr_info.Pcb1[rr_info.RR_i].performed/rr_info.Pcb1[rr_info.RR_i].length *100
                rr_info.pgb1[rr_info.RR_i].setProperty("value", int(value))
            time.sleep(0.5)
        time.sleep(0.5)
        self.run()

class HR_Thread(QThread):
    def __init__(self):
        super(HR_Thread,self).__init__()
    def run(self):
        if rr_info.item3>=2:
            if 0 not in rr_info.HR_ywc:
                while True:
                    rr_info.Pcb3[0].performed+=1
                    if rr_info.Pcb3[0].performed >= rr_info.Pcb3[0].length:
                        value=100
                        rr_info.HR_ywc.append(0)
                    else:
                       value=rr_info.Pcb3[0].performed / rr_info.Pcb3[0].length *100
                    rr_info.pgb3[0].setProperty("value",int(value))
                    time.sleep(0.5)        
                    if int(value)>=100:
                        break
            #hr
            else :
                if rr_info.item3 >2:
                    HR_i=1
                    hest=0
                    for i in range(rr_info.item3-1):
                        if i not in rr_info.HR_ywc:
                            now_hest=1 + (rr_info.mem_time - rr_info.achive_time[i])/rr_info.Pcb3[i].length
                            if now_hest > hest:
                                HR_i=i
                                hest=now_hest
                while True:
                    rr_info.Pcb3[HR_i].performed+=1
                    if rr_info.Pcb3[HR_i].performed >= rr_info.Pcb3[HR_i].length:
                        value=100
                        rr_info.HR_ywc.append(HR_i)
                    else:
                       value=rr_info.Pcb3[HR_i].performed / rr_info.Pcb3[HR_i].length *100
                    rr_info.pgb3[HR_i].setProperty("value",int(value))
                    time.sleep(0.5)        
                    if int(value)>=100:
                        break
        time.sleep(0.5)
        self.run()

class PS_Thread(QThread):
    def __init__(self):
        super(PS_Thread,self).__init__()
    def run(self):
        if rr_info.item2 >=2:
            level=5
            PS_i=0
            for i in range(rr_info.item2-1):
                if i not in rr_info.PS_ywc:
                    if rr_info.Pcb2[i].level < level:
                        level=rr_info.Pcb2[i].level
                        PS_i=i
            if PS_i not in rr_info.PS_ywc:
                rr_info.Pcb2[PS_i].performed+=1
                if rr_info.Pcb2[PS_i].performed >= rr_info.Pcb2[PS_i].length:
                    value=100
                    rr_info.PS_ywc.append(PS_i)
                else:
                   value=rr_info.Pcb2[PS_i].performed / rr_info.Pcb2[PS_i].length *100
                rr_info.pgb2[PS_i].setProperty("value",int(value))
        time.sleep(0.5)
        self.run()

class RR_info():
    def __init__(self):
        self.RR_i=0
        self.RR_ywc=[]
        self.mem_time=0
        self.achive_time=[]
        self.HR_ywc=[]
        self.PS_ywc=[]
        self.pgb1=[]
        self.pgb2=[]
        self.pgb3=[]
        self.Pcb1=[]
        self.Pcb2=[]
        self.Pcb3=[]
        self.item1=1
        self.item2=1
        self.item3=1
        self.lab1_len=[]
        self.lab2_len=[]
        self.lab3_len=[]
        self.lab1_stata=[]
        self.lab2_stata=[]
        self.lab3_stata=[]
        self.lab_level=[]
        self.lab_bfb=[]

if __name__=="__main__":
    rr_info=RR_info()
    app=QApplication(sys.argv)
    myWin=MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
