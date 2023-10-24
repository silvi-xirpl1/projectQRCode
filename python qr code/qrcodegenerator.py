#1.) install library qrcode = pip install qrcode
#2.) install library image = pip install image
#3.)code . untuk membuka vs lewat terminal
#4.)install python 3.12 di microsoft store yang eror di pip

import qrcode #install libary di cmd -> pip install qrcode
import qrcode #install libary di cmd -> pip install image
import image 
qr = qrcode.QRCode(
    version = 15, #untuk versi qr codenya
    box_size = 10, #untuk ukuran qr codenya
    border = 5 #ukuran putih2nya qr code
)

data = "https://youtu.be/tpe4k03Jm4I?si=asu8XHUU1tl0-2zE" #link qr code

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black", back_color="white") #setting warna qr code
img.save("link.png") # untuk build qr ke gambar png