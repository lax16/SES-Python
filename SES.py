import numpy as np
import cv2
import sys
import pyHook
import pythoncom


# Get user supplied values
imagePath = 'sample.jpg'
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
img = cv2.imread(imagePath)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
)

print("Face Found".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    break
    cv2.rectangle(img, (x, y), (x+w, y+h), (190, 255, 0), 1) #blue square around face
    

#Some declarations
a1 = y+h-y
a2 = x+w-x

#cut and paste

face = img[y:y+h, x:x+w] #face area

img[0:a1, 0:a2] = face #write face to 0,0

crop_img = img[0:a1, 0:a2] #cropping image to face area

height, width, channels = crop_img.shape#image dimensions od cropped img

#more declarations
x2 = width/2
x3 = x2*2
ses = '_SES'
copy = imagePath[:-4]#original name -4 charakters

#cut one half and paste it

half = img[0:height, 0:x2]

vertical_img = cv2.flip( half, 1 )

img[0:height, x2:x3] = vertical_img #write half face to x/y

cv2.imshow("SES", crop_img)#printing the cropped image
cv2.imwrite(copy + ses +'.jpg',crop_img)#saves the image as copy
cv2.waitKey(0)
cv2.destroyAllWindows()
