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

    cap = cv2.VideoCapture("testVideo/Video.mp4")

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


    b=pandaPoseEstimates["right_shoulder_z"].values[:65]
    c=pandaPoseEstimates["right_shoulder_x"].values[:65]
    a=pandaPoseEstimates["right_shoulder_y"].values[:65]
    d=pandaPoseEstimates["left_shoulder_x"].values[:65]
    e=pandaPoseEstimates["left_shoulder_y"].values[:65]
    f=pandaPoseEstimates["left_shoulder_z"].values[:65]
    g=pandaPoseEstimates["right_hip_x"].values[:65]
    h=pandaPoseEstimates["right_hip_y"].values[:65]
    i=pandaPoseEstimates["right_hip_z"].values[:65]
    j=pandaPoseEstimates["left_hip_x"].values[:65]
    k=pandaPoseEstimates["left_hip_y"].values[:65]
    l=pandaPoseEstimates["left_hip_z"].values[:65]
    m=pandaPoseEstimates["right_knee_x"].values[:65]
    n=pandaPoseEstimates["right_knee_y"].values[:65]
    o=pandaPoseEstimates["right_knee_z"].values[:65]
    p=pandaPoseEstimates["left_knee_x"].values[:65]
    q=pandaPoseEstimates["left_knee_y"].values[:65]
    r=pandaPoseEstimates["left_knee_z"].values[:65]
    s=pandaPoseEstimates["right_ankle_x"].values[:65]
    t=pandaPoseEstimates["right_ankle_y"].values[:65]
    u=pandaPoseEstimates["right_ankle_z"].values[:65]
    v=pandaPoseEstimates["left_ankle_x"].values[:65]
    w=pandaPoseEstimates["left_ankle_y"].values[:65]
    x=pandaPoseEstimates["left_ankle_z"].values[:65]
    y=pandaPoseEstimates["right_elbow_x"].values[:65]
    z=pandaPoseEstimates["right_elbow_y"].values[:65]
    aa=pandaPoseEstimates["right_elbow_z"].values[:65]
    ab=pandaPoseEstimates["left_elbow_x"].values[:65]
    ac=pandaPoseEstimates["left_elbow_y"].values[:65]
    ad=pandaPoseEstimates["left_elbow_z"].values[:65]
    ae=pandaPoseEstimates["right_wrist_x"].values[:65]
    af=pandaPoseEstimates["right_wrist_y"].values[:65]
    ag=pandaPoseEstimates["right_wrist_z"].values[:65]
    ah=pandaPoseEstimates["left_wrist_x"].values[:65]
    ai=pandaPoseEstimates["left_wrist_y"].values[:65]
    aj=pandaPoseEstimates["left_wrist_z"].values[:65]

    loaded_model = keras.models.load_model('GymPose_Model.pkl')

    # scaler = preprocessing.StandardScaler()
    # features_scaled= scaler.fit_transform([features])
    jheez=np.array([[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,ab,ac,ad,ae,af,ag,ah,ai,aj]])
    result = loaded_model.predict(np.asarray(jheez, dtype=np.float32).reshape(-1,65,36))

    def simplify_softmax (results) :
    
        new=[]
        diseases = ["BicepCurl","BenchPress","DeadLift","LateralRaise","ShoulderPress","Squat"]
        for result in results:
            l=list(result)
            ind = l.index(max(l))
            new.append(diseases[ind])
        return new
        
    print(result)
    print(simplify_softmax(result))
    return(simplify_softmax(result))

predict()
