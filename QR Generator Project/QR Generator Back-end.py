import qrcode


data = input("Enter your data: ")

fill = input("Enter the QR color (dark color): ")

background = input("Enter the background color (light color): ")

filename = input("Enter name for saving this file: ")

qr = qrcode.QRCode(version = 1,
				    box_size = 10,
				    border = 5)

qr.add_data(data)

qr.make(fit = True)
img = qr.make_image(fill_color = fill,
					back_color = background)

img.save(filename +'.png')
print("\nYour QR",filename+".png","has been saved.\n\n\n")
