#original
#import qrcode
#url = input("Enter URL: ")
#qr = qrcode.make(url)
#qr.save('1.png')

import qrcode

url = input("Enter URL: ")
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
#qrcode.QRCode() creates a new instance of the QRCode class provided by the qrcode library.
#This class represents a QR code generator,
# which allows us to configure various parameters of the QR code and generate it.

#QR codes come in different versions, ranging from 1 to 40.
# Version 1 is the smallest, containing 21x21 modules (squares).
# As the version increases, the size of the QR code also increases,accommodating more data.

#QR code, making it more robust but also larger. ERROR_CORRECT_L

# This parameter determines the size of each module (square) in the QR code.
# In our case, box_size=10 means each module will be 10 pixels wide and tall.

#The border parameter specifies how many modules thick the border should be around the QR code.
# In our code, border=4 means there will be a 4-module border around the QR code
qr.add_data(url)#to add data
qr.make(fit=True)#to make qr code
#The fit=True parameter indicates that the QR code should adjust
# its size automatically to fit the content.

# Colorize the QR code
colorized = qr.make_image(fill_color="blue", back_color="pink")

# Save the colorized QR code
colorized.save("1_colorful.png")
