import qrcode
import cv2

qr_code_value = int(input("How many qr code you need: "))
if qr_code_value < 1:
    raise Exception("Sorry, no numbers below zero")
for i in range(qr_code_value):
    url_addr = input("Please enter your url: ")
    if "https://" or "http://" in url_addr:
        url = qrcode.QRCode(version=1,
                            box_size=20,
                            border=5)
        url.add_data(url_addr)
        url.make(fit=True)
        img = url.make_image(fill='blue', back_color='white')
        file_name = input("Write your file name: ")
        file_name = file_name + '.png'
        img.save(file_name)
        image = cv2.imread(file_name)
        file_name.replace(".png", "")
        cv2.imshow(file_name, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Enter Correct URL")
