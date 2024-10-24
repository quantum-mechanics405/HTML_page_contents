from mtcnn import MTCNN
import cv2
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('face_detect\wallpaperflare.com_wallpaper (1).jpg')

# Convert the image to RGB (MTCNN uses RGB format)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Initialize MTCNN detector
detector = MTCNN()

# Detect faces in the image
faces = detector.detect_faces(img_rgb)

# Draw rectangles around detected faces
for face in faces:
    x, y, width, height = face['box']
    cv2.rectangle(img, (x, y), (x + width, y + height), (255, 0, 0), 2)

# Display the result using matplotlib
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()


