from io import BytesIO
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
)





class Window(QDialog):
    def fetchimage(self):
      query = self.Query.currentText()
      queryvalue = self.QueryValue.currentText()
      parmvalue = self.Parametervalue.text()
      api_key = 'XYvgXmCtiXfENZ2bi1d6FRZRYoKEde4GWCJiNaEo'
      parameter = 'camera'

      

    #   query='sol'
    #   queryvalue = 1000 
    #   parmvalue = 'fhaz'QComboBox
      print(query)
      print(queryvalue)
      print(parameter)
      print(parmvalue)

      urls =['https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?'+str(query)+'='+str(parmvalue)+'&'+str(parameter)+'='+str(queryvalue)+'&api_key='+str(api_key)]
      for url in urls:
            response = requests.get(url)
            data = response.json()
            photos = []
            for indx, photo in enumerate(data['photos']):
                with open (str(indx)+'.png', 'wb') as f:
                    f.write(requests.get(photo['img_src']).content)      
            self.viewimage()                    

      print(photos)


      self.viewimage()            

    def __init__(self):
        super().__init__()
        layout = QFormLayout()
        self.setWindowTitle("Mars Rover Image Downloader")
        self.resize(500, 500)
        self.Query = QComboBox()
        self.QueryValue = QComboBox()
        self.Parameter = QLineEdit()
        self.Parametervalue = QLineEdit()
        self.button = QtWidgets.QPushButton("Fetch Image")
        self.button.clicked.connect(self.fetchimage)
        layout = QFormLayout()

        # layout.addRow("Parameter", self.Parameter)
        # layout.addRow("Parameter Value", self.Parametervalue)
        layout.addRow(self.Query)
        layout.addRow("Select Parameter", self.Query)
        layout.addRow("Parameter Value", self.Parametervalue)


        self.Query.addItem("sol")
        self.Query.addItem("earth_date")
        layout.addRow("Select Camera", self.QueryValue)
        self.QueryValue.addItem("fhaz")
        self.QueryValue.addItem("rhaz")

        layout.addRow(self.button)
        self.setLayout(layout)


    
    def viewimage(self):
        count=0
        self.image = QtWidgets.QLabel(self)
        self.image.setPixmap(QtGui.QPixmap("/home/adarsh/amfoss_backup/amfoss-tasks/martian-rover/"+str(count)+".png"))
        self.image.setGeometry(0, 0, 500, 500)
        self.image.show()
        self.button=QtWidgets.QPushButton("Next Image",self)
        self.button.setGeometry(500, 500, 100, 100)
        self.button.clicked.connect(self.nextimage)
        self.button.show()
        
        print("image shown")
        layout = QFormLayout()
    
      
    def nextimage(self):
        count+=1
        self.viewimage()
  


    



if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

