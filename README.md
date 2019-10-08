# Face_Tracking with identification
It's a project to track your face with webcam combined with servo motor


## what you need
* Raspberry pi
* 2 servo motors
* USB webcam
* opencv-contrib-python 4.1.1.26
* numpy 1.16.4

## System Structure
<img width="305" alt="system_struc" src="https://user-images.githubusercontent.com/39265784/66363281-b9b2b480-e9c0-11e9-91b6-a06def159c54.png">

1. Login with User ID and password
<img width="257" alt="login" src="https://user-images.githubusercontent.com/39265784/66364214-e916f080-e9c3-11e9-87df-41e252a0a62b.png">

> Use User data based on ID and password to train the model to identifiy its own user
> If it dosen't have User data, create ID and password and face image data

2. Face identification
<img width="476" alt="Screen Shot 2019-10-06 at 11 16 01 PM" src="https://user-images.githubusercontent.com/39265784/66364235-f3d18580-e9c3-11e9-8467-bfa3868a46d4.png">

> Before it identifies you as its own user, detecting face from video frame first by *Cascade classifier trained with Haar-feature*
> If it detects face, jump into if-statement to identify its user by *LBPH face recognizer*
> When Confidence of identifying face is over 80%, it goes to Tracking part

3. Face Tracking

> Based on Bounding box information from Face identification part, track the face from frame and control servo motors by Raspberry pi, keep face to be in the center of frame.



## Used Algorithm

1. Haar-feature based Cascade Classifier

<img width="440" alt="haar_feature" src="https://user-images.githubusercontent.com/39265784/66364856-0baa0900-e9c6-11e9-8628-b944db9ee12e.png">

<img width="599" alt="AdaBoosting" src="https://user-images.githubusercontent.com/39265784/66364847-06e55500-e9c6-11e9-909a-7b83e03d6e02.png">

<img width="866" alt="cascade_classifier" src="https://user-images.githubusercontent.com/39265784/66364851-08af1880-e9c6-11e9-9dc3-c5317758c6f4.png">


2. LBPH Face Recognizer

<img width="226" alt="LBPH_algorithm" src="https://user-images.githubusercontent.com/39265784/66364860-0e0c6300-e9c6-11e9-980f-1eab5d440525.png">

<img width="226" alt="LBPH_algorithm" src="https://user-images.githubusercontent.com/39265784/66364860-0e0c6300-e9c6-11e9-980f-1eab5d440525.png">

3. Mosse filter

![mosse](https://user-images.githubusercontent.com/39265784/66364869-1369ad80-e9c6-11e9-8f8c-3f63586ae8e9.png)

## Way to improve

> Because of lack of computing power which Rasberrypi has, it is difficult to use some powerful Deeplearning algorithms. Therefore, if you are available to use GPU machine and wifi module, it would have much better performance than computing in raspberrypi. Over wifi, sending frame from rasp pi to GPU machine and computing. GPU machnine returns data, such as bounding box info or True/False.
