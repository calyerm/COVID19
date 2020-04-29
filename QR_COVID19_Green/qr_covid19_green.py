# COVID 19 QR Green
# Description : Some fun with makking you own COVID 19 QR Grren Pass 
# Date : 04/19/2020
# Author : mcalyer
# Links : https://pypi.org/project/PyQRCode/  ,  https://pypi.org/project/pypng/
# Requirements:
# 1. pyqrcode  : QR code module
# 2. pypng     : render png

# Note : Change color of cv438.png to dark green 

import pyqrcode
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

# Generate QR Code PNG file
#big_code = pyqrcode.create('0987654321', error='L', version=27, mode='binary')
big_code = pyqrcode.create('0987654321', error='L', version=10)
big_code.png('tg.png', scale=6, module_color=[0, 0, 0, 0xFF], background=[0x00, 0xff, 0x00],quiet_zone = 8)

# Get image
base = Image.open('tg.png').convert('RGBA')

# Get image
cv = Image.open('cv438.png').convert('RGBA')
cv_copy = cv.copy()
cv_copy.putalpha(64)

# Make blank image for the text , initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))

# Get a Font
fnt = ImageFont.truetype('FreeMono.ttf', 18)

# Get drawing contectDrawDraw text , half opacity
d = ImageDraw.Draw(txt)

#Draw text , full opacity 
d.text((6,8), "CA SCC 95124 COVID 19 Green 04/19/2020", font=fnt, fill=(0,0,0,255))

# Composite images
out = Image.alpha_composite(base, txt)
out = Image.alpha_composite(out, cv_copy)

# Save as png file
out.save('sss.png')

