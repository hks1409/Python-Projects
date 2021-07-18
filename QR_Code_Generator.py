import pyqrcode 
from pyqrcode import QRCode 
  
s = "https://github.com/"

url = pyqrcode.create(s) 
  
url.svg("github.svg", scale = 8) 