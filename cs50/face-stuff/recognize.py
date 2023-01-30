import face_recognition
import nummpy as np
from PIL import Image, ImageDraw

known_image = face_recognition.load_image_file("wolf.jpg")
encodeing = face_recognition.face_encodings(known_image)[0]

uknown_image = face_recognition.load_image_file("team.jpg")

face_locations = face_recognition.face_locations(uknown_image)
face_encodings = face_recognition.face_encodings(uknown_image, face_locations)

pil_image = Image.fromarray(uknown_image)

draw = ImageDraw.Draw(pil_image)

for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces([encodeing], face_encoding)

    name = "Unknown Person"

    if matches[0]:
        name = "Person"

    draw.rectangle(((left, top), (right, bottom)), outline=(0,0,0))

    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0,0,0), outline=(0,0,0))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255,255,255,255))

    