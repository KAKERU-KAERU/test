import qrcode

qr=qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=5,
    border=8
)

qr.add_data('https://letus.ed.tus.ac.jp/')#URL
qr.make()
im=qr.make_image(fill_color='black',back_color='white')#set color
im.show()
