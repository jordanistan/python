import qrcode

img = qrcode.make("https://iamjordanrobison.com")

img.save("qr.png", "PNG")

os.system("open qr.png")
