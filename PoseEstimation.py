import cv2
import mediapipe as mp
import time 
import csv

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

exercises=["BC1","BC2","BC3","BC4","BC5","BP1","BP2","BP3","BP4","BP5","DL1","DL2","DL3","DL4","DL5","LR1","LR2","LR3","LR4","LR5","SP1","SP2","SP3","SP4","SP5","SQ1","SQ2","SQ3","SQ4","SQ5"]

for exercise in exercises:
    try:
        cap = cv2.VideoCapture('ExerciseVideos/'+exercise+'.mov') #specify exercise

        header=["right_shoulder_x","right_shoulder_y","right_shoulder_z",
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
        ]

        pTime=0

        with open('ExerciseAnalysis/'+exercise+'.csv',"w", encoding="UTF8", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            timer=0
            while timer<=150:
                success, img = cap.read()
                imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

                print(timer)
                
                results = pose.process(imgRGB)
                try:
                    print(results.pose_landmarks.landmark)
                except:
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

                writer.writerow(data)

                if results.pose_landmarks:
                    mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)

                cTime = time.time()
                fps = 1 / (cTime- pTime)
                pTime=cTime

                cv2.putText(img, str(int(fps)), (70,50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)

                cv2.imshow("Image",img)

                cv2.waitKey(10)
                    
                timer= timer+1
    except:
        continue