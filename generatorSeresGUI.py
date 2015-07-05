# -*- coding: utf-8 -*-


"""
Generator Arturitos in VRML
@author: Francisco Javier Clavero Álvarez
@date: 30.03.2015
"""

import sys, functions, os
from PySide import QtGui, QtCore
from random import randint

class CreateMonster(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        super(CreateMonster, self).__init__(parent)

        self.initUI()
        
    def initUI(self): 


        self.setWindowTitle(u'Informática Gráfica: Generador de Seres.')    

        self.setMaximumSize(500,620)
        self.setMinimumSize(500,620)

        ######################################################################
        
        center = QtGui.QWidget()
        self.setCentralWidget(center)

        ################### Barra ##########################################

        self.bar = QtGui.QProgressBar(self)
        self.bar.setGeometry(3, 4, 2, 2)
        self.timer = QtCore.QBasicTimer()
        self.step = 0        


        ################### Parámetros ##########################################

        self.labelStretch = QtGui.QLabel(u'')

        self.labelTam = QtGui.QLabel(u'Size:')
        self.comboboxTam = QtGui.QComboBox()
        listTam = ['small','medium','big']
        self.comboboxTam.addItems(listTam)
        self.comboboxTam.currentIndexChanged[int].connect(self.imageTam)

        self.labelBody = QtGui.QLabel(u'Faction:')
        self.comboboxBody = QtGui.QComboBox()
        listBody = ['Arturitos','Cethispios']
        self.comboboxBody.addItems(listBody)    
        self.comboboxBody.currentIndexChanged[int].connect(self.imageBody)
    

        self.labelLeg = QtGui.QLabel(u'Leg length:')
        self.comboboxLeg = QtGui.QComboBox()
        listLeg = ['short','medium','large']
        self.comboboxLeg.addItems(listLeg)
        self.comboboxLeg.currentIndexChanged[int].connect(self.imageLeg)


        self.labelGround = QtGui.QLabel(u'Ground Type:')
        self.comboboxGround = QtGui.QComboBox()
        listGround = ['soft','medium','hard']
        self.comboboxGround.addItems(listGround)  
        self.comboboxGround.currentIndexChanged[int].connect(self.imageGround)


        self.labelPos = QtGui.QLabel(u'Mode:')
        self.comboboxPos = QtGui.QComboBox()
        listPos = ['normal','defense0','defense1','defense2','attack0','attack1','attack2'] #6
        self.comboboxPos.addItems(listPos)        
        self.comboboxPos.currentIndexChanged[int].connect(self.imageMode)


        self.labelTail = QtGui.QLabel(u'Tail:')
        self.comboboxTail = QtGui.QComboBox()
        listTail = ['1','3']
        self.comboboxTail.addItems(listTail) 
        self.comboboxTail.currentIndexChanged[int].connect(self.imageTail)


        self.button = QtGui.QPushButton('Create')
        self.buttonRandom = QtGui.QPushButton('Random Create')


        self.pix = QtGui.QLabel(self)
        self.pix.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/medium.png')))
        self.pix.setGeometry(160, 40, 80, 30)

        self.pix1 = QtGui.QLabel(self)
        self.pix1.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/bodyround.png')))
        self.pix1.setGeometry(160, 40, 80, 30)   

        self.pix2 = QtGui.QLabel(self)
        self.pix2.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/legshort.png')))
        self.pix2.setGeometry(160, 40, 80, 30)   

        self.pix3 = QtGui.QLabel(self)
        self.pix3.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/soft.png')))
        self.pix3.setGeometry(160, 40, 80, 30)   

        self.pix4 = QtGui.QLabel(self)
        self.pix4.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/normal.png')))
        self.pix4.setGeometry(160, 40, 80, 30)   

        self.pix5 = QtGui.QLabel(self)
        self.pix5.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/1.png')))
        self.pix5.setGeometry(160, 40, 80, 30)           

        self.faction = 0                


        grid = QtGui.QGridLayout()

        labelBox = QtGui.QVBoxLayout()
        comboBox = QtGui.QVBoxLayout()
        imageBox = QtGui.QVBoxLayout()


        #grid.setColumnStretch(1,0)


        labelBox.addWidget(self.labelBody)
        comboBox.addWidget(self.comboboxBody)  
        imageBox.addWidget(self.pix1)

        labelBox.addWidget(self.labelPos)
        comboBox.addWidget(self.comboboxPos)  
        imageBox.addWidget(self.pix4)        
        
        labelBox.addWidget(self.labelTam)
        comboBox.addWidget(self.comboboxTam)
        imageBox.addWidget(self.pix)




        labelBox.addWidget(self.labelLeg)
        comboBox.addWidget(self.comboboxLeg) 
        imageBox.addWidget(self.pix2)

        labelBox.addWidget(self.labelGround)
        comboBox.addWidget(self.comboboxGround)
        imageBox.addWidget(self.pix3)



        labelBox.addWidget(self.labelTail)
        comboBox.addWidget(self.comboboxTail)   
        imageBox.addWidget(self.pix5)


        #grid.addWidget(self.labelStretch,0,1,0,8)
        grid.addWidget(self.button,9,1,1,5)
        grid.addWidget(self.buttonRandom,8,1,1,5)
        grid.addLayout(imageBox,2,5)
        grid.addLayout(labelBox,2,1,2,1,1)
        grid.addLayout(comboBox,2,2,2,3)
        grid.addWidget(self.bar,10,1,1,3)
        
        center.setLayout(grid)


        self.button.clicked.connect(self.generateMonster)
        self.buttonRandom.clicked.connect(self.randomMonster)


        exitAction = QtGui.QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(self.close)

 
        aboutAction = QtGui.QAction('About', self)
        self.connect(aboutAction, QtCore.SIGNAL("triggered()"), self.about)

        menubar = self.menuBar()
        fileAbout = menubar.addMenu('&Help')
        fileAbout.addAction(aboutAction)
        fileAbout.addAction(exitAction)        

        self.show()

    def imageBody(self, value):

        d = {"round":0, "square":1}

        if value == d["round"]:
            self.faction = value
            self.pix1.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/bodyround.png')))

            self.comboboxTam.setCurrentIndex(1)
            self.pix.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/medium.png')))

            self.comboboxPos.setCurrentIndex(0)
            self.pix4.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/normal.png')))

            self.comboboxLeg.setCurrentIndex(0)
            self.pix2.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/legshort.png')))

            self.comboboxTail.setCurrentIndex(0)
            self.pix5.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/1.png')))

            self.comboboxGround.setCurrentIndex(0)
            self.pix3.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/soft.png')))




        elif value == d["square"]:
            self.faction = value
            self.pix1.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/bodysquare.png')))

            self.comboboxTam.setCurrentIndex(1)
            self.pix.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/medium2.png')))

            self.comboboxPos.setCurrentIndex(0)
            self.pix4.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/normal2.png')))

            self.comboboxLeg.setCurrentIndex(0)
            self.pix2.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/legshort2.png')))

            self.comboboxTail.setCurrentIndex(0)
            self.pix5.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/1_2.png')))

            self.comboboxGround.setCurrentIndex(0)
            self.pix3.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/soft2.png')))


        

    def imageTam(self, value):

        d = {"small":0, "medium":1, "high":2}

        if self.faction == 0:

            if value == d["small"]:
                self.pix.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/small.png')))
            elif value == d["medium"]:
                self.pix.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/medium.png')))
            elif value == d["high"]:
                self.pix.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/high.png')))

        elif self.faction == 1:

            if value == d["small"]:
                self.pix.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/small2.png')))
            elif value == d["medium"]:
                self.pix.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/medium2.png')))
            elif value == d["high"]:
                self.pix.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/high2.png')))


    def imageLeg(self, value):

        d = {"short":0, "medium":1, "large":2}

        if self.faction == 0:

            if value == d["short"]:
                self.pix2.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/legshort.png')))
            elif value == d["medium"]:
                self.pix2.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/legmedium.png')))
            elif value == d["large"]:
                self.pix2.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/leglarge.png')))

        elif self.faction == 1:

            if value == d["short"]:
                self.pix2.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/legshort2.png')))
            elif value == d["medium"]:
                self.pix2.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/legmedium2.png')))
            elif value == d["large"]:
                self.pix2.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/leglarge2.png')))


    def imageGround(self, value):

        d = {"soft":0, "medium":1, "hard":2}

        if self.faction == 0:

            if value == d["soft"]:
                self.pix3.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/soft.png')))
            elif value == d["medium"]:
                self.pix3.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/mediumt.png')))
            elif value == d["hard"]:
                self.pix3.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/hard.png')))

        elif self.faction == 1:

            if value == d["soft"]:
                self.pix3.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/soft2.png')))
            elif value == d["medium"]:
                self.pix3.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/mediumt2.png')))
            elif value == d["hard"]:
                self.pix3.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/hard2.png')))

    def imageMode(self, value):

        d = {"normal":0, "defense0":1, "defense1":2, "defense2":3, "attack0":4, "attack1":5, "attack2":6}

        if self.faction == 0:

            if value == d["normal"]:
                self.pix4.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/normal.png')))

            elif value == d["defense0"]:
                self.pix4.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/defense0_1.png')))
            elif value == d["defense1"]:
                self.pix4.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/defense1_1.png')))
            elif value == d["defense2"]:
                self.pix4.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/defense2_1.png')))

            elif value == d["attack0"]:
                self.pix4.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/attack0_1.png')))
            elif value == d["attack1"]:
                self.pix4.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/attack1_1.png')))
            elif value == d["attack2"]:
                self.pix4.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/attack2_1.png')))                

        elif self.faction == 1:

            if value == d["normal"]:
                self.pix4.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/normal2.png')))

            elif value == d["defense0"]:
                self.pix4.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/defense0_2.png')))
            elif value == d["defense1"]:
                self.pix4.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/defense1_2.png')))
            elif value == d["defense2"]:
                self.pix4.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/defense2_2.png')))

            elif value == d["attack0"]:
                self.pix4.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/attack0_2.png')))
            elif value == d["attack1"]:
                self.pix4.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/attack1_2.png')))
            elif value == d["attack2"]:
                self.pix4.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/attack2_2.png'))) 

    def imageTail(self, value):

        d = {"one":0, "three":1}

        if self.faction == 0:

            if value == d["one"]:
                self.pix5.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/1.png')))
            elif value == d["three"]:
                self.pix5.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/3.png')))

        elif self.faction == 1:

            if value == d["one"]:
                self.pix5.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/1_2.png')))
            elif value == d["three"]:
                self.pix5.setPixmap(QtGui.QPixmap(os.path.join(os.getcwd(),'images/3_2.png')))

    def randomMonster(self):

        self.comboboxTam.setCurrentIndex(randint(0, 2))
        #self.comboboxBody.setCurrentIndex(randint(0, 1))
        self.comboboxLeg.setCurrentIndex(randint(0, 2))
        self.comboboxGround.setCurrentIndex(randint(0, 2))
        self.comboboxPos.setCurrentIndex(randint(0, 6))
        self.comboboxTail.setCurrentIndex(randint(0, 1))


    def generateMonster(self):


        self.timer.start(100, self)
        self.button.setText('creating...')

        #Crea una carpeta separada para cada monstruo.

        i = 1
        c = 1

        if self.faction == 0:
            ruta = os.path.join(os.getcwd(), "Arturito_" + str(i))
            rutaCopy = os.path.join(os.getcwd(), "Base/")

            self.step = 20
            self.bar.setValue(self.step)
            while os.path.exists(ruta): 
                ruta = os.path.join(os.getcwd(), "Arturito_" + str(i))
                i = int(i) + 1

        elif self.faction == 1:
            ruta = os.path.join(os.getcwd(), "Cethispio_" + str(c))
            rutaCopy = os.path.join(os.getcwd(), "Base/")

            self.step = 20
            self.bar.setValue(self.step)
            while os.path.exists(ruta): 
                ruta = os.path.join(os.getcwd(), "Cethispio_" + str(c))
                c = int(c) + 1            
        
        os.makedirs(ruta)

       
        functions.scaleMonster(self.comboboxTam.currentIndex(), self.comboboxBody.currentIndex(), self.comboboxPos.currentIndex(), ruta, rutaCopy)
        functions.legLength(self.comboboxTam.currentIndex(), self.comboboxBody.currentIndex(), self.comboboxLeg.currentIndex(), self.comboboxGround.currentIndex(), self.comboboxPos.currentIndex(), ruta, rutaCopy)
        functions.posMonster(self.comboboxBody.currentIndex(), self.comboboxPos.currentIndex(), ruta, rutaCopy)
        functions.generateFiles(rutaCopy, ruta)
        functions.ornamentMonster(self.comboboxBody.currentIndex(), ruta, rutaCopy)
        functions.nTail(self.comboboxBody.currentIndex(), self.comboboxTail.currentIndex(), self.comboboxPos.currentIndex(), ruta, rutaCopy)
        functions.word(self.comboboxBody.currentIndex(), self.comboboxPos.currentIndex(), ruta, rutaCopy)


        self.step = 100
        self.bar.setValue(self.step)

        if self.faction == 0:
                QtGui.QMessageBox.information(self, "Mensaje","Arturito created in " + ruta)
        elif self.faction == 1:
                QtGui.QMessageBox.information(self, "Mensaje","Cethispio created in " + ruta)

        self.bar.reset()
        self.button.setText('Generate')

    def about(self):
        QtGui.QMessageBox.about(self, "About", u"Francisco Javier Clavero Álvarez\n\nGenerador Arturitos v2.0")

        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = CreateMonster()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
