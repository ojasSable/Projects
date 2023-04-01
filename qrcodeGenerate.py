import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

# generate qr code
data = "Hi, hello world"
img = qrcode.make(data)
print(img)

img.save('qrcode.png')

# decode the generated qr code
img = Image.open('qrcode.png')
decoded_info = decode(img)

print(decoded_info)