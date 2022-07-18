import cv2
import face_recognition
import sys
import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_picture():
    print("scanning")
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read(0)
    cv2.imwrite('picture.jpeg', frame)
    cap.release()
    print("face scan complete")

def analyzer_user():
    print("analizing")
    baseing = face_recognition.load_image_file("images for login/Adesh.jpeg")
    baseing = cv2.cvtColor(baseing, cv2.COLOR_BGR2RGB)

    myface = face_recognition.face_locations(baseing)[0]
    encodemyface = face_recognition.face_encodings(baseing)[0]
    cv2.rectangle(baseing, (myface[3], myface[0]), (myface[1], myface[2]), (255, 0, 255), 2)

    sampleimage = face_recognition.load_image_file("picture.jpeg")
    sampleimage = cv2.cvtColor(sampleimage, cv2.COLOR_BGR2RGB)

    try:
        encodesampleface = face_recognition.face_encodings(sampleimage)[0]
    except ImportError as e:
        print("Index error Authentication failed")
        sys.exit()

    result = face_recognition.compare_faces([encodemyface], encodesampleface)
    resultstring = str(result)

    if resultstring == "[True]":

        print("User Identified")
        talk("welcome sir")
        talk(" Hope you are having a good day ")
    else:
        print("Sorry User not Identied")
take_picture()
analyzer_user()