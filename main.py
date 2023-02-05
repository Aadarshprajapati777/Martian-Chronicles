
from io import BytesIO, StringIO
import pickle
import sys
import random
import requests
from PySide6 import QtCore, QtWidgets, QtGui
from PIL import Image
import PySide6.QtWidgets

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.photos = []
        response = requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2015-6-3&api_key=XYvgXmCtiXfENZ2bi1d6FRZRYoKEde4GWCJiNaEo')
        data = response.json()
        
        for photo in data['photos']:
            img= photo['img_src']
            self.photos.append(img)
     

        
        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("fetch image")
        self.text = QtWidgets.QLabel("Hello World",alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.photos))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())                  
