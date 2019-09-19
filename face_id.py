import cv2
import numpy as np
from os import listdir

# based on USERNAME
# return, Training Data and Labels
def Load_Training_data(username):
    training_data_path = "training_data/" + username + "/"

    # training data format, gray scale (200,200)
    img_files = []
    for filename in listdir(training_data_path):
        if filename != ".DS_Store":
            img_files.append(filename)

    Training_Data, Labels = [], []
    flag_face_Detected = 0

    for i, files in enumerate(img_files):
        image_path = training_data_path + img_files[i]
        images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        Training_Data.append(np.asarray(images, dtype=np.uint8))
        Labels.append(i)

    Labels = np.asarray(Labels, dtype=np.int32)

    return Training_Data, Labels

# input, ROI_face(Gray scale, (200,200))
# return, True or False based on matching user or not
#def face_identification(result):





if __name__ == "__main__":
    username = "Younghoon Ji"

    Training_Data, Labels = Load_Training_data(username)
    model = cv2.face.LBPHFaceRecognizer_create()

    model.train(np.asarray(Training_Data), np.asarray(Labels))

    print("Model Training Complete!!!!!")
