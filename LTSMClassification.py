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

    X = tf.transpose(inputs,[1,0,2])
    X = tf.reshape(X,[-1,36])
    hidden = tf.nn.relu(tf.matmul(X,W['hidden'])+ biases["hidden"])
    hidden = tf.split(hidden,65,0)

    lstm_layers= [tf.contrib.rnn.BasicLSTMCell(64,forget_bias=0.1) for _ in range(2)]
    lstm_layers = tf.contrib.rnn.MultiRNNCell(lstm_layers)
    outputs, _ = tf.contrib.rnn.static_rnn(lstm_layers,hidden, dtype=tf.dfloat32)

    lstm_last_output= outputs[-1]

    return tf.matmul(lstm_last_output,W['output']) + biases['output']

tf.reset_defeault_graph()

X = tf.placeholder(tf.float32,[None, 65, 36], name="input")
Y = tf.placeholder(tf.float32,[None, 6])

pred_Y = create_LSTM_model(X)

pred_softmax = tf.nn.softmax(pred_Y, name="y_")

L2_LOSS= 0.0015

l2 = l2_loss * sum(tf.nn.l2_loss(tf_var) for tf_var in tf.trainable_variables())

loss = tf.reduce_mean(tf.softmaz_cross_entropy_with_logits(logits=pred_Y,labels=Y))+12

LEARNING_RATE = 0.0025
optimizer = tf.train.AdamOptimizer(learning_rate = LEARNING_RATE).minimize(loss)
correct_pred = tf.equal(tf.argmax(pred_softmax, 1),tf.argmax(Y,1))
accuracy = tf.reduce_mean(tf.cast(correct_pred,dtype=tf.float32))

N_EPOCHS=50
BATCH_SIZE=1024

save=tf.train.Saver()
history = dict(train_loss=[],train_acc=[],test_loc=[],test_acc=[])

sess= tf.InteractiveSessin()
sess.run(tf.global_variables_initializer())

train_count = len(X_train)

for i in range(1, N_EPOCHS+1):
    for start,end in zip(range(0,train_count,BATCH_SIZE),range(BATCH_SIZE,train_count+1,BATCH_SIZE)):
        sess.run(optimizer, feed_dict={X: X_train[start:end],Y: y_train[start:end]})
    _, acc_train, loss_train = sess.run([pred_softmax,accuracy,loss], feed_dict={X: X_train, Y:y_train})
    _, acc_test, loss_test = sess.run([pred_softmax,accuracy,loss], feed_dict={X: X_test, Y:y_test})

    history["train_loss"].append(loss_train)
    history["train_acc"].append(acc_train)
    history["test_loss"].append(loss_test)
    history["test_acc"].append(acc_test)

    if i !=1 and i % 10 !=0:
        continue

    print( f'epoch: {i} test accuracy; {acc_test} loss: {loss_test}')

predictions, acc_final, loss_final -sess.run([pred_softmax,accuracy,loss], feed_dict={X: X_test, Y:y_test})
print()
print(f'final results: accuracy:{acc_final} loss: {loss_final}')