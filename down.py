from simple_image_download import simple_image_download as simp
from PIL import Image

def downloadImage(result_str):
    response = simp.simple_image_download
    response().download(result_str, 1)
    linkMsg = response().urls(result_str, 1)
    print("\nThe download link:")
    for x in linkMsg:
        print(x)
    changeImg(result_str)
    
def changeImg(filename):
    path = "simple_images/"+filename+"/"
    try:
        str1 = path + filename + "_1.jpeg"
        im1 = Image.open(str1)
        width, height = im1.size
        widthTarget = 200
        if widthTarget < width:
            scale = width / widthTarget
            heightTarget = height / scale
            reImg = im1.resize((widthTarget,int(heightTarget)), Image.ANTIALIAS)
            newStr = path + filename + ".jpg"
            reImg.save(newStr)
        else:
            newStr = path + filename + ".jpg"
            im1.save(newStr)
    except OSError as e:
        str1 = path + filename + "_1.png"
        im1 = Image.open(str1)
        width, height = im1.size
        widthTarget = 200
        if widthTarget < width:
            scale = width / widthTarget
            heightTarget = height / scale
            reImg = im1.resize((widthTarget,int(heightTarget)), Image.ANTIALIAS)
            newStr = path + filename + ".jpg"
            reImg.save(newStr)
        else:
            newStr = path + filename + ".jpg"
            im1.save(newStr)
    print("Image was resized and saved")

def resizeImgFunc(filename ,path):
    
    str1 = path
    im1 = Image.open(str1)
    width, height = im1.size
    widthTarget = 200
    if widthTarget < width:
        scale = width / widthTarget
        heightTarget = height / scale
        reImg = im1.resize((widthTarget,int(heightTarget)), Image.ANTIALIAS)
        reImg.save(path)
    else:
        im1.save(path)
    print("Image was resized and saved")    
if __name__ == '__main__':
    
    downloadImage("banana")