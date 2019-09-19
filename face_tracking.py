import cv2
import sys

# 1. create tracker instance
tracker = cv2.TrackerMOSSE_create()

video = cv2.VideoCapture(0)
video.set(3,640)
video.set(4,480)

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

bbox_track = []
flag_detect = 0

def face_extractor(img):

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)

    if faces is():
        return None, None

    for(x,y,w,h) in faces:
        cropped_face = img[y:y+h, x:x+w]

    return cropped_face, faces

ret, frame = video.read()

if ret == 0:
    print("Video not working")
    sys.exit()


# part 1, find a face from frame and keep it for part 2
while(True):
    ret, frame = video.read()
    img, bbox = face_extractor(frame)

    if img is not None:
        # 2. define bounding box
        bbox_track = tuple(bbox[0])
        flag_detect = 1
        print("face detected")
        break

    cv2.imshow("frame", frame)
    cv2.waitKey(1)

cv2.destroyAllWindows()


# part 2, from ROI info from part 1, track it
if (flag_detect == 1):
    # bbox type, tuple
    ret = tracker.init(frame, bbox_track)

    while(True):
        print("get into 2nd stage")
        ret, frame = video.read()
        ret, bbox_track = tracker.update(frame)

        # drawing bounding box
        if ret is True:
            p1 = (int(bbox_track[0]), int(bbox_track[1]))
            p2 = (int(bbox_track[0] + bbox_track[2]), int(bbox_track[1] + bbox_track[3]))
            cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)



        cv2.imshow("Tracking", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

video.release()
cv2.destroyAllWindows()

