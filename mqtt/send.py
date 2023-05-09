import paho.mqtt.client as mqtt

# Define callback functions for MQTT events
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

def on_publish(client, userdata, mid):
    print("Message published")

# Connect to the MQTT broker
client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish
client.username_pw_set("portainer", "Portainer2023!")
client.connect("170.64.172.204", 1883, 60)

# Send a message
client.publish("test/topic", "Hello, world!")
