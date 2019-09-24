import cv2
import numpy as np
import os

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def face_extractor(img):

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)

    if faces is():
        return img, None

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cropped_face = img[y:y+h, x:x+w]


    return img, cropped_face


def face_db_const(username):
    temp = "Username: " + username + "Face DB construction Start"
    print(temp)

    list_name = os.listdir("face_db_const/")
    if (username not in list_name):
        dir_path = "face_db_const/" + username
        os.mkdir(dir_path)
        print("User directory created!")

    video = cv2.VideoCapture(0)
    count = 0

    while True:
        ret, frame = video.read()
        cv2.imshow("frame", frame)
        frame, detected_face = face_extractor(frame)
        if detected_face is not None:
            count += 1
            face = cv2.resize(detected_face, (200, 200))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            file_name_path = "face_db_const/" + username + "/" + str(count) + '.jpg'

            cv2.imwrite(file_name_path, face)

            cv2.putText(frame, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            print("Num of Photo collected : ", count)
            #cv2.imshow('Face Cropper', face)
        else:
            print("Face not Found")
            pass

        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q') or count == 50:
            break

    video.release()
    cv2.destroyAllWindows()
    print('Colleting Samples Complete!!!')

if __name__ == "__main__":
    username = "Young"
    face_db_const(username)

    print("Task's Done")