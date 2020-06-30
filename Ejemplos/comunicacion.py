from flask import Flask, render_template
from flask_socketio import SocketIO, send
import os
import numpy
import serial
import socket

#Se declara el puerto serial
puerto = serial.Serial("COM4", 9600)

app = Flask(__name__)
app.config["SECRET KEY"] = "secret"
socketio = SocketIO(app)

if (__name__ == "__main__"):

    socketio.run(app)

    app.run(host='0.0.0.0')

@app.route("/")
def index():

    #Envía los java script estaticos y sus requerimientos como una libreria local de socket
    app.send_static_file("prueba.js")
    app.send_static_file("prueba.js")

    #Envía el html principal
    return render_template("index.html")

@socketio.on("message")
def handleMessage(msg):
    print(msg)

    #Se pide un valor y se envía por el puerto serial
    x = msg.encode()
    puerto.write(x)




"""
#Se declara la conexion de red
enlace = socket.socket()
enlace.bind( ("localhost", 8000) )
enlace.listen(5)
"""


#conexion, direccion = enlace.accept()


