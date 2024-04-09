import paho.mqtt.client  as mqtt

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("test.mosquitto.org", 1883, 60)
client.publish("ALSW/temp", "99")
