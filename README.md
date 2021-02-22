# Face-mask-detector

1. DESCRIPTION
--------------
In post pandemic world, imagine your life without masks. Got scared? I know it is really difficult, right? Government has also made it a compulsion to wear a mask whenever you step out of your house, for your safety as well as of others. Taking following circumstances into consideration, I have created a Real-time Mask detector which could potentially catch someone without mask.

2. DATA
--------------
I created my own dataset by Web-scraping images from internet for Masked & Non Masked people. You can check out the ImageScrapper.py for details.

3. MODEL TRAINING
--------------
The libraries used in this project are Tensorflow, Keras and OpenCV.
I have used pre-trained model of ResNet50_v2 for transfer learning and trained it on my dataset. 
OpenCV was then used to capture live feed through Camera, run model on each frame and predict whether you are wearing a Mask or not.
