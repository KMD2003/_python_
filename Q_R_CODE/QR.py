import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

myqr=qrcode.make("KMD")
myqr1 =qrcode.make("dhanush")


myqr.save("myqr.png",scale=100)
myqr1.save("myqr1.png",scale=110)



b = decode(Image.open("myqr.png"))
print(b[0].data.decode("ascii"))