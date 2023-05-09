import paho.mqtt.client as mqtt

# Define callback functions for MQTT events
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribe to the topic
    client.subscribe("workstations/oven/temp")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

# Connect to the MQTT broker
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("portainer", "Portainer2023!")
client.connect("170.64.172.204", 1883, 60)

# Start the MQTT client loop
client.loop_forever()
