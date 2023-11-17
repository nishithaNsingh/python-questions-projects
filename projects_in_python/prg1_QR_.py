# basic qr code(black and white)

'''import qrcode as qr 
img = qr.make("https://www.youtube.com/watch?v=gfDE2a7MKjA&t=33755s")
img.save('qr_code.png')'''

# designed qr code
import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, 
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border=4)

qr.add_data("file:///C:/Users/Dell/OneDrive/Desktop/second%20year%20notes/Untitled-1.html")
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="blue",)  # Fix typo in black_color
img.save('qr_code2.png')
