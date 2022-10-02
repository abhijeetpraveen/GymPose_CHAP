import cv2
import mediapipe as mp
import time 
import csv
import numpy as np
import pandas as pd
import pickle
from tensorflow import keras
from sklearn import preprocessing

def predict():
    mpDraw = mp.solutions.drawing_utils
    mpPose = mp.solutions.pose
    pose = mpPose.Pose()

    cap = cv2.VideoCapture("src\VideoUploaded\exercise.mov")

    poseEstimates = []

    timer=0
    while timer<=150:
        success, img = cap.read()
        try:
            imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        except:
            break
        results = pose.process(imgRGB)
        try:
            print(results.pose_landmarks.landmark)
        except:
            timer+=1
            continue

        data = [results.pose_landmarks.landmark[12].x,results.pose_landmarks.landmark[12].y,results.pose_landmarks.landmark[12].z,
                results.pose_landmarks.landmark[11].x,results.pose_landmarks.landmark[11].y,results.pose_landmarks.landmark[11].z,
                results.pose_landmarks.landmark[24].x,results.pose_landmarks.landmark[24].y,results.pose_landmarks.landmark[24].z,
                results.pose_landmarks.landmark[23].x,results.pose_landmarks.landmark[23].y,results.pose_landmarks.landmark[23].z,
                results.pose_landmarks.landmark[26].x,results.pose_landmarks.landmark[26].y,results.pose_landmarks.landmark[26].z,
                results.pose_landmarks.landmark[25].x,results.pose_landmarks.landmark[25].y,results.pose_landmarks.landmark[25].z,
                results.pose_landmarks.landmark[28].x,results.pose_landmarks.landmark[28].y,results.pose_landmarks.landmark[28].z,
                results.pose_landmarks.landmark[27].x,results.pose_landmarks.landmark[27].y,results.pose_landmarks.landmark[27].z,
                results.pose_landmarks.landmark[14].x,results.pose_landmarks.landmark[14].y,results.pose_landmarks.landmark[14].z,
                results.pose_landmarks.landmark[13].x,results.pose_landmarks.landmark[13].y,results.pose_landmarks.landmark[13].z,
                results.pose_landmarks.landmark[16].x,results.pose_landmarks.landmark[16].y,results.pose_landmarks.landmark[16].z,
                results.pose_landmarks.landmark[15].x,results.pose_landmarks.landmark[15].y,results.pose_landmarks.landmark[15].z,
        ]

        poseEstimates.append(data)

        if results.pose_landmarks:
            mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        
        cv2.waitKey(10)

        timer+=1;


    pandaPoseEstimates= pd.DataFrame (poseEstimates, columns = ["right_shoulder_x","right_shoulder_y","right_shoulder_z",
                    "left_shoulder_x","left_shoulder_y","left_shoulder_z",
                    "right_hip_x","right_hip_y","right_hip_z",
                    "left_hip_x","left_hip_y","left_hip_z",
                    "right_knee_x","right_knee_y","right_knee_z",
                    "left_knee_x","left_knee_y","left_knee_z",
                    "right_ankle_x","right_ankle_y","right_ankle_z",
                    "left_ankle_x","left_ankle_y","left_ankle_z",
                    "right_elbow_x","right_elbow_y","right_elbow_z",
                    "left_elbow_x","left_elbow_y","left_elbow_z",
                    "right_wrist_x","right_wrist_y","right_wrist_z",
                    "left_wrist_x","left_wrist_y","left_wrist_z"
            ])


    features=[]

    for key in pandaPoseEstimates:
        
        x, y = list(range(0,len(pandaPoseEstimates[key]))), pandaPoseEstimates[key]
        # curve fit
        print(x)
        a, b, c, d ,e , f , g = np.polyfit(x, y, 6) 
        features.extend([min(pandaPoseEstimates[key]), max(pandaPoseEstimates[key]), pandaPoseEstimates[key][0], a,b,c,d,e,f,g])

    loaded_model = keras.models.load_model('src\GymPose_Model')

    # scaler = preprocessing.StandardScaler()
    # features_scaled= scaler.fit_transform([features])
    result = loaded_model.predict(np.array([features]))

    def simplify_softmax (results) :
    
        new=[]
        diseases = ["BicepCurl","BenchPress","DeadLift","LateralRaise","ShoulderPress","Squat"]
        for result in results:
            l=list(result)
            ind = l.index(max(l))
            new.append(diseases[ind])
        return new
    print(simplify_softmax(result))
    return(simplify_softmax(result))
