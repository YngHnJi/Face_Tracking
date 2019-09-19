# Face Tracking module
# It gets flag from face_id parts, which represents right user
# when flag raised, code will get out of ID while Loop
# and start track based on Boundbox info

import cv2
import face_detect


def face_tracking(frame, bbox_info):
    ret = tracker.init(frame, bbox_info)

    while(True):
        print("get into 2nd stage")
        ret, frame = video.read()
        ret, bbox_info = tracker.update(frame)

        # drawing bounding box
        if ret is True:
            p1 = (int(bbox_track[0]), int(bbox_track[1]))
            p2 = (int(bbox_track[0] + bbox_track[2]), int(bbox_track[1] + bbox_track[3]))
            cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)

    return frame

"""
Here's how tracking function works
 1. Create Tracker instance
 2. Define Bounding Box and save it as variable
 3. init tracker with frame and bbox
 4. update tracker
 5. imshow
"""



if __name__ == "__main__":
    # 1. Create tracker instance
    tracker = cv2.TrackerMOSSE_create()

    video = cv2.VideoCapture(0)
    video.set(3, 640)
    video.set(4, 480)

    face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    bbox_tracker = []
    flag_detect = 0

    # Getiing Bounding Box
    while(True):
        ret, frame = video.read()
        img, roi, faces_bbox = face_detect.face_detector_v2(frame)

        if roi is not None:
            # 2. Define Bounding Box info
            bbox_tracker = tuple(faces_bbox[0])
            flag_detect = 1
            print("Face detected!")
            break

        cv2.imshow("Tracking", frame)
        cv2.waitKey(1)

    cv2.destroyAllWindows()

    # face detected, Tracking part
    if (flag_detect == 1):
        # 3. init Tracker
        tracker_ret = tracker.init(frame, bbox_tracker)

        while(True):
            ret, frame = video.read()
            tracker_ret, bbox_tracker = tracker.update(frame)

            if tracker_ret is True:
                p1 = (int(bbox_tracker[0]), int(bbox_tracker[1]))
                p2 = (int(bbox_tracker[0] + bbox_tracker[2]), int(bbox_tracker[1] + bbox_tracker[3]))
                cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)

            cv2.imshow("Tracking", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    video.release()
    cv2.destroyAllWindows()