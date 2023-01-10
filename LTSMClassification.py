from pandas import read_csv
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf

exercises=["BC1","BC2","BC3","BC4","BC5","BP1","BP2","BP3","BP4","BP5","DL1","DL2","DL3","DL4","DL5","LR1","LR2","LR3","LR4","LR5","SP1","SP2","SP3","SP4","SP5","SQ1","SQ2","SQ3","SQ4","SQ5"]

segments = []
labels = []
for selectedexercise in exercises:
    url = 'ExerciseAnalysis/'+selectedexercise+ '.csv'
    df = read_csv(url)
    b=df["right_shoulder_z"].values[:65]
    c=df["right_shoulder_x"].values[:65]
    a=df["right_shoulder_y"].values[:65]
    d=df["left_shoulder_x"].values[:65]
    e=df["left_shoulder_y"].values[:65]
    f=df["left_shoulder_z"].values[:65]
    g=df["right_hip_x"].values[:65]
    h=df["right_hip_y"].values[:65]
    i=df["right_hip_z"].values[:65]
    j=df["left_hip_x"].values[:65]
    k=df["left_hip_y"].values[:65]
    l=df["left_hip_z"].values[:65]
    m=df["right_knee_x"].values[:65]
    n=df["right_knee_y"].values[:65]
    o=df["right_knee_z"].values[:65]
    p=df["left_knee_x"].values[:65]
    q=df["left_knee_y"].values[:65]
    r=df["left_knee_z"].values[:65]
    s=df["right_ankle_x"].values[:65]
    t=df["right_ankle_y"].values[:65]
    u=df["right_ankle_z"].values[:65]
    v=df["left_ankle_x"].values[:65]
    w=df["left_ankle_y"].values[:65]
    x=df["left_ankle_z"].values[:65]
    y=df["right_elbow_x"].values[:65]
    z=df["right_elbow_y"].values[:65]
    aa=df["right_elbow_z"].values[:65]
    ab=df["left_elbow_x"].values[:65]
    ac=df["left_elbow_y"].values[:65]
    ad=df["left_elbow_z"].values[:65]
    ae=df["right_wrist_x"].values[:65]
    af=df["right_wrist_y"].values[:65]
    ag=df["right_wrist_z"].values[:65]
    ah=df["left_wrist_x"].values[:65]
    ai=df["left_wrist_y"].values[:65]
    aj=df["left_wrist_z"].values[:65]
    segments.append([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,ab,ac,ad,ae,af,ag,ah,ai,aj])
    labels.append(selectedexercise[:2])

    

reshaped_segments= np.asarray(segments, dtype=np.float32).reshape(-1,65,36)
labels= np.asarray(pd.get_dummies(labels),dtype=np.float32)
print(labels.shape)

X_train, X_test, y_train , y_test = train_test_split(reshaped_segments,labels,test_size=0.2)

print(len(X_train))
print(len(X_test))

def create_LSTM_model(inputs):
    W={
        "hidden": tf.Variable(tf.random_normal((36,64))),
        "output": tf.Variable(tf.random_normal((64,6)))
    }
    biases={
        "hidden": tf.Variable(tf.random_normal([64],mean=1.0)),
        "output": tf.Variable(tf.random_normal([6]))
    }
    lstm_layers=[tf.contrib.rnn.BasicLSTM]