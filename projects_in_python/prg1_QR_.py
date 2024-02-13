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

qr.add_data("https://web.whatsapp.com/")
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="black",)  # Fix typo in black_color
img.save('qr_code2.png')
