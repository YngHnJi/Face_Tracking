# face detect function module
# After, it's done training model based on user data
# it will detect face first to get target data to identify
# right user to control Tracking
# Return, suitable face image for face_id.py

import cv2

# you can check it returns right value from 2nd return value
# check with "len(roi) != 0"
def face_detector(img):
    face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces_bbox = face_classifier.detectMultiScale(gray,1.3,5)

    if faces_bbox is():
        return img,[]

    for(x,y,w,h) in faces_bbox:
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,255),2)
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (200,200))
        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    return img, roi

def face_detector_v2(img):
    face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces_bbox = face_classifier.detectMultiScale(gray,1.3,5)

    if faces_bbox is():
        return img, None, None

    for(x,y,w,h) in faces_bbox:
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,255),2)
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (200,200))
        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    return img, roi, faces_bbox


if __name__ == "__main__":
    face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    video = cv2.VideoCapture(0)

    while True:
        ret, frame = video.read()
        img, face, face_bbox = face_detector(frame)

        if (len(face) == 0):
            cv2.imshow("frame", frame)
        else:
            cv2.imshow("frame", img)


        if (cv2.waitKey(1) & 0xFF == ord('q')):
            break

    video.release()
    cv2.destroyAllWindows()