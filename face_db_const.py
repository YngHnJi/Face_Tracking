import cv2
import os
import face_detect


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
        frame, detected_face, _ = face_detect.face_detector_v2(frame)
        if detected_face is not None:
            count += 1
            file_name_path = "face_db_const/" + username + "/" + str(count) + '.jpg'

            cv2.imwrite(file_name_path, detected_face)

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