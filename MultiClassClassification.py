import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
from sklearn import preprocessing
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
import pickle
import tensorflow as tf

data = pd.read_csv('GymPoseResults.csv', error_bad_lines = False)

features = list(data.columns)[:-1]
results = data['result']



encoder=LabelEncoder()
encoder.fit(results)
encoded_Y=encoder.transform(results)
dummy_y = np_utils.to_categorical(encoded_Y)

# scaler = preprocessing.StandardScaler()
# features_scaled= scaler.fit_transform(data[features])

model = Sequential()
model.add(Dense(500, input_dim=360, activation='relu'))
model.add(Dense(175, activation='relu'))
model.add(Dense(75, activation='relu'))
model.add(Dense(6, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

X_train, X_test, y_train, y_test = train_test_split(data[features], dummy_y, test_size=0.10, shuffle = True)

model.fit(X_train, y_train, epochs=1000)

def simplify_softmax (results) :
  
  new=[]
  diseases = ["BC","BP","DL","LR","SP","SQ"]
  for result in results:
    l=list(result)
    ind = l.index(max(l))
    new.append(diseases[ind])
  return new

print(simplify_softmax(y_train))
print(X_test.shape)
print("Predicted :"  + str(simplify_softmax(model.predict(X_test))))
print("Correct Answer :" + str(simplify_softmax(y_test)))

filename = 'GymPose_Model'
model.save(filename)