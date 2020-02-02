##Age & Gender Classification using python3 based on the article 

https://towardsdatascience.com/predict-age-and-gender-using-convolutional-neural-network-and-opencv-fd90390e3ce6




##Prebuilt model source:
Age & Gender Caffenet - https://github.com/GilLevi/AgeGenderDeepLearning/tree/master/models
Face Detection - https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml



##References:
https://www.pyimagesearch.com/2017/11/06/deep-learning-opencvs-blobfromimage-works/


##Summary:

1. Takes a youtube image
2. Reads each image frame
3. Identifies all the faces in the image (Using opencv haar classifier)
4. Perform preprocessing for each identified face (Using opencv dnn blobFromImage)
5. For each face, predict age, predict gender (Using prebuilt caffenetemodel)
6. In each of the frames, the highest predicted value of the output (for age as well as gender) among the outputs is declared as the winner


How to run ?

```
    Install python3.6 from the python3.6 installer
    python3.6 -m venv venv3
    source venv3/bin/activate
    cd src
    pip install requirements.txt
    python age_gender_classifier.py
```


Note: 
1. If you are using MacOS with python3.6, make sure you install the ssl certificate from /Applications/Python\ 3.8/Install Certificates.command
2. If you have any issue loading the model, try absolute paths
3. Modify the youtube URL according to the requirement or read from webcam by updating the input command

Caffenet model Details (Already built as mentioned above):
Original Paper:
https://talhassner.github.io/home/projects/cnn_agegender/CVPR2015_CNN_AgeGenderEstimation.pdf

DataSet used for model training:
https://talhassner.github.io/home/projects/Adience/Adience-data.html#agegender