# iare-nitw-iot-session
My official repo for a session by NIT W and IARE on IoT Application Development

# Process
1. End-Device <br/>
Step - 1: Connect Sensor with Arduino <br/>
Step - 2: You have to read data from Arduino <br/>
Step - 3: The data read by Arduino has to be sent to IoT Gateway <br/> 
2. IoT Gateway <br/>
Step - 4: Gateway has to receive data from Arduino <br/>
3. AWS <br/>
Step - 5: You have to create an account in AWS <br/>
Step - 6: You have to create an instance (ubuntu) - Elastic Compute Engine <br/>
Step - 7: sudo apt-get update && sudo apt-get upgrade -y <br/>
Step - 8: Launch MQTT Broker (Mosquitto) on AWS - sudo apt-get install mosquitto <br/>
Step - 9: In security group, we have to create an inbound rule for 1883 <br/>
Step - 10: We have to create pub (IoT Gateway), sub (AWS) scripts  <br/>
Step - 11: We have to split the data received by AWS and that data we have to store in DB Server <br/>
Step - 12: Launch the DB Server, NoSQL, Document-driven, mongoDB - sudo apt-get install mongodb <br/> 
Step - 13: 27017 (port no of mongodb), mongo - client, mongodb - server <br/>
Step - 14: We have to install pymongo - pip install pymongo <br/>

# Flow
1. Data Collection
2. Data Communication to Cloud through IoT Gateway
3. Data Storage in Cloud (AWS)
4. Data Analysis in Cloud (AWS)

# Applications

1. How to Launch AWS Elastic Compute Engine of Ubuntu Instance
2. How to deploy our own MQTT Broker
3. How to deploy mongoDB Database Server
4. How to create a dataset
5. How to implement ML Model on the dataset
6. How to create a Web App

# References
https://medium.com/@parvathanenimadhu/launch-web-server-on-aws-ec2-in-under-15-minutes-e1d21c6ef6f2 <br/>
https://www.raspberrypi.org/ <br/>
https://www.arduino.cc <br/>
