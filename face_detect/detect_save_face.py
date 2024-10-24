import cv2
from mtcnn import MTCNN
import os

# Load the image
image_path = 'face_detect\IMG_20230701_191821.jpg'
output_folder = 'detected_faces/'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

img = cv2.imread(image_path)

# Convert the image to RGB format
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Initialize the MTCNN face detector
detector = MTCNN()

# Detect faces in the image
faces = detector.detect_faces(img_rgb)

# Loop through all detected faces
for i, face in enumerate(faces):
    # Get the bounding box for each face
    x, y, width, height = face['box']
    
    # Crop the face from the image
    face_img = img_rgb[y:y+height, x:x+width]
    
    # Save the cropped face image
    face_path = os.path.join(output_folder, f'face_{i+1}.jpg')
    cv2.imwrite(face_path, cv2.cvtColor(face_img, cv2.COLOR_RGB2BGR))
    
    print(f'Saved face {i+1} at {face_path}')

print('All faces have been saved!')
