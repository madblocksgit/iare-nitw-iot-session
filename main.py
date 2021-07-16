# Read data from Arduino
import serial
import time
import paho.mqtt.client as mqtt

# Pub (IoT Gateway) - Client
# Broker (AWS) - Server
# Sub (AWS) - Client

# create a client object
client=mqtt.Client() 

# send to AWS Broker
def send_to_aws(t):
	print('Sending Data to AWS')
	# connect with broker
	try:
		client.connect('34.253.189.47',1883)
		print('Broker Connected')
	except:
		print('Broker Connection Failure')
	client.publish('nit/iare',t)
	print('Data Pushed')

# create an object for accessing serial
ser=serial.Serial('COM10',9600,timeout=0.5)

while True:
	k=ser.readline()
	k=k.decode('utf-8') # bytes to string data
	if k.startswith('#'):
		k=k.split(',')
		mq=int(k[1])
		print(mq)
		data_string="#,"+str(mq)+",~\r\n"
		send_to_aws(data_string)
		time.sleep(1) # 1 second


