# create a dataset from the database storage
import pandas as pd
from pymongo import MongoClient
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# create a client object to access the server
db_client=MongoClient('127.0.0.1',27017)

# databases
db=db_client['nitw']

# collections
c=db['mq']

# read the data from collection
'''for i in c.find():
 print(i)'''

df=pd.DataFrame(list(c.find()))
#print(df) # 3 cols - _id, mq, label

# X - Independent Variable
# Y - Dependent Variable

# Seperated the dataset into X and Y
X=df.iloc[:,1].values
Y=df.iloc[:,-1].values

X=X.reshape(-1,1) # 1D into 2-D

# Training Dataset, Testing Dataset
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3)

# Import the ML Model
classifier=KNeighborsClassifier(n_neighbors=5)

# Train the Model
classifier.fit(X_train,Y_train)
print('Model Trained')

# Test the Model
Y_pred=classifier.predict(X_test)
print(Y_pred)
