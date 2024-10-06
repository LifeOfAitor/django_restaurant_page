import qrcode

# create a qr code of the main page (change when project is finished)
image = qrcode.make("https://127.0.0.1:8000")
image.save("qr.png")