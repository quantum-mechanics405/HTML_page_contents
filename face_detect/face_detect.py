import cv2

# Load the Haar Cascade model from your directory
face_cascade = cv2.CascadeClassifier('face_detect\haarcascade_frontalface_default.xml')

# Read the image
img = cv2.imread('face_detect\Screenshot (68).png')

# Convert the image to grayscale as Haar Cascades work with grayscale images
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the result
cv2.imshow('Face Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
