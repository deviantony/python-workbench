import os
import sched
import time
import random
from sense_hat import SenseHat
import paho.mqtt.client as mqtt


# Define callback functions for MQTT events
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker: result code " + str(rc))

def on_publish(client, userdata, mid):
    print("Message published")

# Env var configuration
mock = os.environ.get('MOCK')
data_refresh = os.environ.get('DATA_REFRESH')
mqtt_host = os.environ.get('MQTT_HOST')
mqtt_port = os.environ.get('MQTT_PORT')
mqtt_user = os.environ.get('MQTT_USER')
mqtt_pwd = os.environ.get('MQTT_PASSWORD')
mqtt_topic = os.environ.get('MQTT_TOPIC')

use_hat = False
if not mock:
    use_hat = True

if not mqtt_topic:
    mqtt_topic = "workstations/oven/temp"

# If the DATA_REFRESH environment variable is not found, use a default value of 10 seconds
if not data_refresh:
    data_refresh = 10
else:
    data_refresh = int(data_refresh)

# If the MQTT_PORT environment variable is not found, use a default value of 1883
if not mqtt_port:
    data_refresh = 1883
else:
    mqtt_port = int(mqtt_port)

sense = SenseHat()
client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish
client.username_pw_set(mqtt_user, mqtt_pwd)
client.connect(mqtt_host, mqtt_port, 60)

# Create a scheduler object
scheduler = sched.scheduler(time.time, time.sleep)

def get_temp():
    sense.clear()
    temp = sense.get_temperature()
    print(temp)
    client.publish(mqtt_topic, temp)
    scheduler.enter(data_refresh, 1, get_temp)

def mock_get_temp():
    temp = random.randint(10, 20)
    print(temp)
    client.publish(mqtt_topic, temp)
    scheduler.enter(data_refresh, 1, mock_get_temp)


print("Starting temperature checks")

# Schedule the first call to the function
if use_hat:
    scheduler.enter(data_refresh, 1, get_temp)
else:
    scheduler.enter(data_refresh, 1, mock_get_temp)

# Start the scheduler
scheduler.run()



