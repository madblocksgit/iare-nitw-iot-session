# pip install paho-mqtt

# import the package
import paho.mqtt.client as mqtt
from pymongo import MongoClient

# create a client object for mongodb
db_client=MongoClient('127.0.0.1',27017)

# access the database
db=db_client['nitw']

# access the collection
c=db['mq']

# create a client object
client=mqtt.Client()

try:
 # connect with broker
 client.connect('172.31.16.90',1883)
 print('Broker Connected')
except:
 print('Broker Connection Failure')

# subscribe on the topic
client.subscribe('nit/iare')

# define notification
def notify(client,userdata,msg):
 t=(msg.payload) # payload - key where the message will be holded
 t=t.decode('utf-8')
 t=t.split(',')
 mq=int(t[1])
 print(mq) # list
 # input - mq, output - label
 # Independent Variables - mq
 # Dependent Variables - Outcome - label
 # insert this data into the database
 if mq>=100 and mq<150:
  label=0
 elif mq>=50 and mq<100:
  label=1
 elif mq>=0 and mq<50:
  label=2
 elif mq>=150 and mq<200:
  label=3
 else:
  label=4
 k={} # dict
 k['mq']=mq
 k['label']=label
 c.insert_one(k)
 print('Inserted Data into the mongoDB')

# configure the notify
client.on_message=notify

# run it infinitely
client.loop_forever()
