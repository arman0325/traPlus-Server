from simple_image_download import simple_image_download as simp
from PIL import Image

def downloadImage(result_str):
    response = simp.simple_image_download
    response().download(result_str, 1)
    print(response().urls(result_str, 1))
    changeImg(result_str)
    
def changeImg(filename):
    path = "simple_images/"+filename+"/"
    try:
        str1 = path + filename + "_1.jpeg"
        im1 = Image.open(str1)
        newStr = path + "new_" + filename + ".jpg"
        im1.save(newStr)
    except OSError as e:
        str1 = path + filename + "_1.png"
        im1 = Image.open(str1)
        newStr = path + "new_" + filename + ".jpg"
        im1.save(newStr)
    print("OK")
    
if __name__ == '__main__':
    
    downloadImage("banana")