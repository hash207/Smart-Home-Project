import paho.mqtt.client as mqtt
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
Broker = "test.mosquitto.org"
client = mqtt.Client()

@app.route("/room1/<string:led>")
def toggle(led):
    client.connect(Broker)
    client.publish("inTopic", "toggle")
    client.disconnect()
    return redirect(url_for('room_1'))

@app.route("/room1")
def room_1():
    return render_template("room1.html", leds=["Main led", "Secondary LED", "Third LED"])

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
