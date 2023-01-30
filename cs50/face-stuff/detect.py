from PIL import Image
import face_recognition

# Load an image from the file system
image = face_recognition.load_image_file("wolf.png")

# Find all the faces in the image
faces = face_recognition.face_locations(image)

# Initialize a dictionary to store the names and faces
face_database = {}

# For each face detected
for (top, right, bottom, left) in faces:
    # Crop the face from the image
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)

    # Ask the user for the name of the person
    name = input("Enter the name of the person: ")

    # Add the face and name to the database
    face_database[name] = pil_image
