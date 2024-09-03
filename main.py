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

logo = Image.open('mylogo.png') #adding my logo onto qr

# Calculate logo size and position
qr_width, qr_height = img.size
logo_size = int(qr_width / 4)
logo = logo.resize((logo_size, logo_size))
logo_position = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

# Paste logo onto QR Code
img.paste(logo, logo_position, logo)

img.save("test.png")