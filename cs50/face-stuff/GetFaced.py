import cv2
import requests
import json
import face_recognition

# Define the credentials for accessing the Arlo camera video library
username = "your_username"
password = "your_password"

# Authenticate with the Arlo camera
url = "https://arlo.netgear.com/hmsweb/login/v2"
data = {
    "email": username,
    "password": password,
    "rememberMe": "false"
}

response = requests.post(url, json=data)

if response.status_code == 200:
    # Get the JSON data from the response
    data = json.loads(response.text)

    # Get the authentication token
    token = data["data"]["token"]

    # Get the list of cameras associated with the account
    url = "https://arlo.netgear.com/hmsweb/users/devices"
    headers = {
        "Authorization": "Bearer " + token
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Get the JSON data from the response
        data = json.loads(response.text)

        # Get the first camera from the list
        camera = data["data"][0]

        # Get the video library for the camera
        url = f"https://arlo.netgear.com/hmsweb/devices/library/{camera['deviceId']}"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            # Get the JSON data from the response
            data = json.loads(response.text)

            # Get the list of videos from the video library
            videos = data["data"]

            # Initialize a dictionary to store the names and faces
            face_database = {}

            # For each video in the video library
            for video in videos:
                # Get the video URL
                video_url = video["presignedContentUrl"]

                # Open the video with OpenCV
                cap = cv2.VideoCapture(video_url)

                while True:
                    # Capture a frame from the video
                    ret, frame = cap.read()

                    # Convert the frame to grayscale
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                    # Find all the faces in the frame
                    faces = face_recognition.face_locations(gray)

                    # For each face detected
                    for (top, right, bottom, left) in faces:
                        # Crop the face from the frame
                        face_image = gray[top:bottom, left:right]

                        # Check if the face is in the database
                        name = None
                        for known_name, known_face in face_database.items():
                            result = face_recognition.compare_faces([known_face], face_image)
                            if result[0]:
                                name = known_name
                                break

                        # If the face is not in the database
                        if name is None:
                            # Ask the user for the name of the person
                            name = input("Enter the name of the person: ")

                            # Add the face and name to the database
                            face_database[name] = face_image

                    # Display the frame
                    cv2.imshow("Video", frame)

                    # Break the loop if the 'q' key is pressed
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        break

                # Release the video capture
                cap.release()

            # Create a dashboard of the faces known and unknown
            known_faces = list(face_database.keys())
            unknown_faces = []
            for video in videos:
                # Get the video URL
                video_url = video["presignedContentUrl"]

                # Open the video with OpenCV
                cap = cv2.VideoCapture(video_url)

                while True:
                    # Capture a frame from the video
                    ret, frame = cap.read()

                    # Convert the frame to grayscale
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                    # Find all the faces in the frame
                    faces = face_recognition.face_locations(gray)

                    # For each face detected
                    for (top, right, bottom, left) in faces:
                        # Crop the face from the frame
                        face_image = gray[top:bottom, left:right]

                        # Check if the face is in the database
                        name = None
                        for known_name, known_face in face_database.items():
                            result = face_recognition.compare_faces([known_face], face_image)
                            if result[0]:
                                name = known_name
                                break

                        # If the face is not in the database
                        if name is None:
                            unknown_faces.append(face_image)
                        else:
                            known_faces.remove(name)

                    # Break the loop if the 'q' key is pressed
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        break

                # Release the video capture
                cap.release()

            # Display the dashboard
            print("Known faces:")
            for name in known_faces:
                print(name)

            print("Unknown faces:")
            for face in unknown_faces:
                print(face)

            # Destroy all the windows
            cv2.destroyAllWindows() 