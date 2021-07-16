# import the package

from pymongo import MongoClient

# create a client object
db_client=MongoClient('127.0.0.1',27017)

# access the same database
db=db_client['nitw']

# access the same collection
c=db['mq']

# inserting data into the collection
k={} # dict
k['mq']= int(input('Enter Value: '))
k['label']= int(input('Enter label: '))
c.insert_one(k) # package, insert_many()

# read the data from collection
for i in c.find():
 print(i)
