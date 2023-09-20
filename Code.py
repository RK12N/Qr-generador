import qrcode
texto = "https://www.youtube.com/watch?v=h7BiXr81Guw"

qr=qrcode.QRCode(version=7,
                 box_size=10,
                 border=2)
qr.add_data(texto)
qr.make(fit=True)

imagen_qr =qr.make_image(fill_color="black",
                          black_color="white")
imagen_qr.save("Codigo_qr.png")
