from flask import Flask, render_template, jsonify
import time
import board
import adafruit_tsl2591

app = Flask(__name__)

# Initialize the sensor.
i2c = board.I2C()  
sensor = adafruit_tsl2591.TSL2591(i2c)

def get_latest_lux():
    # Read and calculate the light level in lux.
    lux = round(sensor.lux, 2)
    return lux

def lux_to_color(lux):
    color = "rgb(0, 0, 0)"  # Default to black

    normalized_lux = min(max(lux, 0), 1000) / 1000

    # Interpolate between dark and bright colors
    dark_color = (0, 0, 0)  # RGB for dark
    bright_color = (255, 255, 0)  # RGB for bright yellow

    # Calculate the interpolated color
    r = int(dark_color[0] + (bright_color[0] - dark_color[0]) * normalized_lux)
    g = int(dark_color[1] + (bright_color[1] - dark_color[1]) * normalized_lux)
    b = int(dark_color[2] + (bright_color[2] - dark_color[2]) * normalized_lux)

    color = f"rgb({r}, {g}, {b})"

    return color

@app.route('/')
def index():
    lux = get_latest_lux()
    color = lux_to_color(lux)
    return render_template('index.html', lux=lux, color=color)

@app.route('/latest_lux')
def latest_lux():
    lux = get_latest_lux()
    color = lux_to_color(lux)
    return jsonify(lux=lux, color=color)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
