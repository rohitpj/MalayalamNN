#changes transparent background to white
import os
from PIL import Image

def whiteBackground(image):
    imageName=os.path.splitext(image)[0]
    image = Image.open(image)
    new_image = Image.new("RGBA", image.size, "WHITE") # Create a white rgba background
    new_image.paste(image, (0, 0), image)              # Paste the image on the background. Go to the links given below for details.
    newImageName=imageName+'.jpg'
    print(newImageName)
    new_image.convert('RGB').save(newImageName, "JPEG")   

whiteBackground('C:\Users\Rohit\MalayalamNN\98.png')