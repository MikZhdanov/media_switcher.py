import os
from PIL import Image

path = r"C:\Users\7up\Desktop\vertical_01112021\720_1280"
filelist = os.listdir(path)
#os.mkdir(r"C:\\Users\\7up\\Desktop\\droid")
left = 40
top = 400
right = 680
bottom = 880

for num, file in enumerate(filelist):
    if num>4000:
        try:
            name = os.path.join(path, file)
            im = Image.open(name)
            im_crop = im.crop((left, top, right, bottom))
            im_crop.save("C:\\Users\\7up\\Desktop\\droid\\{}.png".format(num))
        except:pass
