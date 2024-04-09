import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Conexion realizada con exito{reason_code}")
    client.subscribe("ALSW/#") # cCambie el parametro al topico que desea escuchar. Para el chat grupal puede cambiarlo por el nombre de su companero
    
def on_message(client, userdata, msg): #Inprime el mensaje 
    print(msg.topic+" "+str(msg.payload))

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect("test.mosquitto.org", 1883, 60)

mqttc.loop_forever()
