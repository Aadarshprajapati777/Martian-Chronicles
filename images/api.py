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
      query = self.Query.text()
      queryvalue = self.QueryValue.text()
      parameter = self.Parameter.text()
      parmvalue = self.Parametervalue.text()
      

    #   query='sol'
    #   queryvalue = 1000
    #   parameter = 'camera'
    #   parmvalue = 'fhaz'
      api_key='XYvgXmCtiXfENZ2bi1d6FRZRYoKEde4GWCJiNaEo'

      print(query)
      print(queryvalue)
      print(parameter)
      print(parmvalue)
      print(api_key)

      urls =['https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?'+str(query)+'='+str(queryvalue)+'&'+str(parameter)+'='+str(parmvalue)+'&api_key='+str(api_key)]
      for url in urls:
            response = requests.get(url)
            data = response.json()
            photos = []
            for photo in data['photos']:
                img= photo['img_src']
                
                filename = img.split('/')[-1]
                with open(filename, 'wb') as f:
                    f.write(requests.get(img).content)
                    photos.append(filename)
                print(photos)



    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mars Rover Image Downloader")
        self.resize(500, 500)
        self.Query = QLineEdit()
        self.QueryValue = QLineEdit()
        self.Parameter = QLineEdit()
        self.Parametervalue = QLineEdit()
        self.button = QtWidgets.QPushButton("Fetch Image")
        self.button.clicked.connect(self.fetchimage)
        layout = QFormLayout()
        layout.addRow("Query", self.Query)
        layout.addRow("Query Value", self.QueryValue)
        layout.addRow("Parameter", self.Parameter)
        layout.addRow("Parameter Value", self.Parametervalue)
        layout.addRow(self.button)
        self.setLayout(layout)

    def view_image(self):
        self.image = Image.open(self.filename)
        self.image.show()


    
    



if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

