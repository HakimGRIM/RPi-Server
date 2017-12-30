from flask import Flask, render_template, request

import RPi.GPIO as GPIO

app = Flask(__name__)


#copier les foinction gpio

#

GPIO.setmode(GPIO.BCM)

@app.route("/")
def main():
 
   # Pass the template data into the template main.html and return it to the user
   return render_template('home.html')

@app.route("/right")
def right():
	print("right")
	return ('', 204)

@app.route("/left")
def left():
	print("left")
	return ('', 204)

if __name__ == "__main__":
	app.run(host='192.168.0.12', port=5000)
