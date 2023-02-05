from io import BytesIO
import pickle
import requests
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PIL import Image
import PySide6.QtWidgets

query='sol'
queryvalue = 10000
parameter = 'page'
parmvalue = '1'
api_key='XYvgXmCtiXfENZ2bi1d6FRZRYoKEde4GWCJiNaEo'

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
     
