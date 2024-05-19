import pyqrcode
from pyqrcode import QRCode
x="https://youtu.be/dQw4w9WgXcQ?si=fewafkemQjLTLjmv"
url=pyqrcode.create(x)
url.svg("A good song.svg", scale=8)
