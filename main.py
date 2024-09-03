import qrcode
from PIL import Image
qr = qrcode.QRCode(
    version = 5, #says how complicated the qr must be
    box_size = 5, #the box size of the qr
    border = 3 #border gap of the qr with the box
)

data = "https://youtu.be/Dp6lbdoprZ0?si=Yw-opH4LyltyjVu2"

qr.add_data(data)
qr.make(fit = True)

img = qr.make_image(fill_color = "red",back_color = "white").convert('RGB')

img.save("test.png")