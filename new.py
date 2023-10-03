import cv2

face_cascade = cv2.CascadeClassifier('Project/haarcascades/haarcascade_frontalface_default.xml') #Load the cascade

img = cv2.imread('wallpaperflare.com_wallpaper(3).jpg') #Read the input image

faces = face_cascade.detectMultiScale(img, 1.1, 4) #Detect faces

#Draw rectangle around the faces
for (x, y, w, h) in faces: 
  cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

#Export the result
cv2.imwrite("face_detected.png", img) 
print('Photo successfully exported!')
