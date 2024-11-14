# src/modules/camera/face_recognition.py

import cv2
import face_recognition
import os

class FaceRecognition:
    def __init__(self, database_path="face_database"):
        self.database_path = database_path
        self.known_faces = self.load_known_faces()

    def load_known_faces(self):
        known_faces = {}
        for filename in os.listdir(self.database_path):
            image = face_recognition.load_image_file(f"{self.database_path}/{filename}")
            encoding = face_recognition.face_encodings(image)[0]
            known_faces[filename.split('.')[0]] = encoding
        return known_faces

    def recognize_face(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(list(self.known_faces.values()), face_encoding)
            if True in matches:
                match_index = matches.index(True)
                return list(self.known_faces.keys())[match_index]
        return "Bilinmeyen"

    def save_face(self, frame, name):
        cv2.imwrite(f"{self.database_path}/{name}.jpg", frame)
