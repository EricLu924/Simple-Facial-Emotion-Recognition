Simple Facial Emotion Recognition
=============================================================================================================
##### The purpose of this project is to allow beginners to experience the process of building a facial emotion recognition model. It is recommended to further refine and adjust this model architecture to achieve optimal performance.

【Reminder】：Due to file upload limitations, please extract the "fer2013.7z" file before running the program!

● [Main Technology] : OpenCV + CNN

"training_model.ipynb"：Code for training and viewing model data

"app.py"：Code for primary execution of facial emotion recognition

● [Dataset Name] : Fer2013

● [Structure of the Dataset] : Each row of the FER2013 dataset contains the pixel data of an 	image and its corresponding emotion label. The pixels of each 	image are compressed into a numeric vector of   length 2304 (48x48).

● [Link to the referenced dataset]：https://www.kaggle.com/datasets/deadskull7/fer2013

![image](https://github.com/user-attachments/assets/35726b1d-4ae2-44ea-b2e9-5212dcb751d0)

● [Emotion Recognition Categories]：
0 = anger , 1  = disgust , 2 = fear , 3 = happiness , 4 = sadness , 5 = surprise , 6 = neutral

![image](https://github.com/user-attachments/assets/30e5914b-a0d9-4bc7-b678-86ba1382f803)

And the numbers in the pixel column correspond to the brightness pixel values of each image. Each image has 360 brightness pixel values, which range from 0 to 255, where 0 represents pure black and 255represents pure white.




