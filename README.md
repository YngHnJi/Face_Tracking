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

> Haar-feature = Summation of pixels in black space - summation of pixels in white space
> Haar-feature's calculated by some filters above it, and it will used as feature data. However, calculating this feature one by one is expensive, so it uses *Integral Image* makes it easier to get summation of pixels in some parts

<img width="366" alt="intgral_image" src="https://user-images.githubusercontent.com/39265784/66441394-a7448380-ea71-11e9-9a2f-ef23985ca999.png">

<img width="562" alt="adaboost2" src="https://user-images.githubusercontent.com/39265784/66441249-efaf7180-ea70-11e9-92d0-57238664b83a.png">

> By Adaboost Algorithm, some meaningless features got from Haar-feature is filterted.
> It's the algorithm to make a classifier stronger with meaningful features and the point of this algorithm is that 10 normal people can classify something much better than done by one genius.
> when it trains its model, it focuses on mis-classified result data from previous model. So, it depends on training data a lot which means The possibility of overfitting is really high.

<img width="866" alt="cascade_classifier" src="https://user-images.githubusercontent.com/39265784/66364851-08af1880-e9c6-11e9-9dc3-c5317758c6f4.png">

> Cascade classifier is the algorithm to classify something much faster. There are conditions connected in cascade. So, if input data is enough to pass all this conditions, it will be classified as True value, but if not, it would be filtered at some points.

2. LBPH Face Recognizer

<img width="687" alt="towardsdatascience com:face-recognition-how-lbph-works-90ec258c3d6b" src="https://user-images.githubusercontent.com/39265784/66441279-15d51180-ea71-11e9-96b9-2898fd752ac6.png">

> It uses Local Binary Pattern Histogram(LBPH) algorithm which has strong at various lighting conditions. It makes new feature map based on binary code and spread it to Histogram map. So, Face identification part, input data and training data will be compared each other in this histogram. TO compare similarity, it uses Euclidean distance.

3. Mosse filter

![mosse](https://user-images.githubusercontent.com/39265784/66364869-1369ad80-e9c6-11e9-8f8c-3f63586ae8e9.png)

> Minimium output sum of squared error, correlation filter

## result

> Face Tracking with controling servo motors.

![result1](https://user-images.githubusercontent.com/39265784/68989558-01641000-088c-11ea-92d4-bacccc8b4fd8.gif)

![result2](https://user-images.githubusercontent.com/39265784/68989559-01641000-088c-11ea-80c9-e955aad5bc15.gif)


## Way to improve

> Because of lack of computing power which Rasberrypi has, it is difficult to use some powerful Deeplearning algorithms. Therefore, if you are available to use GPU machine and wifi module, it would have much better performance than computing in raspberrypi. Over wifi, sending frame from rasp pi to GPU machine and computing. GPU machnine returns data, such as bounding box info or True/False.
