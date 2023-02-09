from io import BytesIO
import os
import pickle
import sys
import requests
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PIL import Image
import PySide6.QtWidgets
from PySide6.QtWidgets import (
    QGroupBox,
    QLabel,
    QLineEdit,
    QPlainTextEdit,
    QRadioButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
    QApplication,
    QFormLayout,
    QDialog,
    QDialogButtonBox,
    QComboBox,
    QCheckBox,
    QButtonGroup,
    QMessageBox,
    Qicon,
    QSystemTrayIcon,
)
from PySide6.QtGui import QPixmap
import ezgmail


count=0
photos = []
imagedata = []
countingphoto=0
class Window(QDialog):

    def fetchimage(self):
      global imagedata
      global countingphoto
      global photos
      self.imageDownloading()

      icon=Qicon("icon.png")
      tray=QSystemTrayIcon(icon)
      tray.show()
      

    

      query = self.Query.currentText()
      queryvalue = self.QueryValue.currentText()
      parmvalue = self.Parametervalue.text()
      api_key = 'XYvgXmCtiXfENZ2bi1d6FRZRYoKEde4GWCJiNaEo'
      parameter = 'camera'
      rover = self.Rover.currentText()
      page=1
      photono = self.photono.text()
      photocount=int(photono)


    #   query='sol'
    #   queryvalue = 1000 
    #   parmvalue = 'fhaz'QComboBox

      print(query)
      print(queryvalue)
      print(parameter)
      print(parmvalue)
      print(photono, "photo no")
      print(rover)
      print(photocount,"integer photo no")
    

      urls =['https://api.nasa.gov/mars-photos/api/v1/rovers/'+(rover)+'/photos?'+str(query)+'='+str(parmvalue)+'&'+str(parameter)+'='+str(queryvalue)+'&page='+str(page)+'&api_key='+str(api_key)]
      
      
      for url in urls:
            response = requests.get(url)
            data = response.json()
            photos = []
        
            for indx, photo in enumerate(data['photos']):
                with open (str(indx)+'.png', 'wb') as f:
                    f.write(requests.get(photo['img_src']).content) 
                    photos.append(indx)   
                    print("image downloaded: "+str(indx)+".png")
                    countingphoto=countingphoto+1
                    msg=QMessageBox()
                    msg.setWindowTitle("Downloading")
                    msg.setText("Downloading Image "+str(countingphoto))
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.NoButton)
                    x=msg.show()
                    if countingphoto==photocount:
                        break
                    else:
                        pass
                        
      print(photos)

      if len(photos) == 0:
            print("No photos found")
            self.showmsg()
            return
      
      else:
        self.viewimage()




    def __init__(self):
        super().__init__()
        layout = QFormLayout()
        self.setWindowTitle("Mars Rover Image Downloader")
        self.resize(765,577)
        self.Query = QComboBox()
        self.QueryValue = QComboBox()
        self.Parameter = QLineEdit()
        self.photono = QLineEdit()
        self.Rover = QComboBox()
        self.Rover.addItem("curiosity")
        self.Rover.addItem("opportunity")
        self.Rover.addItem("spirit")
    

        self.Parametervalue = QLineEdit()
        self.button = QtWidgets.QPushButton("Fetch Image")
        self.button.clicked.connect(self.deletePrevData)
        layout = QFormLayout()

        # layout.addRow("Parameter", self.Parameter)
        # layout.addRow("Parameter Value", self.Parametervalue)

        layout.addRow("Select Parameter", self.Query)
        layout.addRow("Parameter Value", self.Parametervalue)
        layout.addRow("Select Rover", self.Rover)
        self.Query.addItem("sol")
        self.Query.addItem("earth_date")
        layout.addRow("Photo", self.photono)
        layout.addRow("Select Camera", self.QueryValue)
        self.QueryValue.addItem("fhaz")
        self.QueryValue.addItem("rhaz")
        self.QueryValue.addItem("mast")
        self.QueryValue.addItem("chemcam")
        self.QueryValue.addItem("mahli")
        self.QueryValue.addItem("mardi")
        self.QueryValue.addItem("navcam")
        self.QueryValue.addItem("pancam")
        self.QueryValue.addItem("minites")
     

        layout.addRow(self.button)
        self.setLayout(layout)

        self.image = QtWidgets.QLabel(self)



    def imageDownloading(self):
        msg = QMessageBox()
        msg.setWindowTitle("Downloading photos")
        msg.setText("Downloading photos please wait")
        msg.setIcon(QMessageBox.Information)

        x = msg.exec_()




    def showmsg(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("No Photos Found")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.NoButton)
        x = msg.exec_()


    def deletePrevData(self):
        global count
        count=0
        for i in range(0,100):
            try:
                os.remove(str(i)+'.png')
            except:
                pass

        self.fetchimage()
     

    
    def viewimage(self):
        global count
    
        self.image.setPixmap(QtGui.QPixmap("/home/adarsh/amfoss_backup/amfoss-tasks/martian-rover/"+str(count)+".png"))
        self.image.setGeometry(30,210,491,341)
        self.image.show()


        self.button=QtWidgets.QPushButton("Next Image",self)
        self.button.setGeometry(600,300,89,25)
        self.button.clicked.connect(self.nextimage)
        self.button.show()
        self.button=QtWidgets.QPushButton("Prev Image",self)
        self.button.setGeometry(600,340,89,25)
        self.button.clicked.connect(self.previmage)
        self.button.show()
        print("image shown")

        self.receiver=QtWidgets.QLineEdit(self)
        self.receiver.setGeometry(600,200,89,25)
        self.receiver.show()

        
        self.button=QtWidgets.QPushButton("Send Mail",self)
        self.button.setGeometry(600,380,89,25)
        self.button.clicked.connect(self.sendmail)
        self.button.show()
        





    
      
    def nextimage(self):
        global count
        global photos

        if count < len(photos):
                count +=1
                self.viewimage()
                print("next image count is", count)


    def previmage(self):
        global count
        if count >= 0:
            count -=1
            self.viewimage()
            print("prev image count is "    , count)    

    
    # def mailtemplate(self):
    #     self.layout=QVBoxLayout(self)
    #     self.layout.addWidget(QLabel("Receiver"))
    #     self.receiver=QLineEdit()
    #     self.layout.addWidget(QLabel("Subject"))
    #     self.subject=QLineEdit()
    #     self.layout.addWidget(QLabel("Body"))
    #     self.body=QLineEdit()
        


        

        

        

        # global photos
        # msg = QMessageBox()
        # msg.setWindowTitle("Sending Mail")
        # msg.setText("Sending mail please wait")
        # msg.setIcon(QMessageBox.Information)
        # x = msg.exec_()
        # print("sending mail")
        # ezgmail.send('
    def sendmail(self):
        global count
        global photos
        msg = QMessageBox()
        msg.setWindowTitle("Sending Mail")
        msg.setText("Sending mail please wait")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()
        print("sending mail")
        ezgmail.send(self.receiver.text(), 'Mars Rover Image', 'This is the image of mars rover', [str(count)+'.png'])
        self.mailsent()


    def mailsent(self):
        msg = QMessageBox()
        msg.setWindowTitle("Mail Sent")
        msg.setText("Mail Sent Sucessfully")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())